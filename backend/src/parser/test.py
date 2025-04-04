from anicli_api.source.animego import Extractor


sources = (
    Extractor()
    .search("lain")[0]
    .get_anime()
    .get_episodes()[0]
    .get_sources()
)

videos = sources[0].get_videos(transport=None,  
                               headers={"User-Agent": "i'm crushing :("})

print(videos)