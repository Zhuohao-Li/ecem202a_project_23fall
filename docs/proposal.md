# Project Proposal

## 1. Motivation & Objective

In an era where information is abundant, the ability to understand, process, and communicate in natural language is a valuable asset. Large Language Models (LLMs) are designed to bridge the gap between human communication and machine understanding. The primary goal is to create a tool that can interpret and generate human-like text, providing assistance, simplification, and augmentation of our daily informational and communicational tasks. Essentially, we are trying to teach machines the art of human conversation and written communication.

## 2. State of the Art & Its Limitations

Currently, Large Language Models are at the forefront of artificial intelligence research. Models like GPT (Generative Pre-trained Transformer) have shown capabilities in generating coherent and contextually relevant text based on the input they are given[^1]. However, they are not without their limitations. These models often require vast amounts of data to train[^2], can sometimes generate biased or incorrect information[^3],, and lack a deep understanding of the nuances and complexities inherent in human languages[^4].

## 3. Novelty & Rationale

Our research introduces a novel approach: deploying existing LLMs across a variety of devices to examine performance bottlenecks and system compatibilities. We selected several state-of-the-art LLM models which are extremely popular these days, both in research and industry. For example, Llamma-2[^5] from Meta AI, LoRA/QLoRA[^6]. Additionally, we plan to choose various deployment platforms ranging from cloud, personal edge devices, computing server, etc. This could help us to understand the capacity of LLMs in current computing platforms and areas.

## 4. Potential Impact

The successful development of an improved LLM has the potential to revolutionize numerous fields. From automating customer service to aiding in creative writing, the applications are vast. Technically, it would signify a leap towards more nuanced AI communication. Broadly, it could enhance education, accessibility, and information dissemination, breaking down language barriers and making knowledge more readily available.

## 5. Challenges

One of the greatest challenges is ensuring that the model can discern context and handle the subtleties of human language without perpetuating biases or misinformation. The complexity of language means that even small errors can significantly alter the meaning of the generated text. Additionally, the ethical use and potential misuse of LLMs pose a risk that must be carefully managed.

## 6. Requirements for Success

To undertake this project, a team with expertise in machine learning, natural language processing, and ethics in AI is essential. Access to large datasets, powerful computational resources, and a framework for ongoing evaluation against ethical standards are also necessary components for success.

## 7. Metrics of Success

Success will be measured by the model's ability to generate accurate, relevant, and unbiased text across a range of topics and styles. Performance metrics will include the quality and coherence of text, the ability to understand and generate responses to nuanced queries, and feedback from users on its reliability and usefulness. Additionally, adherence to ethical guidelines and the responsible use of the technology will be a crucial metric.

## 8. Execution Plan

<!-- Describe the key tasks in executing your project, and in case of team project describe how will you partition the tasks. -->
### 8.1 Key tasks
    1. Data collection and preparation: prepare the datasets required for testing the LLMs, including collect, clean, preprocess and validate the quality of the data.
    2. Experiment Setup: Establish testing environment for the LLMs, including configure hardware and software requirements for testing the models, and set up the testing environment.
    3. Performance Testing: Execute performance tests on the LLMs using the prepared datasets. Specifically, this task is to run each LLM with the datasets and record accuracy and latency metrics.
    4. Data Analysis: Analyze the test data to quantify the latency-accuracy relationship in the selected LLMs.
### 8.2 Task Partition
    The project tasks are divided and assigned to different team members or groups, ensuring efficient and expert execution at each stage.

| Team member  | Task  | 
|---|---|
| Zhuohao Li  |   | 
| Ying Li  |   | 



## 9. Related Work

### 9.a. Papers
List the key papers that you have identified relating to your project idea, and describe how they related to your project. Provide references (with full citation in the References section below).
#### The era of Large Language Models
The GPT series, starting with GPT[^11], demonstrated the capabilities of large-scale language models in generating coherent and contextually relevant text. Subsequent iterations, including GPT-2 and GPT-3, scaled up in terms of parameter count and training data, pushing the boundaries of model performance[^1]. Similarly, BERT and its variants improved performance in understanding context and nuances in language[^12].

#####TODO: ying-add llama

#### Evaluating Performance: Latency and Accuracy
While large language models achieved high accuracy, their practical deployment often faced challenges due to latency issues. Rajpurkar et al[^9] studied on models like SQuAD and others in the domain of question answering began to highlight the trade-offs between accuracy and latency. Further research by Wang et al.[^10] on GLUE and SuperGLUE benchmarks provided comprehensive frameworks for evaluating language models but did not focus extensively on latency.




### 9.b. Datasets

List datasets that you have identified and plan to use. Provide references (with full citation in the References section below).

### 9.c. Software

<!-- List softwate that you have identified and plan to use. Provide references (with full citation in the References section below). -->

In our project, several software tools and platforms will be utilized. These have been identified for their effectiveness in managing, executing, and analyzing large-scale AI models.
- PyTorch:An open-source machine learning library known for its flexibility and dynamic computational graph.[^13]
- Hugging Face's Transformers: A library providing thousands of pre-trained models to perform tasks on texts.[^14]

## 10. References


[^1]:Brown T, Mann B, Ryder N, et al. Language models are few-shot learners[J]. Advances in neural information processing systems, 2020, 33: 1877-1901
[^2]:  Kaplan J, McCandlish S, Henighan T, et al. Scaling laws for neural language models[J]. arXiv preprint arXiv:2001.08361, 2020.
[^3]: Bender E M, Gebru T, McMillan-Major A, et al. On the dangers of stochastic parrots: Can language models be too big?🦜[C]//Proceedings of the 2021 ACM conference on fairness, accountability, and transparency. 2021: 610-623.MLA
[^4]: Marcus G. The next decade in AI: four steps towards robust artificial intelligence[J]. arXiv preprint arXiv:2002.06177, 2020.MLA
[^5]: Llama 2. 2023.11. https://ai.meta.com/llama/
[^6]: Hu E J, Shen Y, Wallis P, et al. Lora: Low-rank adaptation of large language models[J]. arXiv preprint arXiv:2106.09685, 2021.MLA
[^7]: OpenAI. 2023. GPT3.5. https://openai.com/blog/gpt-3-5-turbo-fine-tuning-and-api-updates
[^8]: OpenAI. 2023. GPT4. https://openai.com/gpt-4
[^9]: Rajpurkar P, Zhang J, Lopyrev K, et al. Squad: 100,000+ questions for machine comprehension of text[J]. arXiv preprint arXiv:1606.05250, 2016.
[^10]: Wang A, Singh A, Michael J, et al. GLUE: A multi-task benchmark and analysis platform for natural language understanding[J]. arXiv preprint arXiv:1804.07461, 2018.
[^11]: Radford A, Narasimhan K, Salimans T, et al. Improving language understanding by generative pre-training[J]. 2018.
[^12]: Devlin J, Chang M W, Lee K, et al. Bert: Pre-training of deep bidirectional transformers for language understanding[J]. arXiv preprint arXiv:1810.04805, 2018.
[^13]:Paszke A, Gross S, Massa F, et al. Pytorch: An imperative style, high-performance deep learning library[J]. Advances in neural information processing systems, 2019, 32.
[^14]:Wolf T, Debut L, Sanh V, et al. Transformers: State-of-the-art natural language processing[C]//Proceedings of the 2020 conference on empirical methods in natural language processing: system demonstrations. 2020: 38-45.


