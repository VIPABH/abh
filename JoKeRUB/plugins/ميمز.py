#all write Codes By Team Aljoker @jepthon
#By Hussein @lMl10l
import asyncio
import random
import re
import json
import base64
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from asyncio.exceptions import TimeoutError
from telethon import events
from ..sql_helper.memes_sql import get_link, add_link, delete_link, BASE, SESSION, AljokerLink
from telethon.errors.rpcerrorlist import YouBlockedUserError
#ياقائم آل محمد
from JoKeRUB import l313l
from ..helpers.utils import reply_id
plugin_category = "tools"
    
@l313l.on(admin_cmd(pattern="حالتي ?(.*)"))
async def _(event):
    await event.edit("**- يتم التاكد من حالتك اذا كنت محظور او لا**")
    async with bot.conversation("@SpamBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=178220800)
            )
            await conv.send_message("/start")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("** اولا الغي حظر @SpamBot وحاول مجددا**")
            return
        await event.edit(f"- {response.message.message}\n @jepthon")


@l313l.on(admin_cmd(pattern="الاغنية ?(.*)"))
async def _(event):
    "To reverse search music by bot."
    if not event.reply_to_msg_id:
        return await event.edit("**▾∮ يجب الرد على الاغنيه اولا**")
    reply_message = await event.get_reply_message()
    chat = "@auddbot"
    try:
        async with event.client.conversation(chat) as conv:
            try:
                await event.edit("**▾∮ يتم التعرف على الاغنية انتظر**")
                start_msg = await conv.send_message("/start")
                response = await conv.get_response()
                send_audio = await conv.send_message(reply_message)
                check = await conv.get_response()
                if not check.text.startswith("Audio received"):
                    return await event.edit(
                        "**▾∮ يجب ان يكون حجم الاغنيه من 5 الى 10 ثواني **."
                    )
                await event.edit("- انتظر قليلا")
                result = await conv.get_response()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("```Mohon buka blokir (@auddbot) dan coba lagi```")
                return
            namem = f"**الأغنية : **{result.text.splitlines()[0]}\
        \n\n**التفاصيـل : **{result.text.splitlines()[2]}"
            await event.edit(namem)
            await event.client.delete_messages(
                conv.chat_id,
                [start_msg.id, send_audio.id, check.id, result.id, response.id],
            )
    except TimeoutError:
        return await event.edit("***حدث خطا ما حاول مجددا**")


@l313l.on(admin_cmd(pattern="ايميل وهمي(?: |$)(.*)"))
async def _(event):
    chat = "@TempMailBot"
    geez = await event.edit("**جاري انشاء بريد ...**")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=220112646)
            )
            await conv.send_message("/start")
            await asyncio.sleep(1)
            await conv.send_message("/create")
            response = await response
            l313lmail = (response).reply_markup.rows[2].buttons[0].url
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await geez.edit("**الغي حظر @TempMailBot  و حاول مجددا**")
            return
        await event.edit(
            f"الايميل الخاص هو `{response.message.message}`\n[ اضغط هنا لرؤية من رسائل الايميل الواردة]({l313lmail})"
        )
#السلام على الحسين وعلى الارواح التي حلت بفنائك ولعن الله قاتليك
@l313l.on(admin_cmd(outgoing=True, pattern="افتار$"))
async def aljoker313(joker313):
  rl = random.randint(4,52)
  url = f"https://t.me/iamMUAOL/{rl}"
  await joker313.client.send_file(joker313.chat_id,url,caption="᯽︙  اذكر القائم",parse_mode="html")
  await joker313.delete()
    
@l313l.on(admin_cmd(outgoing=True, pattern="متروك$"))
async def jepvois(vois):
  rl = random.randint(4, 40)
  url = f"https://t.me/themuaol/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="᯽︙  اذكر القائم",parse_mode="html")
  await vois.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="قران$"))
async def jepvois(vois):
  rl = random.randint(2,101)
  url = f"https://t.me/QuraanJep/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="᯽︙ اذكر القائم",parse_mode="html")
  await vois.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="لطمية$"))
async def jepThe(theme):
  rl = random.randint(19,149)
  url = f"https://t.me/x04ou/{rl}"
  await theme.client.send_file(theme.chat_id,url,caption="᯽︙  اذكر القائم ",parse_mode="html")
  await theme.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="لتغلط$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/4"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ببجي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1134"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="نشاقة$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/3"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="احب الله$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/2"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="هع$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1165"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="شنهي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1115"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="تف$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1161"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="شش$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/79"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ماذا$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/81"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="هه$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/338"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="نية$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1157"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="مرهم$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/537"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="سبحان$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/541"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="طط$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/طط"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="لاا$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/571"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="زيج$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/VIPABH/1171"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="زيج2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/memesoundjep/20"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="(عبود|شيلة عبود)"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/VIPABH/1162"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="وخر$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/589"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="هههه$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/memesoundjep/44"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="انجب$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/592"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="امريكا$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1113"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="شسوي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1114"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ها$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1115"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="لتغلطط$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/memesoundjep/4"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="مي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1116"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="انعل$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/597"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="فلا"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1160"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="طاح$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/612"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="شماته$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/memesoundjep/37"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ماكدر$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/memesoundjep/38"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="لب$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/614"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="خوش$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/memesoundjep/57"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="صل$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/735"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ط$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/736"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="يولن$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/292"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ههه$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1164"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="كعبة"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1155"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="شبيك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1163"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="دكي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/987"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="نعال$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1156"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="دنجب$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/988"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="روح$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/memesoundjep/71"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="مزنجر$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/997"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="الهي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/23"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ملحد$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/55"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="يدكتور$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1107"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="بط"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/VIPABH/1168"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="اي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1098"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="الماوارثها$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1093"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="يامرحبا$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/memesoundjep/60"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="نيو$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/5"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="نوكيا$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1111"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ايرور$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/7"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="بوربه$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1159"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="طبك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/memesoundjep/65"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="سييي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/66"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="سبيدر مان"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/67"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="خاف حرام$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/68"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="تحيه لاختك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/69"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="نيه$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/71"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="امشي كحبة$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/72"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="امداك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/73"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="الحس$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/74"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="افتهمنا$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/75"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="اطلع$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/77"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="اوني تشان"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/78"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="اخت التنيج$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/79"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="اوني تشان2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/97"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="كعدت الديوث$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/98"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="خبز يابس$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/100"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="خيار بصل$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/101"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ماي ارو$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/102"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
