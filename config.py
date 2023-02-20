import os

# Telegram Bot API token
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

# Payment provider token and credentials
PAYMENT_PROVIDER_TOKEN = os.environ.get("PAYMENT_PROVIDER_TOKEN")
PAYMENT_PROVIDER_NAME = os.environ.get("PAYMENT_PROVIDER_NAME")
PAYMENT_PROVIDER_URL = os.environ.get("PAYMENT_PROVIDER_URL")
PAYMENT_PROVIDER_CERT_PATH = os.environ.get("PAYMENT_PROVIDER_CERT_PATH")

# Subscription plans and their respective prices
PLANS = {
    "1": {"name": "15 Days", "price": 35},
    "2": {"name": "1 Month", "price": 59},
    "3": {"name": "6 Months", "price": 199},
    "4": {"name": "1 Year", "price": 99},
}

# Bot owner and admin user IDs
BOT_OWNER = os.environ.get("BOT_OWNER")
BOT_ADMINS = os.environ.get("BOT_ADMINS")

# Google Sheets API credentials
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
GOOGLE_API_SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
GOOGLE_SHEET_ID = os.environ.get("GOOGLE_SHEET_ID")
GOOGLE_SHEET_RANGE = os.environ.get("GOOGLE_SHEET_RANGE")

# Telegraph API token
TELEGRAPH_API_TOKEN = os.environ.get("TELEGRAPH_API_TOKEN")
