from transformers import TFT5ForConditionalGeneration, T5Tokenizer
from tensorflow.keras.initializers import RandomNormal

model = TFT5ForConditionalGeneration.from_pretrained("google/flan-t5-small")
tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-small")

input_text = "Question: How many cities does France have with more than 1 million inhabitants?"
input_ids = tokenizer.encode(input_text, return_tensors="tf")

initializer = RandomNormal(seed=42)
model.init_weights(initializer)

outputs = model.generate(input_ids, max_new_tokens=10)
decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(decoded_output)