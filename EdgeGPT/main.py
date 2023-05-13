import asyncio
from EdgeGPT import Chatbot, ConversationStyle
import tracemalloc

async def main():
    asyncio.create_task(other_func()) # run this when you find tasks to complete while waiting for API calls etc.
    bot = await Chatbot.create(cookie_path='EdgeGPT/cookies.json')
    # user_request = input("Finish the sentence: Show me all countries ")
    user_request = "that speak french"
    correct_example = "{
    'French Speaking Countries': ['Belgium', 'Benin', 'Burkina Faso', 'Burundi', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Comoros', 'Democratic Republic of the Congo', 'Djibouti', 'Equatorial Guinea', 'France', 'Gabon', 'Guinea', 'Haiti', 'Ivory Coast', 'Luxembourg', 'Madagascar', 'Mali', 'Monaco', 'Niger', 'Republic of the Congo', 'Rwanda', 'Senegal', 'Seychelles', 'Switzerland', 'Togo'],
    'Spanish Speaking Countries': ['Argentina','Bolivia','Chile','Colombia','Costa Rica','Cuba','Dominican Republic','Ecuador','El Salvador','Equatorial Guinea','Guatemala','Honduras','Mexico','Nicaragua','Panama','Paraguay','Peru','Puerto Rico','Spain','Uruguay','Venezuela']}"
    chatbot_input = "Show me all countries " + user_request + ". Only write the answer in a python dictionary, using the categories (e.g. 'french speaking' )as keys and a list of the countries as values (e.g. ['France', 'Canada', 'Others']). Here is an example of a correct dictionary for french and spanish speaking countries. " + correct_example
     response = await bot.ask(prompt=chatbot_input, conversation_style=ConversationStyle.creative)
    for message in response["item"]["messages"]:
        if message["author"] == "bot":
            bot_response = message["text"]
    await bot.close()

    print(bot_response)

async def other_func(): # function that can be run while main waits for API etc.
    return None

if __name__ == "__main__":
    asyncio.run(main())

