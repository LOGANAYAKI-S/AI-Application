import streamlit as st
import requests

NEWS_API_KEY = st.secrets["NEWS_API_KEY"]


def get_news(topic):

    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={topic}"
        f"&sortBy=publishedAt"
        f"&language=en"
        f"&pageSize=5"
        f"&apiKey={NEWS_API_KEY}"
    )

    response = requests.get(url)

    data = response.json()

    reply = f"## 📰 Latest {topic.title()} News\n\n"

    if data["status"] == "ok" and len(data["articles"]) > 0:

        for article in data["articles"]:

            title = article.get("title", "No Title")

            description = article.get("description")

            if not description:
                description = "Click the link below to read full news."

            news_url = article.get("url", "")

            source = article.get("source", {}).get("name", "Unknown")

            published = article.get("publishedAt", "")

            reply += f"""
### 📰 {title}

📝 {description}

🌍 Source: {source}

📅 Date: {published[:10]}

🔗 Read More:
{news_url}

---
"""

    else:

        reply = "❌ No latest news found."

    return reply