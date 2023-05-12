from transformers import T5Tokenizer, TFT5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained('t5-small')
model = TFT5ForConditionalGeneration.from_pretrained('t5-small')
inputs = tokenizer.encode("Hello, my dog is cute", return_tensors="tf")  # Batch size 1
outputs = model(inputs, decoder_input_ids=inputs)
prediction_scores = outputs[0]

tokenizer = T5Tokenizer.from_pretrained('t5-small')
model = TFT5ForConditionalGeneration.from_pretrained('t5-small')
inputs = tokenizer.encode("summarize: Hello, my dog is cute", return_tensors="tf")  # Batch size 1
result = model.generate(inputs)