from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class music:
    def __init__(self):
        self.query = None
        options = webdriver.ChromeOptions()
        service = Service(executable_path="C:\Windows\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service, options=options)

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)

        # video = self.driver.find_element(By.XPATH, '//*[@id="dismissible"]')

        video = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="dismissible"][1]'))
        )
        video.click()
        time.sleep(600)


# assist = music()
# assist.play('jab we met song')
