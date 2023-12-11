# Table of Contents

- Abstract
- [Introduction](#1-introduction)
- [Related Work](#2-related-work)
- [Technical Approach](#3-technical-approach)
- [Evaluation and Results](#4-evaluation-and-results)
- [Discussion and Conclusions](#5-discussion-and-conclusions)
- [References](#6-references)

# Abstract

Provide a brief overview of the project objhectives, approach, and results.

# 1. Introduction

### Motivation & Objective:

In an era where information is abundant, the ability to understand, process, and communicate in natural language is a valuable asset. Large Language Models (LLMs) are designed to bridge the gap between human communication and machine understanding. The primary goal is to create a tool that can interpret and generate human-like text, providing assistance, simplification, and augmentation of our daily informational and communicational tasks. Essentially, we are trying to teach machines the art of human conversation and written communication.

### State of the Art & Its Limitations:

Currently, Large Language Models are at the forefront of artificial intelligence research. Models like GPT (Generative Pre-trained Transformer) have shown capabilities in generating coherent and contextually relevant text based on the input they are given[^1]. However, they are not without their limitations. These models often require vast amounts of data to train[^2], can sometimes generate biased or incorrect information[^3],, and lack a deep understanding of the nuances and complexities inherent in human languages[^4].

### Novelty & Rationale:

Our research introduces a novel approach: deploying existing LLMs across a variety of devices to examine performance bottlenecks and system compatibilities. We selected several state-of-the-art LLM models which are extremely popular these days, both in research and industry. For example, Llamma-2[^5] from Meta AI, LoRA/QLoRA[^6]. Additionally, we plan to choose various deployment platforms ranging from cloud, personal edge devices, computing server, etc. This could help us to understand the capacity of LLMs in current computing platforms and areas.

### Potential Impact:

The successful development of an improved LLM has the potential to revolutionize numerous fields. From automating customer service to aiding in creative writing, the applications are vast. Technically, it would signify a leap towards more nuanced AI communication. Broadly, it could enhance education, accessibility, and information dissemination, breaking down language barriers and making knowledge more readily available.

### Challenges:

One of the greatest challenges is ensuring that the model can discern context and handle the subtleties of human language without perpetuating biases or misinformation. The complexity of language means that even small errors can significantly alter the meaning of the generated text. Additionally, the ethical use and potential misuse of LLMs pose a risk that must be carefully managed.

### Requirements for Success:

To undertake this project, a team with expertise in machine learning, natural language processing, and ethics in AI is essential. Access to large datasets, powerful computational resources, and a framework for ongoing evaluation against ethical standards are also necessary components for success.

### Metrics of Success:

Success will be measured by the model's ability to generate accurate, relevant, and unbiased text across a range of topics and styles. Performance metrics will include the quality and coherence of text, the ability to understand and generate responses to nuanced queries, and feedback from users on its reliability and usefulness. Additionally, adherence to ethical guidelines and the responsible use of the technology will be a crucial metric.

- Motivation & Objective: What are you trying to do and why? (plain English without jargon)
- State of the Art & Its Limitations: How is it done today, and what are the limits of current practice?
- Novelty & Rationale: What is new in your approach and why do you think it will be successful?
- Potential Impact: If the project is successful, what difference will it make, both technically and broadly?
- Challenges: What are the challenges and risks?
- Requirements for Success: What skills and resources are necessary to perform the project?
- Metrics of Success: What are metrics by which you would check for success?

# 2. Related Work

We did a following following survey and literature review about the current and past LLMs research. LLMs is a quite hot and recent research domain, and we found there're existing interesting work done before.

## Generative Pre-trained Transformers (GPTs)

The first well know LLM nowadays are absolutely GPT, or Generative Pre-trained Transformers developed by OpenAI. GPTs themself represent a series of evolutionary steps in the domain of natural language processing and machine learning. These models have set new benchmarks in the field of AI with their ability to understand and generate human-like text. Some GPT-based tools have already been widely used these days (eg. ChatGPT). During the developement progress of GPTs, we select several milestone during the way:

**GPT-2:**
GPT-2's architecture is a defining feature, utilizing a stacked transformer structure that includes multiple layers of transformer blocks. Each of these blocks incorporates multi-head self-attention mechanisms alongside fully connected neural network layers. The model, in its largest iteration, contains 1.5 billion parameters, which are meticulously fine-tuned during training to capture intricate language patterns. This extensive parameterization is crucial for the model’s ability to understand and generate complex language constructs.

A significant technical aspect of GPT-2 is its use of self-attention mechanisms within the transformers. These mechanisms enable the model to dynamically determine the relevance of each word in a sentence or sequence, adapting its understanding based on context. This flexibility is a step forward from previous models that relied on fixed positional encoding, offering a more nuanced understanding of language.

Furthermore, GPT-2 employs byte pair encoding (BPE) for tokenization, striking a balance between word-level and character-level tokenization. This approach is particularly effective in managing the model's vocabulary size and addressing the challenge of out-of-vocabulary words, which are common in natural language processing tasks.

**GPT-3:**
Introduced in June 2020, GPT-3 (the third generation of the GPT series) astounded the tech world with its 175 billion machine learning parameters[^1]. This vast network of parameters allows GPT-3 to engage in tasks such as translation, question-answering, and content creation with remarkable fluency and minimal task-specific training[^2]. Its critical technique lies in unsupervised learning from a diverse and extensive corpus of text which enables it to generate contextually rich and varied responses. Evaluation of GPT-3's capabilities has been predominantly qualitative, focusing on its linguistic versatility and the breadth of applications it can adapt to, though quantitative measures such as perplexity scores also showcase its efficiency[^2].

**GPT-3.5:**
GPT-3.5 serves as an intermediary iteration, an update to GPT-3, fine-tuned and optimized based on user feedback and ongoing research[^7]. It is not a full-fledged successor to GPT-3 but rather an enhancement that addresses some of the limitations found in GPT-3, particularly in consistency and factual accuracy. The critical technique employed remains largely the same, with improvements in fine-tuning processes and possibly the inclusion of more data to address gaps identified in GPT-3. Evaluations continue to focus on both qualitative and quantitative aspects, with increased attention to the model's ability to remain coherent over longer conversations and to better handle nuanced instructions.

**GPT-4:**
GPT-4[^8], as the successor to GPT-3, is anticipated to be a more advanced version that not only increases the parameter count but also introduces new techniques for training efficiency and output quality. While details are speculative until its release, it is expected that GPT-4 will make strides in addressing issues of bias, ethical use, and misinformation. The critical techniques might involve more sophisticated training algorithms, better contextual understanding, and refined interaction patterns. Evaluation will likely encompass a wide array of benchmarks including ethical alignment, multi-modal abilities (should it support more than text), and the efficiency of learning from fewer examples (few-shot learning).

Each of these models represents a leap forward in the capacity of machines to interact with human language, both in understanding and generation. The evolution from GPT-3 to GPT-4 illustrates a trajectory of AI becoming more integrated into daily tasks, emphasizing the need for rigorous evaluation and responsible deployment. The overarching aim of these models is to serve as a versatile and reliable interface between humans and computers, enhancing our ability to communicate with and through technology.

## Llamma-2

Meta has developed **Llama-2**, standing as a speculative successor to a hypothetical Llama-1 language model, would embody the next step in natural language processing and AI-driven linguistic tasks. This model, in the realm of machine learning, would likely aim to eclipse its predecessor in understanding and generating human-like text with higher precision and broader contextual awareness. Note that Llamma-2 is fully open-sourced thus it is very useful for academic research.

Meta has released Llamma-2 **small(7B)**, **medium(13B)**, and **large(70B)** models for public to use.

Assuming advancements along the lines of its contemporaries, Llama-2's critical technique would probably involve a combination of unsupervised and supervised learning, likely harnessing a transformer-based architecture renowned for its effectiveness in handling sequential data. The model would plausibly incorporate larger datasets, more refined parameter tuning, and potentially innovative approaches to reduce bias and improve the model's ability to grasp nuanced text. Advances in few-shot learning, where the model generates accurate responses with minimal input, could also be a focus, alongside multi-modal capabilities that integrate text with other data types like images or sounds.

## Fine-tuning LLMs

**LoRA**, which stands for Low-Rank Adaptation, is an innovative technique designed to enhance the capabilities of large pre-trained language models such as GPT-3. Developed with the intent to fine-tune these vast models more efficiently, LoRA focuses on the adaptability of neural networks without the need for significant architectural changes or the extensive computational cost typically associated with training large-scale AI models.

The critical technique behind LoRA lies in its novel approach to model tuning. Instead of updating the entire weight matrix within the transformer layers of a model, LoRA strategically targets specific parts of the weights for low-rank updates. By doing this, it can maintain the original model's performance while enabling new capabilities or knowledge to be added with minimal updates. This approach reduces the number of trainable parameters significantly, which in turn lowers the computational cost and resources required for fine-tuning.

LoRA's method allows the model to retain its original "knowledge" learned during pre-training while also acquiring new information during the fine-tuning process. This is particularly useful when adapting a model to a specialized domain or function without retraining it from scratch on large datasets.

Evaluating the effectiveness of LoRA involves assessing both the performance of the adapted model on targeted tasks and the efficiency gains it provides. Performance metrics would typically include standard benchmarks relevant to the specific tasks for which the model has been fine-tuned, such as accuracy, F1 score, or BLEU score for language translation tasks. Efficiency metrics would compare the computational resources and time required for fine-tuning with LoRA against traditional full-model fine-tuning techniques.

Furthermore, evaluation of LoRA also includes how well the adapted model can transfer its learning to other related tasks without additional training—this assesses the model's generalization capabilities. The ability to maintain baseline performance on tasks for which the model was not specifically fine-tuned is also a critical part of LoRA's evaluation.

In summary, LoRA represents a significant advancement in the fine-tuning of large-scale language models, providing a pathway to model customization that balances performance with resource efficiency.

# 3. Technical Approach

## Deployment Environment

Our goal is to analyze and evaluate the performance of large language models by comparing their deployment across various environments, including high-performance Mac M2, the Hugging Face platform, and Ubuntu servers equipped with NVIDIA A6000 GPUs. The detailed environment are as follow: - Local Environment on Mac M2 - Model Management platform Hugging Face - Ubuntu 20.04 with NVIDIA A6000 GPUs

We deployed our LLMs including original ones and fine-tuned families on there different environments ranging from embedded systems, edge devices, and cloud or server. The details are following like this:

- Edge devices/embedded system: M2 Chip on Mac

  - OS:
  - Hardware:

- Cloud: [Hugging Face](https://huggingface.co/)

  - runtime: Google Colab NVIDIA [A100](https://www.nvidia.com/en-us/data-center/a100/)/[V100](https://www.nvidia.com/en-us/data-center/v100/) GPU runtime

- GPU server:

  - OS: ubuntu 20.04.6 LTS
  - Hardware: 3 _ [NVIDIA RTX A6000 GPU](https://www.nvidia.com/en-us/design-visualization/rtx-a6000/) (48GB), 16 _ [Intel Xeon Gold 5222 CPU @ 3.80GHz](https://www.intel.com/content/www/us/en/products/sku/192445/intel-xeon-gold-5222-processor-16-5m-cache-3-80-ghz/specifications.html). (**We don't use distributed training across multiple servers**)

## Model Selection

We selected different large language models in our experiment, the model details are as follows:
| model | #Parameters | Training Data Raw Size | Training Data #Tokens | Training Data #Instances |
|---|---|---|---|---|
| Llama-2 7B| | | | |
| Llama-2 13B| | | | |
| | | | | |

## Task Definition

In evaluating the performance of large language models such as LLaMA-2, a comprehensive set of tasks and datasets is typically employed to assess both accuracy and inference latency. These tasks are designed to gauge the model's capabilities in various aspects of natural language processing. We carefully select the following tasks to measure the performance both in accuracy and latency of LLMs.

1. **Text Classification**
   Objective: To assess the model's ability to understand and categorize text.
   Typical Datasets: IMDb for movie reviews, SST-2 for sentiment analysis, and GLUE benchmark for general language understanding.
2. **Question Answering**
   Objective: To test the model's performance in providing accurate answers to specific questions.
   Typical Datasets: SQuAD (Stanford Question Answering Dataset), TriviaQA, and Natural Questions.
3. **Text Generation**
   Objective: To evaluate the model's capability in generating coherent, relevant, and creative text.
   Tasks: Story generation, dialogue creation, content summarization.
4. **Named Entity Recognition (NER)**
   Objective: To assess the model's proficiency in identifying named entities (such as names, places, organizations) in text.
   Typical Datasets: CoNLL-2003 NER and others.
5. **Natural Language Inference (NLI)**
   Objective: To evaluate the model's ability in inferring the relationship between text fragments (e.g., contradiction, entailment).
   Typical Datasets: SNLI (Stanford Natural Language Inference), MultiNLI.
6. **Translation**
   Objective: To test the model's ability in translating text from one language to another accurately.
   Typical Datasets: WMT (Workshop on Machine Translation), IWSLT.
7. **Inference Latency Measurement**
   Methodology: Inference latency is typically measured by repeatedly running model inferences on the same or similar tasks and recording the time taken for each run. The average latency and throughput (requests processed per second) are calculated.

# 4. Evaluation and Results

| model       | #Parameters | Training Data Raw Size | Training Data #Tokens | Training Data #Instances |
| ----------- | ----------- | ---------------------- | --------------------- | ------------------------ |
| Llama-2 7B  |             |                        |                       |                          |
| Llama-2 13B |             |                        |                       |                          |
|             |             |                        |                       |                          |

# 5. Discussion and Conclusions

# 6. References

[^1]: Brown T, Mann B, Ryder N, et al. Language models are few-shot learners[J]. Advances in neural information processing systems, 2020, 33: 1877-1901
[^2]: Kaplan J, McCandlish S, Henighan T, et al. Scaling laws for neural language models[J]. arXiv preprint arXiv:2001.08361, 2020.
[^3]: Bender E M, Gebru T, McMillan-Major A, et al. On the dangers of stochastic parrots: Can language models be too big?🦜[C]//Proceedings of the 2021 ACM conference on fairness, accountability, and transparency. 2021: 610-623.MLA
[^4]: Marcus G. The next decade in AI: four steps towards robust artificial intelligence[J]. arXiv preprint arXiv:2002.06177, 2020.MLA
[^5]: Llama 2. 2023.11. https://ai.meta.com/llama/
[^6]: Hu E J, Shen Y, Wallis P, et al. Lora: Low-rank adaptation of large language models[J]. arXiv preprint arXiv:2106.09685, 2021.MLA
[^7]: OpenAI. 2023. GPT3.5. https://openai.com/blog/gpt-3-5-turbo-fine-tuning-and-api-updates
[^8]: OpenAI. 2023. GPT4. https://openai.com/gpt-4
