from transformers import AutoTokenizer
import transformers
import torch
import time

model = "tiiuae/falcon-7b-instruct"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
)

start_time = time.time()


# inference here
sequences = pipeline(
   "he sentiment(positive/negative) of this sentence : This is a sunny day",
    max_length=200,
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
)
# end of inference

end_time = time.time()

elapsed_time = end_time - start_time
print(f"Inference took {elapsed_time} seconds.")

for seq in sequences:
    print(f"Result: {seq['generated_text']}")