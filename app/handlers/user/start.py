from aiogram import types
from aiogram.filters import CommandStart

from loader import _
from loader import router as dp

@dp.message(CommandStart())
async def _start_command(message: types.Message):
    text = _("👋, <a href='tg://user?id={}'>{}</a>")
    await message.answer(text.format(message.from_user.id, message.from_user.full_name))
