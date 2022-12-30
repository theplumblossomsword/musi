import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "24833791"))
    API_HASH = os.environ.get("API_HASH", "42488cb247a33d13d5f97d6839c8e52b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5879384212:AAFHPL8fpCP6cl1L5jA4xHmX4Sz-S_fzivM")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOGsBu34AZd_riHQj1E2pACuuS5s2YtNqX-JtqWLXo9Fj2Zg0HMDl_dl5FDR8CiNrzNJs8R74iR_WAEbWnyeSzRHib6SwS6-_jWBrdK2bp9RQOQDtk4OVpxT9L1ZmFdDV283a65h50kkxS48f0-mDAf3_7rv4Z2zsmU1NUSYplTl5kn-ryoukDQabnJyRyJsoUdlLNoKHrgJyx-kAWfuHrjtQv4ssBWdZAMqMLl695zGlrZSZbXuQcxNG5ilOY4DH-MnJCR6LgaTfhM2BYXNMbAxW3WLMJpqOorhkcrtF1XYuPZ5-T_quJEg7YELetp1jnqT2_TfoZyZ1RAxC33KMj5PpjcQ=")
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
