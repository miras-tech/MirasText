# MirasText: An Automatically Generated Text Corpus for Persian
This repository contains MirasText corpus and description along side with what it has been used for and what it can be used for. A sample of the dataset is provided in MirasText_sample.txt which contains 1000 documents. The full dataset is uploaded in google drive and you can download it [here](https://drive.google.com/file/d/1QNHPv4B22d-Dj7oYoOKQNx2zUfFzsAUL/view?usp=sharing). In order to use the complete dataset you need to submit a request to behnam@miras-tech.com and we will provide you with the password needed to extract MirasText.zip.

## MirasText Description
MirasText is the result of crawling more than 250 persain news websites. Each article in MirasText contains the following attributes:
* Content: The article content
* Description: The summary provided for each article (may not be available in some articles (nan))
* Keywords: The keywords associated with each article (may not be available in some articles (nan))
* Title: Title of the article
* Website: The website from which the article is crawled
* URL: The article absolute URL

MirasText has more than 2.8 million articles and over 1.4 billion content words. The following table demonstrates the statistics of the corpus:

|       Total Documents      |   2,835,414   |
|:--------------------------:|:-------------:|
|     Total Content Words    | 1,429,878,960 |
|   Average Content Length   |     504.3     |
|      Average Keywords      |      8.4      |
| Average Description Length |      19.8     |
|    Average Title Length    |      9.5      |

## What it has been used for
At Miras Technologies International we are using MirasText to develop some NLP applications. including:
* Document Classification
* Word Embedding Extraction
* Summarization
* Keyword Extraction

Please inform us if you have used MirasText for any porpuses to be added to this list.

## What it can be used for
MirasText can be used for a variety of NLP tasks, besides from the applications mentioned above it can also be used for:
* Language Modeling
* Title Extraction
* Named Entity Recognition (for an unsupervised approach)

## Dataset Description
The dataset is provided in MirasText.zip. You will have to extract it first, then simply use parser.py to read the dataset line by line. Each line contains one article. The attributes of each article are delimited using an special delimiter to avoid conflicts. (delimiter = ***)

Each article is provided in the following format:
content *** description *** keywords *** title *** website *** url
(note that *** is the delimiter used to separate the attributes)

## Cite
Please cite the following paper in your publication if you are using MirasText in your research:
```bibtex
@InProceedings{SABETI18.385,
  author = {Behnam Sabeti ,Hossein Abedi Firouzjaee ,Ali Janalizadeh Choobbasti ,Seyed hani elamahdi Mortazavi Najafabadi and Amir Vaheb},
  title = {MirasText: An Automatically Generated Text Corpus for Persian},
  booktitle = {Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018)},
  year = {2018},
  month = {may},
  date = {7-12},
  location = {Miyazaki, Japan},
  editor = {Nicoletta Calzolari (Conference chair) and Khalid Choukri and Christopher Cieri and Thierry Declerck and Sara Goggi and Koiti Hasida and Hitoshi Isahara and Bente Maegaard and Joseph Mariani and Hélène Mazo and Asuncion Moreno and Jan Odijk and Stelios Piperidis and Takenobu Tokunaga},
  publisher = {European Language Resources Association (ELRA)},
  address = {Paris, France},
  isbn = {979-10-95546-00-9},
  language = {english}
  }
  ```