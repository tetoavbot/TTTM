import asyncio
from pyrogram import Client,filters,enums

api_id = input('25024408')
api_hash = input('4b1f6d4688cb616f0c845dd16018c004')
sessionstring = input('BAC0AQAG3UoB73x41w-PHP1Fxv6LPCmKL6ILjkUwEU0m7ZxXUL3YpmcLs3yFfn5WRgbsgAw5Wj_zR4Ccfs7robo1x6vic91Y1wOLFp_JgZ5pwvPAWg6Yxy3JDxsqhJ0Rb5JnI_mU3a1_VjkD17g9zBbP9NGxINg81KIs8PltApTPn4DrUsX3o97jzl62m_-K_N2DtxNuoB2nx8VcX89Q3lI9rLQ31KqysfH7JqI-JPpWcK8q9kc_Yp4k8AMxg4IPQe3hIQy10_YyL1A-vsASQsvC277_Kf1wiHCo-MaMoFCKfURr597igeCjoF_ZxCPEKXoFJClnU-H5iVvDHm2QKPaAAAAAYFQu84A')
app = Client("acc", session_string = sessionstring, api_id = api_id, api_hash = api_hash)

@app.on_message(filters.command("حظر الكل","") & filters.me)
async def num(client, message):
  i = 1
  xx = 0
  async for x in app.get_chat_members(message.chat.id):
    try :
      await app.ban_chat_member(message.chat.id,x.user.id)
      if i%10 == 0 :
          await message.edit(f"• تم حظر {i}")
      i += 1
    except :
      xx +=1
      await message.edit(f"• العضو {x.user.id} لم استطيع حظره")
  await message.edit(f"• تم حظر {i} عضو \n• لم استطيع حظر {xx} عضو")

@app.on_message(filters.command("مسح المحظورين","")& filters.me)
async def bn(client ,message):
  xxx = 0
  await message.edit("• جاري الغاء الحظر ...")
  async for m in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.BANNED):
    try :
      await app.unban_chat_member(message.chat.id , m.user.id)
      xxx += 1
    except :
      print("error")
  await message.edit(f"تم الغاء حظر {xxx} عضو")


app.run()