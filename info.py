from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


class google:
    def __init__(self):
        self.query = None
        options = webdriver.ChromeOptions()
        service = Service(executable_path="C:\Windows\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service, options=options)

    def get_google_info(self, query):
        self.query = query
        self.driver.get(url="https://www.google.com/")

        search = self.driver.find_element("xpath", '//*[@id="APjFqb"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element("xpath", "//input[@name='btnK']")
        enter.click()

        time.sleep(600)  # Let the user actually see something!


# assist = google()
# assist.get_google_info("bengali comics")
