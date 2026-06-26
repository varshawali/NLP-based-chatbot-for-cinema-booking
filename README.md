# 🎬 NLP-Based Chatbot for Cinema Booking

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![NLP](https://img.shields.io/badge/NLP-NLTK-154F3C?style=flat)](https://www.nltk.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> A conversational AI chatbot that lets users search, select, and book cinema tickets through natural language — powered by NLP techniques including lemmatisation, intent recognition, and entity extraction.

---

## 🎥 Demo

```
User:   I want to book 2 tickets for Dune Part 2 this Saturday evening.
Bot:    Sure! I found Dune: Part Two showing on Saturday at 7:30 PM at CineMark.
        Seats available: Standard, Premium. Which do you prefer?

User:   Premium please.
Bot:    Great! 2 Premium tickets for Dune: Part Two on Sat 7:30 PM.
        Total: $34.00. Shall I confirm the booking?

User:   Yes!
Bot:    ✅ Booking confirmed! Your booking ID is #CIN2847. Enjoy the movie!
---

## 🧠 How It Works

The chatbot pipeline has four stages:

```
User Input
    │
    ▼
Text Preprocessing
(tokenisation → lemmatisation → stopword removal)
    │
    ▼
Intent Classification
(greeting / search_movie / book_ticket / cancel / FAQ)
    │
    ▼
Entity Extraction
(movie name, date, time, number of seats, seat type)
    │
    ▼
Response Generation
(template-based + dynamic data lookup)
```

### NLP Techniques Used
- **Tokenisation & Lemmatisation** — NLTK WordNet Lemmatizer
- **Intent Recognition** — TF-IDF + cosine similarity / rule-based matching
- **Named Entity Recognition** — Custom entity extraction for movie names, dates, and times
- **Dialogue Management** — State-tracking for multi-turn conversations

---

## 🛠️ Setup & Usage

### Installation

```bash
git clone https://github.com/varshawali/NLP-based-chatbot-for-cinema-booking.git
cd NLP-based-chatbot-for-cinema-booking
pip install -r requirements.txt
python -m nltk.downloader punkt wordnet stopwords
```

### Run the chatbot (terminal)

```bash
python chatbot.py
```

### Run as a web app (Streamlit)

```bash
pip install streamlit
streamlit run app.py
```

---

## 📁 Project Structure

```
├── chatbot.py              # Core chatbot logic
├── app.py                  # Streamlit web interface
├── intents.json            # Intent definitions and training phrases
├── preprocessing.py        # Text cleaning and lemmatisation
├── entity_extractor.py     # Movie name, date, time extraction
├── movies_data.json        # Mock cinema schedule database
├── requirements.txt
└── README.md
```

---

## 💬 Supported Intents

| Intent | Example Phrases |
|---|---|
| Greeting | "Hi", "Hello", "Hey there" |
| Search movie | "What's showing this weekend?", "Find action movies" |
| Book ticket | "Book 2 tickets for Inception tonight" |
| Check availability | "Is Oppenheimer showing at 8pm?" |
| Cancel booking | "Cancel my booking #CIN2847" |
| Get help | "What can you do?", "Help" |


---

## 🔖 Topics

`nlp` `chatbot` `python` `nltk` `lemmatization` `intent-recognition` `conversational-ai` `cinema` `streamlit` `entity-extraction`

---

## 📬 Contact

**Varsha Wali** — [LinkedIn](https://www.linkedin.com/in/varshawali) · [GitHub](https://github.com/varshawali)
