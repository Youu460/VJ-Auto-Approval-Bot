# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, errors, enums
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
from database import add_user, add_group, all_users, all_groups, users, remove_user
from configs import cfg
import random, asyncio

app = Client(
    "approver",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_chat_join_request(filters.group | filters.channel)
async def approve(_, m : Message):
    op = m.chat
    kk = m.from_user
    try:
        add_group(m.chat.id)
        await app.approve_chat_join_request(op.id, kk.id)
        await app.send_message(kk.id, "**Hello {}!\nWelcome To {}\n\n__Powerd By : @VJ_Botz __**".format(m.from_user.mention, m.chat.title))
        add_user(kk.id)
    except errors.PeerIdInvalid as e:
        print("user isn't start bot(means group)")
    except Exception as err:
        print(str(err))    
 
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Start ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.private & filters.command("start"))
async def op(_, m :Message):
    try:
        await app.get_chat_member(cfg.CHID, m.from_user.id)
    except:
        try:
            invite_link = await app.create_chat_invite_link(int(cfg.CHID))
        except:
            await m.reply("𝙈𝙖𝙠𝙚 𝙎𝙪𝙧𝙚 𝙄 𝘼𝙢 𝘼𝙙𝙢𝙞𝙣 𝙄𝙣 𝙔𝙤𝙪𝙧 𝘾𝙝𝙖𝙣𝙣𝙚𝙡")
            return 
        key = InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("⚓️ 𝙅𝙤𝙞𝙣 𝘾𝙝𝙖𝙣𝙣𝙚𝙡", url=invite_link.invite_link),
                InlineKeyboardButton("♻️ 𝘾𝙃𝙀𝘾𝙆 𝘼𝙂𝘼𝙄𝙉 ♻️", callback_data="chk")
            ]]
        ) 
        await m.reply_text("**⚠️Access Denied!⚠️\n\n👀𝙋𝙡𝙚𝙖𝙨𝙚 𝙅𝙤𝙞𝙣 𝙈𝙮 𝙐𝙥𝙙𝙖𝙩𝙚 𝘾𝙝𝙖𝙣𝙣𝙚𝙡 𝙏𝙤 𝙐𝙨𝙚 𝙈𝙚.𝙄𝙛 𝙔𝙤𝙪 𝙅𝙤𝙞𝙣𝙚𝙙 𝙏𝙝𝙚 𝘾𝙝𝙖𝙣𝙣𝙚𝙡 𝙏𝙝𝙚𝙣 𝘾𝙡𝙞𝙘𝙠 𝙊𝙣 𝘾𝙝𝙚𝙘𝙠 𝘼𝙜𝙖𝙞𝙣 𝘽𝙪𝙩𝙩𝙤𝙣 𝙏𝙤 𝘾𝙤𝙣𝙛𝙞𝙧𝙢**", reply_markup=key)
        return 
    keyboard = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("📺 𝘾𝙃𝘼𝙉𝙉𝙀𝙇", url="https://t.me/vj_botz"),
            InlineKeyboardButton("🕹 𝙎𝙐𝙋𝙋𝙊𝙍𝙏", url="https://t.me/vj_bot_disscussion")
        ]]
    )
    add_user(m.from_user.id)
    await m.reply_photo("https://graph.org/file/d57d6f83abb6b8d0efb02.jpg", caption="**🦊 Hello {}!\nI'm an auto approve [Admin Join Requests]({}) Bot.\nI can approve users in Groups/Channels.Add me to your chat and promote me to admin with add members permission.\n\n__Powered By : @VJ_Botz __**".format(m.from_user.mention, "https://t.me/telegram/153"), reply_markup=keyboard)
    

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ callback ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_callback_query(filters.regex("chk"))
async def chk(_, cb : CallbackQuery):
    try:
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
    except:
        await cb.answer("👀𝙋𝙡𝙚𝙖𝙨𝙚 𝙅𝙤𝙞𝙣 𝙈𝙮 𝙐𝙥𝙙𝙖𝙩𝙚 𝘾𝙝𝙖𝙣𝙣𝙚𝙡 𝙏𝙤 𝙐𝙨𝙚 𝙈𝙚.𝙄𝙛 𝙔𝙤𝙪 𝙅𝙤𝙞𝙣𝙚𝙙 𝙏𝙝𝙚 𝘾𝙝𝙖𝙣𝙣𝙚𝙡 𝙏𝙝𝙚𝙣 𝘾𝙡𝙞𝙘𝙠 𝙊𝙣 𝘾𝙝𝙚𝙘𝙠 𝘼𝙜𝙖𝙞𝙣 𝘽𝙪𝙩𝙩𝙤𝙣 𝙏𝙤 𝘾𝙤𝙣𝙛𝙞𝙧𝙢", show_alert=True)
        return 
    keyboard = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("📺 𝘾𝙃𝘼𝙉𝙉𝙀𝙇", url="https://t.me/vj_botz"),
            InlineKeyboardButton("🕹 𝙎𝙐𝙋𝙋𝙊𝙍𝙏", url="https://t.me/vj_bot_disscussion")
        ]]
    )
    add_user(m.from_user.id)
    await cb.edit_text(text="**🦊 Hello {}!\n🪄𝙄'𝙈 𝘼𝙉 𝘼𝙐𝙏𝙊 𝘼𝙋𝙋𝙍𝙊𝙑𝙀 [Admin Join Requests]({}) Bot.\nI can approve users in Groups/Channels.Add me to your chat and promote me to admin with add members permission.\n\n__Powered By : @VJ_Botz __**".format(cb.from_user.mention, "https://t.me/telegram/153"), reply_markup=keyboard)
    

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ info ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("users") & filters.user(cfg.SUDO))
async def dbtool(_, m : Message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await m.reply_text(text=f"""
🍀 Chats Stats 🍀
🙋‍♂️ Users : `{xx}`
👥 Groups : `{x}`
🚧 Total users & groups : `{tot}` """)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("bcast") & filters.user(cfg.SUDO))
async def bcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast Forward ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("fcast") & filters.user(cfg.SUDO))
async def fcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")

print("I'm Alive Now!")
app.run()
