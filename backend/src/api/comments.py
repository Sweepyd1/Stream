from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from utils import ConnectionManager

comments = APIRouter("/api/comments", tags=["эндпоинты связанные с видео"])


# @comments.websocket("/ws/comments")
# async def websocket_endpoint(manager:ConnectionManager, websocket: WebSocket, client_id: int):
#     await manager.connect(websocket)
#     try:
#         while True:
#             data = await websocket.receive_text()
#             await manager.send_personal_message(f"You wrote: {data}", websocket)
#             await manager.broadcast(f"Client #{client_id} says: {data}")
#     except WebSocketDisconnect:
#         manager.disconnect(websocket)
#         await manager.broadcast(f"Client #{client_id} left the chat")
        
        
        

@comments.post("/put_like_comments")
async def put_like():
    pass        


@comments.delete("/delete_like_comments")
async def put_like():
    pass





@comments.get("/get_comments_for_episode/{episode_id}")
async def get_comments_for_episode():
    pass 


@comments.post("/new_comment")
async def get_comments_for_episode():
    pass        