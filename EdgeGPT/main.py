import asyncio
from EdgeGPT import Chatbot, ConversationStyle
import pygal
from ast import literal_eval


async def main():
    asyncio.create_task(other_func()) # run this when you find tasks to complete while waiting for API calls etc.
    bot = await Chatbot.create(cookie_path='EdgeGPT/cookies.json')
    # user_request = input("Finish the sentence: Show me all countries ")
    user_request = "that are the top 10 in absolute exporting of oil"
    correct_example = """[
    ['French Speaking Countries', ['Belgium', 'Benin', 'Burkina Faso', 'Burundi', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Comoros', 'Democratic Republic of the Congo', 'Djibouti', 'Equatorial Guinea', 'France', 'Gabon', 'Guinea', 'Haiti', 'Ivory Coast', 'Luxembourg', 'Madagascar', 'Mali', 'Monaco', 'Niger', 'Republic of the Congo', 'Rwanda', 'Senegal', 'Seychelles', 'Switzerland', 'Togo']]
    ,['Spanish Speaking Countries', ['Argentina','Bolivia','Chile','Colombia','Costa Rica','Cuba','Dominican Republic','Ecuador','El Salvador','Equatorial Guinea','Guatemala','Honduras','Mexico','Nicaragua','Panama','Paraguay','Peru','Puerto Rico','Spain','Uruguay','Venezuela']]]"""
    chatbot_input = "Show me all countries " + user_request + ". Only write the answer in a python list. This list should be a list of smaller lists. These smaller lists contain a descriptive string and a list of countries with a string coming first, that describes the list that comes later.  using the categories (e.g. 'french speaking') as strings and a list of the countries (e.g. ['France', 'Canada', 'Others']). Here is an example of a correct dictionary for french and spanish speaking countries. " + correct_example
    response = await bot.ask(prompt=chatbot_input, conversation_style=ConversationStyle.creative)
    for message in response["item"]["messages"]:
        if message["author"] == "bot":
            bot_response = message["text"]
    await bot.close()


    try:
        maybe_list = bot_response[bot_response.index('```python') + 9:bot_response.rindex(']') + 1]
        # literal_eval; watch out for security!
        print(maybe_list, 'trial1')
        rq = literal_eval(maybe_list)
        create_map(rq)

    except Exception as e:
        #TODO: add recall function here that tries again to get a better response from bing
        print("Error here", e)



async def other_func(): # function that can be run while main waits for API etc.
    return None

def create_map(requirements: dict):
    
    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = 'Title'

    for to_add in requirements:
        #transform country names into abbreviations (Belgium -> be)
        worldmap_chart.add(to_add[0],to_add[1] )
    # worldmap_chart.render()
    worldmap_chart.render_to_file('map.svg')

if __name__ == "__main__":
    asyncio.run(main())

