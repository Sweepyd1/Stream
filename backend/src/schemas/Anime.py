from pydantic import BaseModel
from typing import List, Union


class Anime(BaseModel):
    title: str
    cover_url:Union[None, str]
    video_url:Union[None, str]
    genres: Union[List[str], str]
    
    def json_serialize(self):
        return self.model_dump()





