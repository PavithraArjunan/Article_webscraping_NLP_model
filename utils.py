import os
from textblob import TextBlob
import spacy
from gtts import gTTS
from deep_translator import GoogleTranslator
import requests
from bs4 import BeautifulSoup

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Predefined company keywords for identification
company_keywords = {
    "Tesla": ["tesla", "elon musk", "cybertruck"],
    "Maruti Suzuki": ["maruti", "suzuki"],
    "Mahindra": ["mahindra", "xuv700", "thar"],
    "Tata Motors": ["tata", "jaguar", "land rover"],
    "Nissan-Honda": ["nissan", "honda"]
}

def analyze_sentiment(text):
    """Perform sentiment analysis and return polarity label."""
    score = TextBlob(text).sentiment.polarity
    if score > 0.5:
        return "Very Positive"
    elif score > 0:
        return "Positive"
    elif score == 0:
        return "Neutral"
    elif score > -0.5:
        return "Negative"
    else:
        return "Very Negative"

def identify_company(title, summary):
    """Identify company based on keywords in the title/summary."""
    combined_text = f"{title} {summary}".lower()
    for company, keywords in company_keywords.items():
        if any(keyword in combined_text for keyword in keywords):
            return company
    return "Other"

def extract_topics(summary):
    """Extract relevant topics dynamically using NLP."""
    doc = nlp(summary)
    return list(set(ent.text for ent in doc.ents if ent.label_ in ["ORG", "PRODUCT", "EVENT"]))

def text_to_speech(text, filename="output.mp3"):
    """Convert text to Hindi speech and save as an audio file."""
    translated_text = GoogleTranslator(source="auto", target="hi").translate(text)
    tts = gTTS(translated_text, lang="hi")
    
    audio_folder = "static/audio"
    os.makedirs(audio_folder, exist_ok=True)
    
    file_path = os.path.join(audio_folder, filename)
    tts.save(file_path)
    
    return file_path

def scrape_article(url):
    """Scrape the content of a news article from a given URL."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract headline (assuming <h1> tag)
        headline = soup.find("h1").text if soup.find("h1") else "No title found"
        
        # Extract article content (assuming <p> tags for paragraphs)
        paragraphs = soup.find_all("p")
        article_text = " ".join([p.text for p in paragraphs])
        
        return headline, article_text
    except requests.exceptions.RequestException as e:
        print(f"Error scraping {url}: {e}")
        return None, None
