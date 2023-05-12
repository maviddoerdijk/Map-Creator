
def flan_t5-small():
    from transformers import pipeline

    nlp = pipeline("text2text-generation", model="google/flan-t5-small") # you can use 5 different sizes: small, base, large, xl and xxl
    nlp("Question: How many cities does France have with more than 1 million inhabitants?")
    return