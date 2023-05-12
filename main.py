# from hugchat import hugchat
from ast import literal_eval
# chatbot = hugchat.ChatBot()


import flan

model = flan.T5Model.from_pretrained("google/flan-t5-small")
tokenizer = flan.T5Tokenizer.from_pretrained("google/flan-t5-small")

prompt = "What is the capital of France?"
input_ids = tokenizer.encode(prompt, return_tensors="pt")
output_ids = model.generate(input_ids)


# user_request = input("Finish the sentence: Show me all countries ")
user_request = "that speak french"
chatbot_input = "Show me all countries " + user_request + ". Only write the answer in a python dictionary, using the categories (e.g. 'french speaking' )as keys and a list of the countries as values (e.g. ['France', 'Canada', 'Others'])."

# chatbot_output = chatbot.chat(chatbot_input)

try:
    flan_output = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    print(flan_output)
except Exception as e:    
    flan_output = None
    print(flan_output, e)


# try:
#     maybe_dict = chatbot_output[chatbot_output.index("{"):chatbot_output.index("}") + 1]
#     # literal_eval; watch out for security!
#     mydict = literal_eval(maybe_dict)
# except Exception as e:
#     output = chatbot.chat("Good answer. Now please only answer in a dictionary.")
#     print(output)

# # # New a conversation (ignore error)
# id = chatbot.new_conversation()
# chatbot.change_conversation(id)

# # Get conversation list
# conversation_list = chatbot.get_conversation_list()
# print(conversation_list, 'here')