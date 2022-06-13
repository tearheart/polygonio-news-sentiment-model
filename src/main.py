from fastapi import FastAPI
from pydantic import BaseModel

from transformers import BertTokenizer, BertForSequenceClassification, pipeline

import logging
from logging.config import dictConfig
from src.log_config import log_config

dictConfig(log_config)
logger = logging.getLogger("polygonio-news-sentiment-model-logger")

app = FastAPI(title="Sentiment Analysis: Financial News Articles")

# Represents a news article
class Article(BaseModel):
    headline: str

# Startup
@app.on_event("startup")
def load_model():
    global finbert, tokenizer
    finbert = BertForSequenceClassification.from_pretrained('yiyanghkust/finbert-tone',num_labels=3)
    tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert-tone')

# Home
@app.get("/")
def home():
    return "Congratulations! Your API is working as expected. Now head over to http://localhost:80/docs"

# Sentiment
@app.post("/sentiment")
def sentiment(article: Article):
    nlp = pipeline("text-classification", model=finbert, tokenizer=tokenizer)
    data = article.headline
    sent = nlp(data)
    print(sent)
    return { "Sentiment": sent }
