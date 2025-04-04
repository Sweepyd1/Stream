import requests
def process_anilibria_json():
    json_data = requests.get("https://api.anilibria.tv/v2/getRandomTitle")
    json_data = json_data.json()
    # anime_data = {
    #     'id': json_data['id'],
    #     'title_ru': json_data['names']['ru'],
    #     'title_en': json_data['names']['en'],
    #     'posters': f"{json_data['posters']['original']['url']}" if json_data['posters'] else None,
    #     'genres': json_data['genres'],
    #     'description': json_data['description'],
    #     'in_favorites': json_data['in_favorites']
    # }
    print(json_data)

process_anilibria_json()