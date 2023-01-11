import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "21927988"))
    API_HASH = os.environ.get("API_HASH", " e18f720acdff1e5b0ec80616aecd8a5a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5863608616:AAElYyHFTa2huSfefBzN_uHwekPF4iEE3Io")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOL8Bu5vI6KGJ9nQmvAn4LXAPyo9t2WpTcY6g3qr6CqFJ1i4AEAD5EFa7ka0yHP66Diydc-K5dKpHNgbnup5M_Q174msQrI6NaSy4MZ1xx0PtQI-mrULgG0GvLuHwHW6_bk91IbqStXQPegzL-OHRmYXQ1MVHXuOnlfm99LZUOaii3xggmRPSry7J9m-XuGTVf2RhGvnAlAjf9N6M8nSlOkub92X40ikguc62Zl2ovL5ifS41eKdIFSdyRqJXwk9QxfiQPVw21lB-EBLAQrW-wOTjtMM1x9iETTcT1HUEjBXeB7x6LYklIOlY9Q1-6HUY3KE_bUvxTWeCacVjWZOYBU7QEkE=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Manbagi_MusicBot")
    SUPPORT = os.environ.get("SUPPORT", "theoneandonlymurim")
    CHANNEL = os.environ.get("CHANNEL", "rimurubotsnetwork")
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/681cc533d6ec55794180f.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/2dc5c1c4e0063ab40efc3.jpg")
