import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile

BOT_TOKEN = "7527692969:AAEeynFXlcLQsbw32fb8srS34YNBGJMc27s"

PHOTO_PATH = "muzik.jpg"
COMMENT_TEXT = (
    "<b>🎶 СДЕЛАТЬ ПОСТ О СЕБЕ или ВЫЛОЖИТЬ РЕЛИЗ:</b> @newdistribution\n\n"
    "<b>🗣 Голоса:</b> https://t.me/boost/newmuzziik\n\n"
    "<b>Все наши каналы:</b> @muzikbl0g\n\n"
    "<b>— Пиши комментарий и становись легендой музыки!</b>"
)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

processed_media_groups = set()

@dp.message(F.forward_from_chat, F.forward_from_chat.type == "channel")
async def comment_under_post(message: Message):

    # если альбом — отвечаем только 1 раз
    if message.media_group_id:
        if message.media_group_id in processed_media_groups:
            return
        processed_media_groups.add(message.media_group_id)

    photo = FSInputFile(PHOTO_PATH)

    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=COMMENT_TEXT,
        parse_mode="HTML",
        reply_to_message_id=message.message_id
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
