import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "21927988"))
    API_HASH = os.environ.get("API_HASH", "e18f720acdff1e5b0ec80616aecd8a5a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5879384212:AAFHPL8fpCP6cl1L5jA4xHmX4Sz-S_fzivM")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOGsBu0mCeCecmJlIDPbT-0xEXrboJLLzvkoc54eGCMrxc-i6zng_TP7J-bQCa_lihghpL9gHI5nL9o-ws57m_0NTLA-oWlpY5yFM7ZTE6h6IjAXyTtzOXaHlMZW3vThrLoEnv3aGTuix5eljBTVtBiYdncQhoI0QT7DEOHhVIY35aDZWnNRedv672erBeHB8OdggHPuzgiEL996Ng_QLffzquW2il1ORfguGXeNWkJEQXq0MjSgG4HrYKP5EwG_C_cuV0hVgyZIV58ZLgiCnqwhLCIntdAGnKnTkEd5Dj-EkjQjD4QzBxJpbZH5hRRu1lLdeBFvypn7nnhE0mLfZ790Ji38=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Shuna_utabot")
    SUPPORT = os.environ.get("SUPPORT", "theoneandonlymurim") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "rimurubotsupdates") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/599709741897bf71697a1.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/9cb323f8cc384c729d2fb.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "1131567642")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', "False") # Change it to "True"
