from typing import Optional
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from tinydb import TinyDB, Query
import scraper

app = FastAPI(
    title="BOZ Scraper",
    description="Get dollar exchange rates for all banks in Zambia with this api",
    version="1.0.0",
)
app.mount("/static", StaticFiles(directory="static"), name="static")
db = TinyDB('db.json')

templates = Jinja2Templates(directory="templates")

@app.get("/", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/register", response_class=HTMLResponse,include_in_schema=False)
def register(email:str = Form(...)):
    db.insert({"email": email})
    return """
        <div class="sm:text-center lg:text-left">
            <p
                class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
              >
                Thank you for Registering for notifications.
              </p>
            <p
                class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
              >
                You will begin to recieve notifications soon.
              </p>
        </div>
    """

@app.get("/bank")
def all_bank_rates():
    """
    Get all dollar exchange rates for all banks listed on the Bank of Zambia Website.
    This returns the rate's buy and sell for the bank for each time period i.e 9:30, 12:30, 15:30

    :return: Returns a JSON object containing all information of 
    :rtype: JSON
    """
    data = scraper.bank_exchange_rates()
    return data

@app.get("/bank/{query}")
def get_bank_rates(query: str):
    """
    Get the dollar exchange rate for a single bank.
    Send in the bank name or part of the bank name e.g "Stanbic " as the query string.

    :param query: Name of the bank you would like to 
    :type query: str
    :return: A JSON object with the buy and sell rate for the bank 
    :rtype: JSON
    """
    data = scraper.bank_exchange_rates()
    filtered_data = [d for d in data if query.lower() in d["bank"].lower()]
    return filtered_data