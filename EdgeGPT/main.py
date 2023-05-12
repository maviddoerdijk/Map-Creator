import asyncio
from EdgeGPT import Chatbot, ConversationStyle

import os

# print(os.getcwd())


bot = Chatbot(cookie_path='\EdgeGPT\cookies.json')
print(bot.ask(prompt="Hello there", conversation_style=ConversationStyle.creative))