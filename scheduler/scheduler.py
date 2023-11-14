from apscheduler.schedulers.blocking import BlockingScheduler
from utils.cmc_api import fetch_bitcoin_price
from db.database import insert_price

def job_function():
    price = fetch_bitcoin_price()
    insert_price(price)
    print(f"Fetched and saved price: {price}")

def start_scheduler():
    scheduler = BlockingScheduler()
    scheduler.add_job(job_function, 'interval', minutes=5)
    scheduler.start()
