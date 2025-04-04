from parser.parser import AniLibriaParser
from config import cfg

from database.db_manager import DatabaseManager


parser = AniLibriaParser(cfg.anime_api.data_api, cfg.anime_api.download_api, cfg.anime_api.image_api)