'''
Author: Garrick
LastEditTime: 2023-12-10 20:31:17
FilePath: /ecem202a_project_23fall/software/Hugging-face/llama_2_7b.py
zhuohaol@ucla.edu
Copyright (c) 2023 by Zhuohao Li, All Rights Reserved. 
'''
from transformers import AutoTokenizer
import transformers
import torch

model = "meta-llama/Llama-2-7b-chat-hf"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)

sequences = pipeline(
    'Who is the CEO of Tesla?\n',  # write prompt here
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    max_length=200,
)
for seq in sequences:
    print(f"Result: {seq['generated_text']}")
