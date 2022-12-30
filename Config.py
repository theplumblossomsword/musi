import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "21927988"))
    API_HASH = os.environ.get("API_HASH", "e18f720acdff1e5b0ec80616aecd8a5a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5879384212:AAFHPL8fpCP6cl1L5jA4xHmX4Sz-S_fzivM")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOGsBuwO8Knx8hwvikSyhH61oB63VgYua3glDkO6pVRj8lNP_0tL8SclQge6pd_tri3RmUhvEIbSVIDqomncycl_bgBWiBYuXuKS1QQkNWhHA7I_QWX5_TQ199Xh6XwzHBGu4EwDd5087oJXeVRhXGN4hKGAfhxOBCCECPtIxVzno_XgmDFQpeydyezI8gQvZP1vhBkWOeoBw_kQjEvW4NbazBQX3lQ2GUMjvaKqDCbGeQ6n8cxWUCkjNz3MhssWKhv3944g2HxZ0YLB1Qx-uqqPH4zMODK9Lq5Q6l-lB3-vKerQFupzsZcZ6GvOeQiiV1HA0_rA8T9hnwTRne-u93yb0Vu0=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Shuna_utabot")
    SUPPORT = os.environ.get("SUPPORT", "theoneandonlymurim") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "rimurubotsupdates") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/599709741897bf71697a1.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/9cb323f8cc384c729d2fb.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5865826050")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', "False") # Change it to "True"
