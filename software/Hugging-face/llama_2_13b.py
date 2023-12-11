'''
Author: Garrick
LastEditTime: 2023-12-10 20:38:16
FilePath: /ecem202a_project_23fall/software/Hugging-face/llama_2_13b.py
zhuohaol@ucla.edu
Copyright (c) 2023 by Zhuohao Li, All Rights Reserved. 
'''
from transformers import AutoTokenizer, pipeline
import transformers
import torch
import time

model = "meta-llama/Llama-2-13b-chat-hf"

tokenizer = AutoTokenizer.from_pretrained(model)
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,  # 添加分词器
    torch_dtype=torch.float16,
    device=0 if torch.cuda.is_available() else -1,  # 确保使用GPU（如果可用）
)

# 开始计时
start_time = time.time()

# 进行模型推理
sequences = pipe(
    'Who created Apple inc?\n',
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    max_length=400,
)

# 结束计时
end_time = time.time()

# 计算运行时间
elapsed_time = end_time - start_time
print(f"Inference took {elapsed_time} seconds.")

# 打印结果
for seq in sequences:
    print(f"Result: {seq['generated_text']}")