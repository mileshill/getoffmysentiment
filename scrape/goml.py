"""
goml.py
Get Off My Lawn Scraper with Beautiful Soup
"""
import time
from selenium import webdriver




if __name__ == "__main__":
    URL = "https://getoffmylawnpod.libsyn.com/"

    options = webdriver.FirefoxOptions()
    # options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(URL)
    time.sleep(20)
    driver.close()


