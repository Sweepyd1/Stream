from parser.parser import AniLibriaParser
from config import cfg




parser = AniLibriaParser(cfg.anime_api.data_api, cfg.anime_api.download_api, cfg.anime_api.image_api)