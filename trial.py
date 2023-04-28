from ast import literal_eval
chatbot_output = " random shit {'red': ['one', 'two'], 'blue': ['four', 'five']} more rndom shit "

maybe_dict = chatbot_output[chatbot_output.index("{"):chatbot_output.index("}") + 1]
mydict = literal_eval(maybe_dict)
