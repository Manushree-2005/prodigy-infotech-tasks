from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pretrained GPT-2 model
model_name = "gpt2"

tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Input prompt
prompt = "Artificial Intelligence is changing the world because"

inputs = tokenizer.encode(prompt, return_tensors="pt")

# Generate text
output = model.generate(
    inputs,
    max_length=100,
    num_return_sequences=1,
    no_repeat_ngram_size=2,
    do_sample=True,
    temperature=0.7
)

# Decode output
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print("\nGenerated Text:\n")
print(generated_text)