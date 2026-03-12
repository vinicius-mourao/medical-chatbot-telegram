# Import necessary libraries and functions 
import os
from turtle import update
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from drug_query import search_drug, extract_drug_info

# Load environment variables
load_dotenv()
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message when the command /start is issued."""
    await update.message.reply_text("Welcome to the OpenFDA Drug Query Bot! Please enter a drug name to get information.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a help message when the command /help is issued."""
    await update.message.reply_text("How to use this bot:\n" 
                                    "Simply enter the name of a drug and I will provide you with detailed information about it.\n"
                                    "- Commands: /start (welcome), /help (this message).\n"
                                    "Note: Information is for educational purposes only.")
    
async def query_drug(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle drug queries."""
    drug_name = update.message.text.strip().lower().replace(" ", "+")
    if not drug_name:
        await update.message.reply_text("Please enter a valid drug name.")
        return
    try:
        # Search for the drug using the OpenFDA API
        search_result = search_drug(drug_name)
        if not search_result:
            await update.message.reply_text("Sorry, I couldn't find any information on that drug.")
            return
        
        # Extract and format the drug information
        info = extract_drug_info(search_result)
        if not info:
            await update.message.reply_text("Sorry, I couldn't extract information for that drug.")
            return
        
        # Format and reply
        formatted_message = format_message(info)
        max_length = 4000  # Leave buffer
        if len(formatted_message) > max_length:
            parts = [formatted_message[i:i+max_length] for i in range(0, len(formatted_message), max_length)]
            for part in parts:
                await update.message.reply_text(part, parse_mode='HTML')
        else:
            await update.message.reply_text(formatted_message, parse_mode='HTML')
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")

def format_message(info: dict) -> str:
    """Format the drug information dictionary into a readable string."""
    if not info:
        return "No information available."
    
    message = ""
    for key, value in info.items():
        if value: # Only include fields that have information
            # Escape HTML characters in value
            value = str(value).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            readable_key = key.replace('_', ' ').title()
            message += f"<u><b>{readable_key}:</b></u> {value}\n"
    return message.strip()

def main() -> None:
    """Start the bot."""
    if not TOKEN:
        print("Error: TELEGRAM_BOT_TOKEN is not set in the environment variables.")
        return
    
    # Create the Application
    application = Application.builder().token(TOKEN).build()

    # Add handlers for commands and messages
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, query_drug))

    # Run the bot
    application.run_polling()

if __name__ == '__main__':
    main()