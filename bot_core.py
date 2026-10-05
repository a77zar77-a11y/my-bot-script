import telebot
from datetime import datetime

# Users aur unki Access Expiry Date (Format: "YYYY-MM-DD HH:MM:SS")
ALLOWED_USERS = {
    1234567890: "2026-10-10 18:00:00",  # Example ID: Expiry Date & Time
    9876543210: "2026-10-07 12:00:00",  # Another ID
}

BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"
bot = telebot.TeleBot(BOT_TOKEN)

def is_access_valid(user_id):
    if user_id not in ALLOWED_USERS:
        return False, "❌ Access Denied! Aap registered nahi hain."

    # Current time aur Expiry time calculate karna
    expiry_str = ALLOWED_USERS[user_id]
    expiry_time = datetime.strptime(expiry_str, "%Y-%m-%d %H:%M:%S")
    current_time = datetime.now()

    if current_time > expiry_time:
        return False, f"⏰ Aapka access expire ho chuka hai!\nExpiry Time tha: {expiry_str}"
    
    return True, "Access Valid"

@bot.message_handler(commands=['start'])
def start_command(message):
    user_id = message.chat.id
    has_access, msg = is_access_valid(user_id)
    
    if not has_access:
        bot.reply_to(message, msg)
        print(f"Access Failed for ID {user_id}: {msg}")
        return

    bot.reply_to(message, f"✅ Welcome! Aapka access active hai.\nBot successfully running!")

if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
  
