<!--
 * @Author: Garrick
 * @LastEditTime: 2023-12-10 13:04:42
 * @FilePath: /ecem202a_project_23fall/software/README.md
 * zhuohaol@ucla.edu
 * Copyright (c) 2023 by Zhuohao Li, All Rights Reserved.
-->

# Quantifying LLMs Accuracy and Latency

In this folder, we open-sourced our code for quantifying LLMs accuracy and latency. We deployed current and recent popular large models in different environments.

### How the file goes

The code files in this manner:

1. `Hugging-face` includes the deployment setups for LLMs runs on popular [Hugging Face](https://huggingface.co/).
2. `Mac` includes the deployment setups for LLMs runs on personal edge executors.
3. `Server` includes the deployment setups for LLMs runs on GPU server which is supported by advanced multi-GPUs.

We will discuss each environment respectively.

### Hugging face

[Hugging Face](https://huggingface.co/) is a prominent company in the artificial intelligence field, particularly known for its work in natural language processing (NLP). Here are the key aspects of Hugging Face and its impact on Large Language Models (LLMs) like GPT-3:

- **Transformers Library**: Hugging Face is best known for its 'Transformers' library, which provides thousands of pre-trained models to perform tasks on texts such as classification, information extraction, question answering, summarization, translation, and text generation. This library is widely used in the AI community for its versatility and ease of use.

- **Model Hub**: They host a model hub, where the AI community can upload and share models. This has become a valuable resource for researchers and practitioners looking for specific models tailored to various tasks.

- **Community and Collaboration**: Hugging Face emphasizes community engagement and open-source collaboration, making it easier for researchers, developers, and companies to advance in NLP.

Hugging Face is widely used by the following features:

- **Accessibility**: The Transformers library democratizes access to state-of-the-art NLP models, allowing both academics and industry professionals to leverage advanced models without the need for extensive computational resources.

- **Ease of Use**: The library is designed to be user-friendly, with a high-level interface for various NLP tasks, simplifying the process of applying AI in practical applications.

### MacOS

### GPU server

Our server is supported by
