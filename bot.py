import logging
import os
import time
import telegram
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Define the start command handler
def start(update, context):
    user = update.message.from_user
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hello {user.first_name}! Welcome to our movie bot. To get started, please join our Telegram group below:")
    context.bot.send_message(chat_id=update.effective_chat.id, text="https://t.me/your_group_link", reply_markup=telegram.InlineKeyboardMarkup([[
        telegram.InlineKeyboardButton(text="Join Group", url="https://t.me/your_group_link"),
        telegram.InlineKeyboardButton(text="Subscription", callback_data="subscription"),
    ]]))

# Define the subscription command handler
def subscription(update, context):
    query = update.callback_query
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Please select a subscription plan below:")
    buttons = [[telegram.InlineKeyboardButton(text=f"{plan['name']} ({plan['price']} {os.getenv('PAYMENT_CURRENCY')})", callback_data=f"{plan['_id']}_{plan['price']}")] for plan in get_plans()]
    context.bot.send_message(chat_id=query.message.chat_id, text="Subscription Plans:", reply_markup=telegram.InlineKeyboardMarkup(buttons))

# Define the callback query handler
def callback_query_handler(update, context):
    query = update.callback_query
    query.answer()
    plan_id, price = query.data.split("_")
    invoice_payload = f"{update.effective_user.id}_{plan_id}"
    context.bot.send_invoice(chat_id=query.message.chat_id,
                             title='Subscription',
                             description=f'Subscription for {get_plan_by_id(plan_id)["name"]}',
                             payload=invoice_payload,
                             provider_token=os.getenv('PAYMENT_TOKEN'),
                             start_parameter='subscription',
                             currency=os.getenv('PAYMENT_CURRENCY'),
                             prices=[telegram.LabeledPrice(label='Subscription', amount=int(price)*100)],
                             need_name=True,
                             need_phone_number=True,
                             need_email=True,
                             is_flexible=False)
    
# Define the invoice handler
def precheckout_callback(update, context):
    query = update.pre_checkout_query
    query.answer(ok=True)
    
# Define the successful payment handler
def successful_payment(update, context):
    user_id = update.message.from_user.id
    chat_id = update.message.chat_id
    message_id = update.message.message_id
    plan_id = update.message.successful_payment.invoice_payload.split("_")[1]
    expiry = int(time.time()) + get_plan_by_id(plan_id)['duration'] * 86400
    context.bot.send_message(chat_id=chat_id, text=f"Thank you for subscribing to {get_plan_by_id(plan_id)['name']}! Your subscription will expire on {time.ctime(expiry)}.")
    context.bot.send_message(chat_id=user_id, text=f"Thank you for subscribing to {get_plan_by_id(plan_id)['name']}! Please
