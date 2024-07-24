from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import re
import joblib
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string
import plotly.graph_objs as go
import plotly
import json
import logging
import ssl

# Fix SSL certificate issue for NLTK
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download("punkt", quiet=True)
nltk.download("wordnet", quiet=True)

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Preprocessing function
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token not in string.punctuation]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return " ".join(tokens)

# Function to scrape article content from URL
def scrape_article(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        content = ""
        for container in ["article", "main", 'div[class*="content"]', 'div[class*="article"]', 'div[id*="content"]', 'div[id*="article"]']:
            if content:
                break
            elements = soup.select(container)
            if elements:
                content = elements[0].get_text(strip=True, separator=" ")

        if not content:
            paragraphs = soup.find_all("p")
            content = " ".join([p.get_text(strip=True) for p in paragraphs])

        if not content:
            divs = soup.find_all("div")
            content = " ".join([div.get_text(strip=True) for div in divs])

        if content:
            return clean_text(content)
        else:
            logging.error("Couldn't extract meaningful content from the webpage.")
            return None
    except requests.RequestException as e:
        logging.error(f"An error occurred while fetching the article: {e}")
        return None

# Function to clean text
def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-zA-Z0-9\s.,!?]", "", text)
    return text.strip()

# Load models and vectorizers
try:
    fake_news_model = joblib.load('model/model.pkl')
    fake_news_vectorizer = joblib.load('model/vectorizer.pkl')
    sentiment_model = joblib.load('model/sentiment_model.pkl')
    sentiment_vectorizer = joblib.load('model/sentiment_vectorizer.pkl')
    logging.info("Models and vectorizers loaded successfully.")
except Exception as e:
    logging.error(f"Error loading models: {e}")

# Function to predict fake news
def predict_fake_news(text, model, vectorizer):
    preprocessed_text = preprocess_text(text)
    vectorized_text = vectorizer.transform([preprocessed_text])
    score = model.predict_proba(vectorized_text)[0][0]  # Get probability of being fake
    prediction = 1 if score < 0.5 else 0
    return prediction, score

# Function to analyze sentiment
def analyze_sentiment(text, vectorizer, sentiment_model):
    preprocessed_text = preprocess_text(text)
    vectorized_text = vectorizer.transform([preprocessed_text])
    sentiment_proba = sentiment_model.predict_proba(vectorized_text)[0]
    sentiment = sentiment_model.classes_[sentiment_proba.argmax()]
    return sentiment

# Function to generate confidence graph using Plotly
def generate_confidence_graph(score):
    labels = ['Fake', 'Real']
    sizes = [score, 1 - score]
    colors = ['red', 'green']

    fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, hole=.3, marker=dict(colors=colors))])
    fig.update_layout(title_text='Confidence Level', annotations=[dict(text='Fake/Real', x=0.5, y=0.5, font_size=20, showarrow=False)])

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

@app.route("/results", methods=["POST", "GET"])
def results():
    try:
        if request.method == "POST":
            url = request.form.get("articleURL")
            logging.debug(f"Received URL: {url}")
            article_content = scrape_article(url)
            if article_content:
                logging.debug("Article content fetched successfully.")
                prediction, score = predict_fake_news(article_content, fake_news_model, fake_news_vectorizer)
                sentiment = analyze_sentiment(article_content, sentiment_vectorizer, sentiment_model)
                result = "Real" if prediction == 1 else "Fake"

                if score < 0.5:
                    confidence = "Not Very Confident"
                elif score < 0.7:
                    confidence = "Somewhat Confident"
                else:
                    confidence = "Very Confident"

                # Generate confidence graph
                graphJSON = generate_confidence_graph(score)

                return render_template('results.html', url=url, result=result, sentiment=sentiment, score=score, confidence=confidence, graphJSON=graphJSON)
            else:
                logging.error("Failed to fetch article content.")
                return render_template("results.html", url=url, result="Unable to analyze", sentiment="N/A", score=0, confidence="N/A")
        return render_template("index.html")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return "An error occurred while processing your request."

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)