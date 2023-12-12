import json
import random

all_data = json.load(open("/u/fr3ya/llama/data/sampled_sst2.json","r"))
positive_data = [each for each in all_data if each['label']==1][:8]

negative_data = [each for each in all_data if each['label']==0][:8]
import time
from typing import List, Optional

import fire

from llama import Llama, Dialog

def get_batch_data(
    data_to_predict: list,
    ckpt_dir: str="/u/fr3ya/llama/llama-2-7b",
    tokenizer_path: str="/u/fr3ya/llama/tokenizer.model",
    temperature: float = 0.6,
    top_p: float = 0.9,
    max_seq_len: int = 512,
    max_batch_size: int = 8,
    max_gen_len: Optional[int] = None,
    
):

    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )
    list_to_chat = []
    for item in data_to_predict:
        tmp_list = []
        system_dict,user_dict = {},{}
        system_dict['role'] = "system"
        system_dict['content'] = "This is a sentiment analysis expert, I will perform sentiment analysis on the sentence you provided, I will output positive or negative, please input the sentence"
        user_dict['role'] = "user"
        user_dict["content"] = item["sentence"]
        tmp_list.append(system_dict)
        tmp_list.append(user_dict)
        list_to_chat.append(tmp_list)

    dialogs: List[Dialog] = list_to_chat
    # dialogs: List[Dialog] = [
    #     [
    #         {"role": "system", "content": "This is a sentiment analysis expert, I will perform sentiment analysis on the sentence you provided, I will output positive or negative or neutral, please input the sentence"},
    #         {"role": "user", "content": "the entire point of a shaggy dog story , of course , is that it goes nowhere , and this is classic nowheresville in every sense . "}
    #     ]
        
    # ]
    # print(dialogs)
    st_time = time.time()
    results = generator.chat_completion(
        dialogs,  # type: ignore
        max_gen_len=max_gen_len,
        temperature=temperature,
        top_p=top_p,
    )
    end_time = time.time()
    print("Predict time for %d data: "%len(data_to_predict), end_time-st_time)
    result_dict_list = []
    for dialog, result in zip(dialogs, results):
        tmp_dict = {}
        for msg in dialog:
            if msg['role'] == 'user':
                tmp_dict['sentence'] = msg['content']
            # print(f"{msg['role'].capitalize()}: {msg['content']}\n")
            if result['generation']['role'] == 'assistant':
                tmp_dict['result'] = result['generation']['content']
        # print(
        #     f"> {result['generation']['role'].capitalize()}: {result['generation']['content']}"
        # )
        result_dict_list.append(tmp_dict)
        print("\n==================================\n")
    return result_dict_list


if __name__=="__main__":
    positive_batch_result = get_batch_data(positive_data)
    negative_batch_result = get_batch_data(negative_data)
    with open("data/pos_res.json", "w") as f:
        json.dump(positive_batch_result, f)
    with open("data/neg_res.json", "w") as f:
        json.dump(negative_batch_result,f)
    # main()