import asyncio
import logging
import sys
from os import getenv
import wikipedia

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message


wikipedia.set_lang("uz")

TOKEN = ("7074918762:AAEs_vVn9zsvhpEEZYrAR1eB3N5Unqgg240")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Salom, {html.bold(message.from_user.full_name)}!\n"
                         f"Siz menga istagan so'zni yuboring, men sizga wikipediadan shu so'zga aloqador maqolani topib beraman 🫡")


@dp.message()
async def wiki_searcher(message: Message) -> None:
    try:
        respons = wikipedia.summary(message.text)
        await message.answer(respons)
    except:
        await message.answer("Bu so'z bilan aloqador malumot topilmadi 🧐")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())