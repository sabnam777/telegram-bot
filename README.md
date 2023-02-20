# Telegram Premium Subscription Bot
This is a Telegram bot that allows users to subscribe to premium content and services. The bot offers different subscription plans, which can be paid for using popular payment systems such as PhonePe, Google Pay, BHIM UPI, and Paytm.

**Table of Contents**
- Features
- Installation
- Usage
- Commands
- Contributing
- License

**Features**
- Users can subscribe to premium content and services using different subscription plans.
- The bot accepts payments via PhonePe, Google Pay, BHIM UPI, and Paytm.
- The bot automatically kicks users out of the premium group when their subscription ends.
- Five days before the subscription ends, the bot notifies users to renew their subscription.
- The bot has a broadcast feature that allows the bot owner to send messages to all users.
- The bot owner and admins can ban users, and the banned user receives a notification message and a button to contact the admin.
- The bot owner and admins can access the bot's logs and status.
- The bot has a restart command that allows the owner to restart the bot.

**Installation**
To use this bot, you need to do the following:

- Clone the repository: git clone https://github.com/your-username/telegram-premium-subscription-bot.git
- Install the requirements: pip install -r requirements.txt
- Create a bot using BotFather and get the API token.
- Copy the API token and add it to the config.py file.
- Run the bot: python main.py

**Usage**
Once the bot is running, users can start using it by sending the /start command. The bot will greet them and provide a button to join the Telegram group. Users can then access the subscription plans page by clicking on the "Upgrade" button. From there, they can choose a subscription plan, select a payment option, and complete the payment process.

**Commands**
The following commands are available for the users:

/start: Start using the bot.
/upgrade: Go to the subscription plans page.
/help: Get information on how to use the bot.
The following commands are available for the bot owner and admins:

/broadcast: Send a message to all users.
/status: Get information about the bot's status.
/restart: Restart the bot.
/history: Get the subscription history of all users.
/logs: Get the bot's logs.
Contributing
Contributions are welcome! If you have any ideas, suggestions, or bug reports, please create an issue or submit a pull request.

<h3 align="center">
    ─「 ᴅᴇᴩʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ 」─
</h3>

<p align="center"><a href="https://dashboard.heroku.com/new?template=https://github.com/sabnam777/telegram-bot"> <img src="https://img.shields.io/badge/Deploy%20On%20Heroku-black?style=for-the-badge&logo=heroku" width="220" height="38.45"/></a></p>

<h3 align="center">

**License**
This project is licensed under the MIT License.
