import re
import os
import time
from os import environ

# Shortlink API configuration
API = environ.get("API", "fe23807ec922f660e8b6040140cf08da97c23015") # shortlink api
URL = environ.get("URL", "Modijiurl.com") # shortlink domain without https://
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/TamilRockerz_TR/150") # how to open link 
BOT_USERNAME = environ.get("BOT_USERNAME", "Kali_Rename_Bot") # bot username without @
VERIFY = environ.get("VERIFY", "True") == "True"  # Convert string to boolean

id_pattern = re.compile(r'^.\d+$')

class Config(object):
    # pyro client config
    API_ID = os.environ.get("API_ID", "27823209")  # ⚠️ Required
    API_HASH = os.environ.get("API_HASH", "1d693fcf3bfea119ca1d9057b08a4495")  # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6874458800:AAGtBuL9TQy8wXZuFLqtrrKoVwxGbWv7r7s")  # ⚠️ Required

    # premium 4g renaming client
    STRING_API_ID = os.environ.get("STRING_API_ID", "11679491")
    STRING_API_HASH = os.environ.get("STRING_API_HASH", "553478fb890172dfdea9bf3d47e067d5")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQCyNwMAbV4eXr89sLQNyoc78HXCqLyr8P_SC4Fxy9_cgOyOq7oiLYt7kNhRD3o7kg0-BoBD9YllXrNXKTWFnCcPe_ON_wGqQ2mP8kcBhKbN1CofB-LDOcWtBBVjLyneM4OHQobKFUp8le-qB-3jve1krijW-lZgT8z2INtyJcy63FrzLfg8sw9bXy1m7a5nzI4yHbyq6-OPwbHN_lHUrMvhGE12m3pdrzk-MT4PhqYLsLtCgjnaC6MsPutyKGJveiZ6qn2NnWYXXaV3EJbv0WxiZ-zpxcbU050DhTk1fEMB9VY376B3CPdl0RXZSN5p9yiIJ1gAxnbbg8xLZKmhBa0gjtOTPwAAAAFxMeNwAA")

    # database config
    DB_NAME = os.environ.get("DB_NAME", "Cluster0")
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://filerename:filerename@cluster0.sd0p4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # ⚠️ Required

    # other configs
    BOT_UPTIME = time.time()
    START_PIC = os.environ.get("START_PIC", "https://envs.sh/IMz.jpg")
    ADMIN = [int(admin) if id_pattern.search(
        admin) else admin for admin in os.environ.get('ADMIN', '6004928770').split()]  # ⚠️ Required
    
    FORCE_SUB = os.environ.get("FORCE_SUB", "TamilRockerz_TR") # ⚠️ Required Username without @
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002014126653"))  # ⚠️ Required
    FLOOD = int(os.environ.get("FLOOD", '105'))
    BANNED_USERS = set(int(x) for x in os.environ.get(
        "BANNED_USERS", "1234567890").split())

    # wes response configuration
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))

    # Add the missing attributes
    VERIFY = VERIFY
    BOT_USERNAME = BOT_USERNAME
    VERIFY_TUTORIAL = VERIFY_TUTORIAL


class Txt(object):
    # part of text configuration
    START_TXT = """<b>Hɪ {} ♡゙,\n\n◈ I Aᴍ A Pᴏᴡᴇʀғᴜʟ Fɪʟᴇ Rᴇɴᴀᴍᴇʀ Bᴏᴛ.
◈ I Cᴀɴ Rᴇɴᴀᴍᴇ Fɪʟᴇs ᴜᴘᴛᴏ 4GB, Cʜᴀɴɢᴇ Tʜᴜᴍʙɴᴀɪʟs, Cᴏɴᴠᴇʀᴛ Bᴇᴛᴡᴇᴇɴ Vɪᴅᴇᴏ Aɴᴅ Fɪʟᴇ, Aɴᴅ Sᴜᴘᴘᴏʀᴛ Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟs Aɴᴅ Cᴀᴘᴛɪᴏɴs.\n\n• Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ : @Straw_Hat_Bots
"""

    ABOUT_TXT = """<b>╭───────────⍟
• ᴍy ɴᴀᴍᴇ : {}
• ᴘʀᴏɢʀᴀᴍᴇʀ : <a href=https://t.me/Urr_Sanjii>𝐒ᴀɴJɪ 𝐒αᴍᴀ</a>
• ɴᴇᴛᴡᴏʀᴋ : <a href=https://t.me/TamilRockerz_TR>🦋 𝐓𝐚𝐦𝐢𝐥𝐑𝐨𝐜𝐤𝐞𝐫𝐳 𝐓𝐑 🦋</a>
• ᴄʜᴀᴛ ɢʀᴏᴜᴘ: <a href=https://t.me/Movies_Request_TR>sᴜᴘᴘᴏʀᴛ</a>
• ᴍʏ ᴏᴡɴᴇʀ / ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/King_of_Kali>༄㉿ᴬℓ𝓲࿐</a>
╰───────────────⍟ """

    HELP_TXT = """
🌌 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ</u></b>
  
<b>•></b> /start Tʜᴇ Bᴏᴛ Aɴᴅ Sᴇɴᴅ Aɴy Pʜᴏᴛᴏ Tᴏ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟy Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /del_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /view_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴɪʟᴇ.


📑 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u></b>

<b>•></b> /set_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ ᴀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /see_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /del_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
Exᴀᴍᴩʟᴇ:- <code> /set_caption 📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration} </code>

✏️ <b><u>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</u></b>
<b>•></b> Sᴇɴᴅ Aɴy Fɪʟᴇ Aɴᴅ Tyᴩᴇ Nᴇᴡ Fɪʟᴇ Nᴀᴍᴇ \nAɴᴅ Aᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ document, video, audio ].           


<b>➜ ᴘᴏᴡᴇʀᴇᴅ ʙʏ:</b> <a href=https://t.me/TamilRockerz_TR>🦋 𝐓𝐚𝐦𝐢𝐥𝐑𝐨𝐜𝐤𝐞𝐫𝐳 𝐓𝐑 🦋</a>
"""

    SEND_METADATA = """
❪ SET CUSTOM METADATA ❫

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:-

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="Powered By:- @TamilRockerz_TR" -metadata author="@TamilRockerz_TR" -metadata:s:s title="Subtitled By :- @TamilRockerz_TR" -metadata:s:a title="By :- @TamilRockerz_TR" -metadata:s:v title="By:- @TamilRockerz_TR" </code>

📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛ. @King_of_Kali
"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱➜
➜ 🗃️ sɪᴢᴇ: {1} | {2}
➜ ⏳️ ᴅᴏɴᴇ : {0}%
➜ 🚀 sᴘᴇᴇᴅ: {3}/s
➜ ⏰️ ᴇᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➜ </b>"""
