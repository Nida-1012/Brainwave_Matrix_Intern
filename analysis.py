import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
# Make sure 'src' is in the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Import custom modules
from src.data_collection import fetch_tweets
from src.preprocessing import clean_tweet
from src.sentiment import analyze_sentiment

# Step 1: Fetch Tweets
print("🔍 Fetching tweets...")
query = "ChatGPT since:2024-01-01 until:2024-12-31"
df = fetch_tweets(query, limit=1000)

if df.empty:
    print("⚠️ No tweets found. Try adjusting the query or date range.")
    sys.exit()

# Step 2: Clean Tweets
print("🧹 Cleaning tweets...")
df['Cleaned_Tweet'] = df['Tweet'].apply(clean_tweet)

# Step 3: Analyze Sentiment
print("💬 Analyzing sentiment...")
df['Sentiment'] = df['Cleaned_Tweet'].apply(analyze_sentiment)

# Step 4: Save Data
os.makedirs('data', exist_ok=True)
df.to_csv('data/tweets.csv', index=False)
print("📁 Data saved to data/tweets.csv")

# Step
