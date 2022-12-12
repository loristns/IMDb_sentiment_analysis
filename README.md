# IMDB Sentiment Analysis

This is a simple Flask application that uses a pre-trained BERT or DistilBERT model to classify the sentiment of movie reviews.

We use fine-tuned BERT and DistilBERT models from Hugging Face Hub. The models are available at the following links:

- [lvwerra/bert-imdb](https://huggingface.co/lvwerra/bert-imdb)
- [lvwerra/distilbert-imdb](https://huggingface.co/lvwerra/distilbert-imdb)

Those models are licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0.html).

### Context

This project was created as part of a course about the Scientific Research environment at the University of La Rochelle.
It was a collaborative project between [Dorian Maidon](https://github.com/statickzz), [Aliou Ly](https://github.com/aliou-ly) and myself.

## Prerequisites

- Python 3
- PyTorch
- Transformers ([https://github.com/huggingface/transformers](https://github.com/huggingface/transformers))
- Flask

## Usage
To run the Flask application, use the following command:

```bash
python app.py
```

The application will then be available at http://localhost:5000/. To classify the sentiment of a movie review through the user interface, go to the homepage and enter a movie review in the input field.

To classify the sentiment of a movie review through the API endpoint, send a GET request to `http://localhost:5000/predict?text=<review>&model=<model_name>`.
 The response will be a JSON object with the predicted sentiment.

## Dataset
The program uses either the BERT or DistilBERT model, which have been fine-tuned on IMDb movie reviews dataset.

```
@InProceedings{maas-EtAl:2011:ACL-HLT2011,
  author    = {Maas, Andrew L.  and  Daly, Raymond E.  and  Pham, Peter T.  and  Huang, Dan  and  Ng, Andrew Y.  and  Potts, Christopher},
  title     = {Learning Word Vectors for Sentiment Analysis},
  booktitle = {Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies},
  month     = {June},
  year      = {2011},
  address   = {Portland, Oregon, USA},
  publisher = {Association for Computational Linguistics},
  pages     = {142--150},
  url       = {http://www.aclweb.org/anthology/P11-1015}
}
```

## Further Reading
For more information on the BERT and DistilBERT models, please see the following papers:

- BERT: https://arxiv.org/abs/1810.04805
- DistilBERT: https://arxiv.org/abs/1910.01108
