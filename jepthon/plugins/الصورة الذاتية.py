from jepthon import *
from jepthon import jepiq
from ..Config import Config
from ..sql_helper.globals import gvarstatus

Jepthon_CMD = Config.SCPIC_CMD or "ذاتية"
@jepiq.on(admin_cmd(pattern=f"{Jepthon_CMD}"))
async def dato(event):
    if not event.is_reply:
        return await event.edit("..")
    lMl10l = await event.get_reply_message()
    pic = await lMl10l.download_media()
    SC_TEXT = gvarstatus("SC_TEXT") or "**احا 😍**"
    await bot.send_file(
        "me",
        pic,
        caption=f"""
-تـم جـلب الصـورة بنجـاح ✅
- CH: @Jepthon
- Dev: @lMl10l
  """,
    )
    await event.edit(" 🙂❤️ ")
