import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "👋 Привет!\n\n"
        "Это анонимный бот.\n"
        "Отправь сюда сообщение, фото, видео, голосовое или файл — "
        "и оно будет передано получателю анонимно.\n\n"
        "Команды:\n"
        "/start — начать"
    )


@dp.message()
async def anonymous_message(message: types.Message):
    # Пока отправляем владельцу бота
    owner_id = 123456789  # заменить на свой Telegram ID

    try:
        await bot.copy_message(
            chat_id=owner_id,
            from_chat_id=message.chat.id,
            message_id=message.message_id
        )

        await message.answer(
            "✅ Сообщение отправлено анонимно!"
        )

    except Exception:
        await message.answer(
            "❌ Ошибка отправки сообщения."
        )


async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
