# Machine Translation

### Introduction

**Machine Translation (MT)** is a classic task in NLP. It uses models to translate text or speech from one language to another. In fact, at the very first stage of NLP, RNN, Transformer are all designed for machine translation task. It's a crucial field in natural language processing that aims to break language barriers and enable seamless communication across different languages. 

A variety of datasets are used for training and evaluating MT models. Common datasets used are briefly introduced as follows:

1. [Europarl Corpus](https://www.statmt.org/europarl/): A collection of documents from the European Parliament, available in 11 European languages. It's widely used for training and testing statistical machine translation models, especially for European languages.

2. [United Nations Parallel Corpus](https://conferences.unite.un.org/uncorpus): This corpus contains official United Nations documents in six official UN languages. It's large and diverse, making it suitable for training and evaluating models, especially for less common language pairs.

3. [OpenSubtitles](https://opus.nlpl.eu/OpenSubtitles2016.php): A large, multilingual collection of movie and TV subtitles. The informal and conversational style of the dataset makes it particularly valuable for training models that handle colloquial language.

4. [WMT](https://statmt.org/wmt20/translation-task.html#download) (Workshop on Statistical Machine Translation) Datasets: These are a series of datasets released as part of the WMT shared tasks. They include news commentaries and other texts and have become a standard benchmark for machine translation models.

5. [Tatoeba](https://tatoeba.org/en/): A collection of sentences and translations, aimed at covering a wide range of languages, including many low-resource languages. It's often used for testing the capabilities of translation models across diverse language pairs.

7. [IWSLT](https://iwslt.org/) (International Workshop on Spoken Language Translation) Datasets: These datasets focus on spoken language and are used in the IWSLT evaluation campaign. They're particularly valuable for systems that translate spoken language or subtitle videos.

### OpenSubtitles

We use **[OpenSubtitles](https://opus.nlpl.eu/OpenSubtitles2016.php)** (OpenSubtitles are fully open-sourced) for testing our LLMs deployment in our project due to its conversational and colloquial nature. The dataset comprises subtitles from movies and television shows, offering a rich and diverse range of everyday language and idiomatic expressions, making it ideal for developing MT models that handle conversational language effectively. As for its size, OpenSubtitles is one of the largest publicly available collections of translated subtitles, featuring millions of sentences, which makes it an extensive resource for training. The corpus covers a wide range of languages, including a significant volume of **Chinese-English translations**. In terms of testing metrics, common choices for evaluating MT models include BLEU (Bilingual Evaluation Understudy), which measures the correspondence between a model's output and reference translations, and METEOR, which considers factors like word order and synonyms. OpenSubtitles' informal and dialog-heavy content provides a unique challenge for MT, as capturing the nuances of spoken language and cultural context is typically harder than translating formal text. Its use in MT research and applications reflects a growing interest in developing models that perform well in real-world, conversational scenarios.

### Chinese-English Subsets in OpenSubtitles

The OpenSubtitles Chinese-English dataset is part of the larger OpenSubtitles collection, which comprises movie and TV show subtitles in various languages. The dataset is derived from subtitles of movies and TV shows. These subtitles are originally created for multilingual audiences and typically include a wide range of linguistic styles, from formal dialogue to colloquial and idiomatic expressions. Given its source, the dataset encompasses a diverse range of genres and contexts, making it a rich resource for natural language processing tasks, especially those involving conversational language.


The exact size of the Chinese-English portion we used  comprising **3M** of sentence pairs. The dataset usually comes in a parallel format, with Chinese sentences aligned with their English translations. This format is particularly useful for training and evaluating machine translation systems.

The data we're gonna use are stored in `./en-zh.txt` folder including English version (`OpenSubtitles.edn-zh.en`) and Chinese version (`OpenSubtitles.edn-zh.zn`).