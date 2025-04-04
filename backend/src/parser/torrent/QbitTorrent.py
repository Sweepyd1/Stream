from qbittorrent import Client

# Подключаемся к qBittorrent
qb = Client('http://127.0.0.1:8080/')
qb.login('username', 'password')

# Загрузка торрент-файла
with open('my_torrent_file.torrent', 'rb') as torrent_file:
    qb.download_from_file(torrent_file)

print('Torrent added to qBittorrent.')
