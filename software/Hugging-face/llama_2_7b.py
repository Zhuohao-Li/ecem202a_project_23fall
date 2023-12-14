

from transformers import AutoTokenizer
import transformers
import torch
import time

model = "meta-llama/Llama-2-7b-chat-hf"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)

start_time = time.time()


# start of inference
sequences = pipeline(
    'Solve -179*q = -190*q - 22 for q. Solve -118525*z = -118565*z + 2720 for z.\n',
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    max_length=200,
)
# end of inference

end_time = time.time()

# 计算运行时间
elapsed_time = end_time - start_time
print(f"Inference took {elapsed_time} seconds.")


for seq in sequences:
    print(f"Result: {seq['generated_text']}")
