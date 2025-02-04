import time
from datetime import datetime
from scrapper import run_scrapper

if __name__ == "__main__":

    scrap_executed = False

    while True:

        time_now = datetime.now()
        if (time_now.hour >= 0 and time_now.hour <= 1):
            run_scrapper()
            scrap_executed = True
        else:
            scrap_executed = False

        time.sleep(60)  