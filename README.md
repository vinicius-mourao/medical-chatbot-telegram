# Medical Chatbot Telegram

A Telegram bot that queries the [OpenFDA API](https://open.fda.gov/) to provide detailed drug label information directly in your Telegram chat.

## Features

- Search for any drug by brand name
- Returns comprehensive drug information including warnings, dosage, adverse reactions, and more
- Handles long responses by splitting them into multiple messages
- Built on top of the [OpenFDA Drug Query](https://github.com/vinicius-mourao/openfda-drug-query) project

## Information Provided

- Brand name and generic name
- Manufacturer
- Route of administration
- Purpose and indications for use
- Warnings and adverse reactions
- Dosage and administration
- Storage and handling
- Inactive ingredients
- And more

## Commands

- `/start` — Welcome message
- `/help` — Usage instructions
- Any text — Search for a drug by brand name

## Requirements
```
python-telegram-bot
python-dotenv
requests
```

## Setup

1. Clone the repository
2. Install dependencies:
```bash
pip install python-telegram-bot python-dotenv requests
```
3. Create a `.env` file in the root directory:
```
TELEGRAM_BOT_TOKEN=your_token_here
```
4. Get your bot token from [@BotFather](https://t.me/botfather) on Telegram
5. Run the bot:
```bash
python medical_chatbot.py
```

## Usage

Open your bot on Telegram and type a drug name, for example:
- `aspirin`
- `ibuprofen`
- `lisinopril`

## Data Source

Drug information is retrieved from the [FDA Drug Label API](https://open.fda.gov/apis/drug/label/).

## Disclaimer

This bot is for educational purposes only. Always consult a healthcare professional before making any medical decisions.

## Author

Vinícius Mourão Mendes Costa