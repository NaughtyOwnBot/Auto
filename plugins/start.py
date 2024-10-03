#(©) Codeflix_Bots

import os
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated

from bot import Bot
from config import *
from helper_func import subscribed, encode, decode, get_messages
from database.database import add_user, del_user, full_userbase, present_user


"""add time im seconds for waitingwaiting before delete 
1min=60, 2min=60×2=120, 5min=60×5=300"""
SECONDS = int(os.getenv("SECONDS", "60"))

