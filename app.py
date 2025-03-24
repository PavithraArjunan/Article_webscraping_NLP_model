import streamlit as st
import requests
import os

# Define Flask API URL (replace with the ngrok URL of your Flask app)
API_URL = "https://6afe-34-59-61-46.ngrok-free.app/get_company_data"  # Replace with your actual URL

# Function to fetch company data from the API
def fetch_company_data(company_name):
    try:
        response = requests.get(API_URL, params={'company_name': company_name})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None

# Function to display company data
def display_company_data(company_data):
    if 'error' in company_data:
        st.error(company_data['error'])
    else:
        # Assuming company_data is a dictionary of companies' data
        for company, data in company_data.items():
            if isinstance(data, dict):  # Ensure that data is a dictionary
                st.header(f"{company} News")
                st.write(f"**Sentiment Summary:** {data.get('Final Sentiment Analysis', 'N/A')}")
                st.write(f"**Sentiment Distribution:** {data.get('Comparative Sentiment Score', {}).get('Sentiment Distribution', 'N/A')}")

                st.write("**Articles:**")
                for article in data.get("Articles", []):
                    st.subheader(f"Title: {article.get('Title', 'No title')}")
                    st.write(f"Summary: {article.get('Summary', 'No summary')}")
                    st.write(f"Sentiment: {article.get('Sentiment', 'No sentiment')}")

                st.write("**Comparative Sentiment Analysis:**")
                for comparison in data.get("Comparative Sentiment Score", {}).get("Coverage Differences", []):
                    st.write(f"Comparison: {comparison.get('Comparison', 'No comparison')}")
                    st.write(f"Impact: {comparison.get('Impact', 'No impact')}")

                st.write("**Topic Overlap:**")
                topic_overlap = data.get("Comparative Sentiment Score", {}).get("Topic Overlap", {})
                st.write(f"Common Topics: {topic_overlap.get('Common Topics', 'N/A')}")
                st.write(f"Unique Topics: {topic_overlap.get('Unique Topics in Articles', 'N/A')}")

                # Add audio (Ensure the key exists in the correct structure)
                audio_file = data.get("audio_file")  # This is where we check for audio_file
                if isinstance(audio_file, str) and os.path.exists(audio_file):
                    with open(audio_file, 'rb') as audio:
                        st.audio(audio.read(), format="audio/mp3")
                else:
                    st.warning(f"Audio saved in api url for {company_name}.")
            else:
                # st.warning(f"Data format not supported for : {company_name}")
                pass

# Streamlit UI
st.title("Company News & Sentiment Analysis")
company_name = st.text_input("Enter a company name (e.g., Tesla, Maruti Suzuki, Mahindra, Tata Motors, Nissan-Honda):")

if st.button("Get Company Data"):
    if company_name:
        # Fetch data from API
        company_data = fetch_company_data(company_name)
        if company_data:
            st.write(company_data)  # This will help you see the actual response data
            display_company_data(company_data)
    else:
        st.warning("Please enter a company name.")
