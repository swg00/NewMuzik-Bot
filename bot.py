import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

BOT_TOKEN = "7527692969:AAEeynFXlcLQsbw32fb8srS34YNBGJMc27s"

PHOTO_PATH = "promo.jpg"
COMMENT_TEXT = (
    "<b>🎶 СДЕЛАТЬ ПОСТ О СЕБЕ или ВЫЛОЖИТЬ РЕЛИЗ:</b> @newdistribution\n"
    "<b>🗣 Голоса:</b> https://t.me/boost/newmuzziik\n\n"
    "<b>Пиши комментарий и становись легендой музыки!</b>"
)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(
    F.forward_from_chat,
    F.forward_from_chat.type == "channel"
)
async def comment_under_post(message: Message):
    await message.reply(COMMENT_TEXT, parse_mode="HTML")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
