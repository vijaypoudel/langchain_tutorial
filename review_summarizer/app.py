

from flask import Flask, request, jsonify
from textblob import TextBlob
from transformers import pipeline

app = Flask(__name__)

# Load the summarization pipeline
summarizer = pipeline("summarization", model="google/pegasus-large")

def analyze_sentiment(review):
    analysis = TextBlob(review)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    else:
        return 'negative'

def summarize_reviews(reviews, sentiment_type):
    if not reviews:
        return "No reviews available."

    # Concatenate all reviews into a single string for summarization
    concatenated_reviews = " ".join(reviews)
    # Summarize the concatenated reviews
    summary = summarizer(concatenated_reviews, max_length=150, min_length=20, do_sample=False)[0]['summary_text']

    if sentiment_type == 'positive':
        return f"Positive Feedback Summary: {summary}"
    else:
        return f"Negative Feedback Summary: {summary}"

@app.route('/reviews', methods=['POST'])
def reviews():
    try:
        reviews = request.json.get('reviews', [])
        if not isinstance(reviews, list):
            return jsonify({'error': 'Invalid input, expected a list of reviews'}), 400

        positive_reviews = []
        negative_reviews = []

        for review in reviews:
            sentiment = analyze_sentiment(review)
            if sentiment == 'positive':
                positive_reviews.append(review)
            else:
                negative_reviews.append(review)

        positive_summary = summarize_reviews(positive_reviews, 'positive')
        negative_summary = summarize_reviews(negative_reviews, 'negative')

        return jsonify({
            'positive_feedback_summary': positive_summary,
            'negative_feedback_summary': negative_summary
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
