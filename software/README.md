

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

**Our Hugging Face Settings:**

We utilize [Colab](https://colab.google/) from Google to better deploy our LLMs on Cloud, the runtime we select is **NVIDIA V100 / A100 GPU**. All the code in `Hugging-face` could be executed online by notebook with the name `ipynb`.

### MacOS

### GPU server

Our server is supported by the following information:

```shell
GPU server:~$ cat /etc/os-release
NAME="Ubuntu"
VERSION="20.04.6 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 20.04.6 LTS"
VERSION_ID="20.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=focal
UBUNTU_CODENAME=focal
```

- Memory: 125GB

- Storage: 1.5T

- CPU: 16\* Intel(R) Xeon(R) Gold 5222 CPU @ 3.80GHz

- GPU: 3\* NVIDIA RTX A6000 (48GB)

- CUDA version: r12.2
