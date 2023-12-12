import json
import random



import time
from typing import List, Optional

import fire

from llama import Llama, Dialog



if __name__=="__main__":
    all_data = json.load(open("/u/fr3ya/llama/data/sampled_sst2.json","r"))
    positive_data = [each for each in all_data if each['label']==1]

    negative_data = [each for each in all_data if each['label']==0]
    ckpt_dir ="/u/fr3ya/llama/llama-2-7b"
    tokenizer_path ="/u/fr3ya/llama/tokenizer.model"
    temperature = 0.6
    top_p = 0.9
    max_seq_len = 512
    max_batch_size = 8
    max_gen_len = None
    
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )
    positive_result = []
    st_time = time.time()
    for item in positive_data:
        tmp_dict = {}
        tmp_dict["sentence"] = item["sentence"]
        dialogs: List[Dialog] = [
            [{"role":"system", "content":"This is a sentiment analysis expert, I will perform sentiment analysis on the sentence you provided, I will output positive or negative or neutral, please input the sentence"},
            {"role": "user", "content":item["sentence"]}]
        ]
        results = generator.chat_completion(
            dialogs,  # type: ignore
            max_gen_len=max_gen_len,
            temperature=temperature,
            top_p=1,
        )
        tmp_dict['result'] = results[0]["generation"]["content"]
        print(tmp_dict['result'])
        positive_result.append(tmp_dict)
    end_time = time.time()
    print("Predict time %f for %d data:"%(end_time-st_time, len(positive_data)))
    negative_result = []
    st_time = time.time()
    for item in negative_data:
        tmp_dict = {}
        tmp_dict["sentence"] = item["sentence"]
        dialogs: List[Dialog] = [
            [{"role":"system", "content":"This is a sentiment analysis expert, I will perform sentiment analysis on the sentence you provided, I will output positive or negative or neutral, please input the sentence"},
            {"role": "user", "content":item["sentence"]}]
        ]
        results = generator.chat_completion(
            dialogs,  # type: ignore
            max_gen_len=max_gen_len,
            temperature=temperature,
            top_p=1,
        )

        tmp_dict['result'] = results[0]["generation"]["content"]
        negative_result.append(tmp_dict)
    end_time = time.time()
    print("Predict time %f for %d data:"%(end_time-st_time, len(negative_data)))
    with open("data/pos_res.json", "w") as f:
        json.dump(positive_result, f)
    with open("data/neg_res.json", "w") as f:
        json.dump(negative_result,f)
    