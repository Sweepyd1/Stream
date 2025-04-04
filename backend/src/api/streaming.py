from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from aiohttp import ClientSession
from loader import parser
import json
from utils.utils import async_timed
from cache.redis import get_redis
from redis.asyncio import Redis

stream = APIRouter(prefix="/api/stream", tags=["эндпоинты связанные с видео"])

@stream.get("/get_serial_for_main_page/")
@async_timed()
async def get_serial_for_main_page(redis: Redis = Depends(get_redis)):
    cache_key = "anime"
    # await redis.delete(cache_key)
    
    if cached_data := await redis.get(cache_key):
        return json.loads(cached_data)

    data = await parser.get_data_for_main_page()
    
    serialized_data = [item.json_serialize() for item in data]
    
    await redis.setex(cache_key, 600, json.dumps(serialized_data))

    return data  
        
@stream.get("/redis-test")
async def redis_test(redis: Redis = Depends(get_redis)):
    await redis.set("test", "OK", ex=10)
    value = await redis.get("test")
    return {"status": value}

@stream.get("/test/")
async def test():
    return await parser.test()


@stream.get("/get_video/{video_id}")
async def get_video_by_id():
    pass

@stream.get("/get_serial/{serial_id}")
async def get_serial_by_id():
    pass
