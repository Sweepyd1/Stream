def kek():
    import requests
    import json  # Импортируем модуль для работы с JSON

    response = requests.get("https://api.jikan.moe/v4/anime?q=naruto")
    data = response.json()

    # Красивое форматирование с отступами и корректной кодировкой
    formatted_json = json.dumps(data, indent=2, ensure_ascii=False)
    print(formatted_json)

    with open("anime_data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    print("Данные сохранены в anime_data.json")

    for anime in data["data"][:5]:
        print(json.dumps(anime, indent=2, ensure_ascii=False))

    print(data.keys())  # Увидеть все ключи верхнего уровня



def lol():
    import requests
    import time

    # 1. Находим ID аниме "Наруто"
    search_url = "https://api.jikan.moe/v4/anime"
    params = {"q": "Naruto", "limit": 1}  # Берем первый результат

    try:
        # Запрос поиска
        search_response = requests.get(search_url, params=params)
        search_response.raise_for_status()  # Проверка на ошибки
        search_data = search_response.json()
        
        if not search_data["data"]:
            print("Аниме не найдено.")
            exit()

        anime_id = search_data["data"][0]["mal_id"]
        print(f"ID аниме 'Наруто': {anime_id}")

        # 2. Запрашиваем список эпизодов
        episodes_url = f"https://api.jikan.moe/v4/anime/{anime_id}/episodes"
        time.sleep(1)  # Задержка для соблюдения лимитов API
        
        episodes_response = requests.get(episodes_url)
        episodes_response.raise_for_status()
        episodes_data = episodes_response.json()

        if not episodes_data["data"]:
            print("Информация о сериях отсутствует.")
            exit()

        # Получаем первую серию
        first_episode = episodes_data["data"][0]
        print(f"\nПервая серия:")
        print(f"Название: {first_episode['title']}")
        print(f"Номер: {first_episode['mal_id']}")
        print(f"URL на MyAnimeList: {first_episode['url']}")  # Ссылка на страницу эпизода

    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")


def tree():
    # Пример ссылки на Crunchyroll (требует проверки доступности)
    crunchyroll_url = f"https://www.crunchyroll.com/watch/{20}/episode-1"
    