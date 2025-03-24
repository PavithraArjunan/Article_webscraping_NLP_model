# Company News & Sentiment Analysis App

This is a Streamlit web application that fetches and displays news and sentiment analysis data for a given company. The app interacts with a Flask API that provides company-specific sentiment analysis data.

## Features
- Accepts a company name as input.
- Fetches company news and sentiment analysis from a Flask API.
- Displays sentiment summary and sentiment distribution.
- Shows news articles with titles, summaries, and sentiment scores.
- Presents comparative sentiment analysis, including coverage differences and topic overlap.
- Provides an audio file you can downloaded in colab inside (static/audio).

## Requirements
Make sure you have the following installed before running the app:

- Python 3.8+
- Streamlit
- Requests

You can install the required dependencies using:

1. Install dependencies:
   ```bash
   pip install streamlit requests
   ```
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## How to Run the App
1. Ensure the Flask API is running and accessible via ngrok or another method.
2. Update the `API_URL` variable in the script with the correct API endpoint.
3. Run the Streamlit app using the command:
```bash
streamlit run app.py
```
4. Enter a company name and click "Get Company Data" to fetch and display the relevant information.

## API Endpoint
The app interacts with the following Flask API endpoint:
```
GET /get_company_data?company_name=<company_name>
```
- **Request Parameter:** `company_name` (str) - The name of the company for which news and sentiment analysis is needed.
- **Response Format:** JSON containing company news, sentiment scores, and articles.

## Expected API Response Format
```json
{
  "Company_Name": {
    "Final Sentiment Analysis": "Positive/Negative/Neutral",
    "Comparative Sentiment Score": {
      "Sentiment Distribution": "Details about sentiment",
      "Coverage Differences": [
        {"Comparison": "Details", "Impact": "Details"}
      ],
      "Topic Overlap": {
        "Common Topics": "Details",
        "Unique Topics in Articles": "Details"
      }
    },
    "Articles": [
      {"Title": "Title of the Article", "Summary": "Short summary", "Sentiment": "Positive/Negative/Neutral"}
    ],
    "audio_file": "Path to the audio file if available"
  }
}
```
## Backend (Flask)

### Features
- Scrapes news articles from predefined URLs.
- Performs sentiment analysis using **TextBlob**.
- Extracts company names based on predefined keywords.
- Identifies key topics using **spaCy**.
- Generates Hindi-translated audio summaries using **gTTS**.
- Exposes a REST API endpoint (`/get_company_data`) for frontend consumption.

### Setup
1. Install dependencies:
   ```bash
   pip install flask pyngrok requests beautifulsoup4 textblob spacy gtts deep-translator
   ```
2. Download the English NLP model for **spaCy**:
   ```bash
   python -m spacy download en_core_web_sm
   ```
3. Run the Flask app:
   ```bash
   python backend.py
   ```
   The Flask app will be exposed via **ngrok**.

### API Endpoint
- **URL:** `/get_company_data`
- **Method:** `GET`
- **Query Parameter:** `company_name`
- **Response:**
  ```json
  {
    "company_data": { ... },
    "audio_file": "https://your-ngrok-url/static/audio/company_news.mp3"
  }
  ```

---

## Future Improvements
- Implement real-time news scraping.
- Add more robust NLP techniques for topic modeling.
- Improve sentiment analysis accuracy with **transformer-based models**.
- Optimize audio file storage and retrieval.

## Troubleshooting
- If no data is returned, check the API URL and ensure the Flask server is running.
- If an error occurs, verify that the API response matches the expected format.
- If the audio file is not playing, ensure the file exists at the provided path.

## Notes
- Ensure the ngrok URL is up to date and correctly set in `API_URL`.
- The app is designed for companies like Tesla, Maruti Suzuki, Mahindra, Tata Motors, and Nissan-Honda, but can be extended.
- Modify the API response parsing logic if the structure changes.

## Author
Developed by Pavithra A as part of sentiment analysis project.


