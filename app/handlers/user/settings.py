from aiogram.types import Message
from aiogram.filters import Command

from loader import _
from loader import router as dp


@dp.message(Command("Settings ⚙️"))
async def _settings_command(message: Message) -> None:
    await message.answer(
        text=_("You settings ⚙️"),
    )
