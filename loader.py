from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram import Router
from aiogram.utils.i18n import I18n

from data.config import TG_TOKEN
# from app.middlewares.i18n import i18n_middleware

storage = MemoryStorage()
bot = Bot(
    TG_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)
dp = Dispatcher(bot=bot, storage=storage)

router = Router()
from data.config import LOCALES_DIR, I18N_DOMAIN
i18n = I18n(path=LOCALES_DIR, domain=I18N_DOMAIN)
_ = i18n.gettext

