from aiogram.types import Message
from aiogram.filters import Command

from loader import _
from loader import router as dp


@dp.message(Command("Help 🆘"))
@dp.message(Command("help"))
async def _help_command(message: Message) -> None:
    await message.answer(
        text=_("Help 🆘"),
    )
