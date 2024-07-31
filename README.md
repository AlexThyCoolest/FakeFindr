# FakeFindr

## 📰 Identify Fake News with AI

FakeFindr is an advanced Flask-based web application that leverages machine learning to identify and flag fake news and misinformation, helping users discern the authenticity of online articles.

![A 1-minute demo of the website](https://github-production-user-asset-6210df.s3.amazonaws.com/118056225/351786228-dbb7f2c5-5d1f-4e3b-8bf9-38f25bd7c8f8.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240724%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240724T155535Z&X-Amz-Expires=300&X-Amz-Signature=ae1b9cc088fbfbdbeda5e39f7dd02af67f2b761098259232b168c412ec46fb67&X-Amz-SignedHeaders=host&actor_id=118056225&key_id=0&repo_id=832837105)

## 🌟 Features

- 🔍 Real-time article analysis
- 🤖 Fake news detection using machine learning
- 📊 Sentiment analysis of the content
- 📈 Confidence level visualization with Plotly
- 🚀 Easy-to-use interface

## 🛠️ Technologies Used

- **Backend**: Flask, Python 3.x
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: scikit-learn, NLTK, joblib
- **Web Scraping**: BeautifulSoup, requests
- **Data Visualization**: Plotly

## 📋 Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- pip
- virtualenv (recommended)

## 🚀 Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/AlexThyCoolest/FakeFindr.git
   cd FakeFindr
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   python app.py
   ```

   The application will be available at `http://localhost:8000`.

### OR

#### Set up a GitHub Codespace

1. **Open This Repository**: Go to this GitHub repository where my project is located.
2. **Create a Codespace**:
   - Click on the green "Code" button at the top right of your repository.
   - Select the "Codespaces" tab.
   - Click "New codespace" to create a new Codespace environment.

#### Download Dependencies

Once the Codespace is set up and the environment is ready:

1. **Open the Terminal**: In the Codespace environment, you will have a terminal window available at the bottom.
2. **Install Dependencies**:

   ```bash
   pip install flask beautifulsoup4 requests joblib nltk plotly
   ```

#### Run Python

   ```bash
   python app.py
   ```

The application will be available at `http://localhost:8000`.

## 💻 Usage

1. Open your web browser and navigate to `http://localhost:8000`.
2. Enter the URL of the article you want to verify.
3. Click "Detect" and wait for the analysis.
4. Review the results, including:
   - Article authenticity prediction (Real or Fake)
   - Emotional tone of the article
   - Confidence level visualization

## 📁 Project Structure

```
├── app.py                 # Main Flask application
├── README.md              # Project documentation
├── static/                # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
|   ├── plugins/
│   └── images/
├── templates/             # HTML templates
│   ├── index.html
│   └── results.html
└── model/                 # Pre-trained ML models and data
    ├── model.pkl
    ├── vectorizer.pkl
    ├── sentiment_model.pkl
    └── sentiment_vectorizer.pkl
```

## 🧠 How It Works

1. **Web Scraping**: Uses BeautifulSoup to scrape article content.
2. **Data Preprocessing**: Cleans and tokenizes text using NLTK.
3. **Feature Extraction**: Utilizes TF-IDF vectorization for text features.
4. **Machine Learning**: Employs Logistic Regression to classify articles.
5. **Sentiment Analysis**: Analyzes article sentiment using pre-trained models.
6. **Result Aggregation**: Combines ML predictions and sentiment analysis for final result.

## 📊 Performance Metrics

| Metric    | Score  |
|-----------|--------|
| Accuracy  | 88%    |
| Precision | 100%   |
| Recall    | 0.59   |
| F1 Score  | 0.74   |

## 🤝 Contributing

Contributions to FakeFindr are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Contact

Alex Agboola - [My Portfolio](https://alexagboola.com) - alexagboolacodes@gmail.com

Project Link: [https://github.com/AlexThyCoolest/FakeFindr](https://github.com/AlexThyCoolest/FakeFindr)

## 🙏 Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [scikit-learn](https://scikit-learn.org/)
- [NLTK](https://www.nltk.org/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Plotly](https://plotly.com/)
