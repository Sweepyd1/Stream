from redis.asyncio import Redis, from_url 

async def get_redis() -> Redis:
    redis = await from_url("redis://localhost")
    try:
        await redis.ping() 
        return redis
    except Exception as e:
        await redis.close()
        raise e