import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "21927988"))
    API_HASH = os.environ.get("API_HASH", "e18f720acdff1e5b0ec80616aecd8a5a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5879384212:AAFHPL8fpCP6cl1L5jA4xHmX4Sz-S_fzivM")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOGsBu2mzr3A9aH-a5aJPD5kIP34gH8WAUWkYE53JatwXtYNA1vhOmY_yeB8ez7xopkWs_Nu0mdr7VIw1Q6-nWwTN5BT7_d7CyQCFi7-sZKvTIoy21lEbJS7USFrdX_EAwVlcK4UVbaumPzZxVZr7jLR7CxzASaoh5hLUvvv4_RWaBPJUQR_SdwB9olqYfjlZASV1KQmpA918OAvf2s7Vuzvfi8N9LhkOViCNIzhrFzNTMOWBXe7e5AD8CqsKKJjYsdfGNybzB9HNuUcWiAoKopXw_OIm5pK2IKpjBm-ceJfovu8rhGHJwT801SbIW95Ywqe6uh7kBJCxcxYktXiF6cC9txQ=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Shuna_utabot")
    SUPPORT = os.environ.get("SUPPORT", "theoneandonlymurim") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "rimurubotsupdates") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/599709741897bf71697a1.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/9cb323f8cc384c729d2fb.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "RedeyeTempest")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
