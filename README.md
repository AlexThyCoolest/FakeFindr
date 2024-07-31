# FakeFindr

FakeFindr is a web application designed to detect and flag fake news and misinformation. Using advanced algorithms and machine learning, it evaluates the credibility of sources and the content's authenticity.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Technologies Used](#technologies-used)
- [How to Use](#how-to-use)
- [Contributing](#contributing)

## Features

- **Real-time Analysis**: Quickly evaluates articles and sources.
- **User-friendly Interface**: Simple and intuitive design for easy navigation.
- **Machine Learning**: Continuously improves accuracy over time.
- **Customizable Settings**: Users can adjust the sensitivity of the analysis.

## Installation

To install FakeFindr, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/AlexThyCoolest/FakeFindr.git
    ```
2. Navigate to the project directory:
    ```bash
    cd FakeFindr
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```bash
    python app.py
    ```
2. Open your web browser and go to `http://localhost:8000`.

## File Structure

- `app.py`: Main application file.
- `templates/`: HTML templates for the web pages.
  - `index.html`: Main page template.
  - `results.html`: Results page template.
- `static/`: Static files (CSS, JS, images).
- `model/`: Pre-trained models and vectorizers.

## Technologies Used

- **Flask**: Web framework for Python.
- **BeautifulSoup**: Web scraping.
- **NLTK**: Natural language processing.
- **Joblib**: Model serialization.
- **Plotly**: Data visualization.

## How to Use

1. Copy the URL of an article you want to verify.
2. Paste the URL into the search bar on the homepage.
3. Click "Detect" and wait for the analysis.
4. View the results, including the authenticity score and sentiment analysis.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.
