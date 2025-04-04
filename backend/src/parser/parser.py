from aiohttp import ClientSession
import asyncio
# from schemas.Anime import Anime
from typing import List
from schemas.Anime import Anime



class AniLibriaParser:
    def __init__(self, data_api:str, download_api:str, image_api:str) -> None:
        self.data_api = data_api
        self.download_api = download_api
        self.image_api = image_api

    async def fetch_data(self, url, session: ClientSession):
        try:
            async with session.get(url) as response:
                response.raise_for_status()  
                return await response.json() 
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None  
     
    async def get_data_for_main_page(self):
        data = []
        async with ClientSession() as session:
            urls = [self.data_api + str(i) for i in range(9000, 9010)]
            
         
            requests = [self.fetch_data(url, session) for url in urls]
            
            for completed in asyncio.as_completed(requests):
                result = await completed
                if result is not None:
                    try:  
                        cover = self.data_api + result.get("posters").get("small").get("url")
                        episode = self.download_api + result.get("player", {}).get("list", {}).get("1", {}).get("hls", {}).get("fhd")
                    except TypeError:
                        episode = None
                    
                    genres = result.get("genres")
                    title = result.get("names").get("ru")
                    
                    
                    print(cover)
                    print(episode)
                    
                    print(genres)
                    print(title)
                    
                    anime = Anime(title=title, cover_url=cover, video_url=episode, genres=genres)
                    data.append(anime)
                    
              
                    
            return data
                   
        
    async def save_response_to_db(self):
        pass 
    
    
    async def download_episodes(self, session, url):
        try:
            async with session.get(url) as response:
                response.raise_for_status()  
                return response  
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None 
        
    async def test(self,):
        return "test succsfuely"

class JikanAPI:
    def __init__(self):
        pass

    