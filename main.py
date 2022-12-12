from flask import Flask, render_template, jsonify, request
from transformers import pipeline

app = Flask(__name__)

models = {
    'hub_bert': (
        pipeline('sentiment-analysis', model='lvwerra/bert-imdb'),
        {
            'LABEL_0': 'negative',
            'LABEL_1': 'positive'
        }
    ),
    'hub_distilbert': (
        pipeline('sentiment-analysis', model='lvwerra/distilbert-imdb'),
        {
            'NEGATIVE': 'negative',
            'POSITIVE': 'positive'
        }
    )
}

# Index html page
@app.route('/')
def index():
    return render_template('index.html', models=list(models.keys()))


@app.route('/predict', methods=['GET'])
def predict():
    text = request.args.get('text')
    pipeline, trans = models[request.args.get('model')]

    sentiment = trans[pipeline(text)[0]['label']]

    return jsonify({
        'text': text,
        'sentiment': sentiment
    })


if __name__ == '__main__':
    app.run()
