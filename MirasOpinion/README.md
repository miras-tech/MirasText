# MirasOpinion: A Sentiment Analysis Dataset for Persian
This repository contains information about MirasOpinion dataset, which is the largest Persian sentiment analysis dataset up to this date, alongside a demo file which contains 20 documents with their corresponding labels. MirasOpinion.zip contains the whole dataset. In order to use the complete dataset you need to submit a request to behnamsabeti@gmail.com and we will provide you with the password needed to extract MirasOpinion.zip.

## What Is MirasOpinion?
MirasOpinion is crawled from the Digikala website, one of the largest e-commerce websites in Iran. 2.5 million comments have been crawled, and after some pre-processing, we reduce its size to one million comments. Then the corpus had been labeled using crowd-sourcing; A telegram bot is used to send the unlabeled data to several users. Our bot asks them to label the represented document as positive, negative, or neutral.

Here is a summary of our dataset statistics:

| Total Documents   | 93,868 |
|-------------------|--------|
| Max Length        | 1434   |
| Min Length        | 3      |
| Mean Length       | 38.15  |
| Positive Comments | 49515  |
| Negative Comments | 14882  |
| Neutral Comments  | 29471  |


## Cite
Please cite the following paper in your publication if you are using MirasOpinion in your research:
```bibtex
@inproceedings{ashrafi-asli-etal-2020-optimizing,
    title = "Optimizing Annotation Effort Using Active Learning Strategies: A Sentiment Analysis Case Study in {P}ersian",
    author = "Ashrafi Asli, Seyed Arad  and
      Sabeti, Behnam  and
      Majdabadi, Zahra  and
      Golazizian, Preni  and
      fahmi, reza  and
      Momenzadeh, Omid",
    booktitle = "Proceedings of The 12th Language Resources and Evaluation Conference",
    month = may,
    year = "2020",
    address = "Marseille, France",
    publisher = "European Language Resources Association",
    url = "https://www.aclweb.org/anthology/2020.lrec-1.348",
    pages = "2855--2861",
    language = "English",
    ISBN = "979-10-95546-34-4",
}
```