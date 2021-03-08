from typing import Optional
from fastapi import FastAPI
import scraper

app = FastAPI()

@app.get("/bank")
def all_bank_rates():
    data = scraper.bank_exchange_rates()
    return data

@app.get("/bank/{query}")
def get_bank_rates(query: str):
    data = scraper.bank_exchange_rates()
    filtered_data = [d for d in data if query.lower() in d["bank"].lower()]
    return filtered_data