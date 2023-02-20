import os

# Telegram Bot Authorization Token
TOKEN = os.environ.get('TOKEN', 'your_token_here')

# Payment Token for Stripe Integration
PAYMENT_TOKEN = os.environ.get('PAYMENT_TOKEN', 'your_payment_token_here')

# Payment Provider Name
PAYMENT_PROVIDER = os.environ.get('PAYMENT_PROVIDER', 'Stripe')

# Payment Currency
PAYMENT_CURRENCY = os.environ.get('PAYMENT_CURRENCY', 'USD')

# Plan Definitions
PLANS = {
    "1": {"name": "15 Days", "price": 35, "duration": 15},
    "2": {"name": "1 Month", "price": 59, "duration": 30},
    "3": {"name": "6 Months", "price": 199, "duration": 180},
    "4": {"name": "1 Year", "price": 99, "duration": 365},
}

# Logging Configuration
LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')

# Bot owner and admin user IDs
BOT_OWNER = os.environ.get('BOT_OWNER', 'your_bot_owner_id_here')
BOT_ADMINS = os.environ.get('BOT_ADMINS', 'your_bot_admins_ids_here').split(',')
