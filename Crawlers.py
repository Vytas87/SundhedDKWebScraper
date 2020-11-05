from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

class PsychologistsCrawler:
    def __init__(self, hostname, chrome_binary_location=None, executable_path=r'C:/Users/irina/AppData/Local/Programs/Python/Python39/chromedriver.exe'):
        self.hostname = hostname
        self._executable_path = executable_path

        if chrome_binary_location is not None:
            self.chrome_binary_location = chrome_binary_location
            options = Options()
            options.binary_location = self.chrome_binary_location
            self.driver = webdriver.Chrome(options=options, executable_path=executable_path)
        else:
            self.driver = webdriver.Chrome(executable_path)

        self.driver.get(hostname)

        # Find the number of psychologists
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="scrollToResultat"]/div/div[1]/div[1]/span[1]/p')))
        finally:
            nr_of_psychologists_element = self.driver.find_elements_by_xpath('//*[@id="scrollToResultat"]/div/div[1]/div[1]/span[1]/p')[0]
            nr_of_psychologists = int(nr_of_psychologists_element.text.split()[6])
            print(nr_of_psychologists)

        page_size = re.search('Pagesize[0-9]+&', hostname)
        print(page_size)

        self.driver.quit()

        # Open the webpage with all psychologists
        # self.driver.get()

    def get_psychologist_data(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="scrollToResultat"]/div/div[2]/div/div[3]/search-result-item/h3/a')))
        finally:
            name_element = self.driver.find_elements_by_xpath('//*[@id="scrollToResultat"]/div/div[2]/div/div[3]/search-result-item/h3/a')[0]
            name = name_element.text

            phone_element = self.driver.find_elements_by_xpath('//*[@id="scrollToResultat"]/div/div[2]/div/div[3]/search-result-item/div[1]/div[1]/p/span/a')[0]
            phone = phone_element.text

            address_street_element = self.driver.find_elements_by_xpath('//*[@id="scrollToResultat"]/div/div[2]/div/div[3]/search-result-item/div[1]/div[1]/div[2]/div[1]')[0]
            address_street = address_street_element.text

            address_postbox_element = self.driver.find_elements_by_xpath(
                '//*[@id="scrollToResultat"]/div/div[2]/div/div[3]/search-result-item/div[1]/div[1]/div[2]/div[2]')[0]
            address_postbox = address_postbox_element.text

            self.driver.quit()

            print('{:10}{}'.format('Name:', name))
            print('{:10}{}'.format('Phone:', phone))
            print('{:10}{}'.format('Street:', address_street))
            print('{:10}{}'.format('PostBox:', address_postbox))
