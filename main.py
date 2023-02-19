from fastapi import FastAPI
from Scraper import scraper
app=FastAPI()
quotes=scraper()
@app.get("/{cat}")
async def read_item(cat):
    return quotes.scrapdata(cat)