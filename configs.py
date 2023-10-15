# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "20389440"))
    API_HASH = getenv("API_HASH", "a1a06a18eb9153e9dbd447cfd5da2457")
    BOT_TOKEN = getenv("BOT_TOKEN", "6413115065:AAGAIXWmI00Zf_-7GVKASEQL0B5BIaWMJCU")
    FSUB = getenv("FSUB", "IrisMoviesCh")
    CHID = int(getenv("CHID", "-1001747312807"))
    SUDO = list(map(int, getenv("SUDO", "730412993").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://bvv:gRXsDeLnAdE71DPu@cluster0.2on6kqk.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
