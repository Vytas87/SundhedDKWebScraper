import pandas as pandas
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options


class PsychologistsCrawler:
    def __init__(self, hostname, executable_path, chrome_binary_location=None):
        self.hostname = hostname
        self.executable_path = executable_path

        if chrome_binary_location is not None:
            self.chrome_binary_location = chrome_binary_location
            options = Options()
            options.binary_location = self.chrome_binary_location
            self.driver = webdriver.Chrome(options=options, executable_path=self.executable_path)
        else:
            self.driver = webdriver.Chrome(self.executable_path)

    def get_psychologist_data(self, nr_of_psychologists=10):

        psychologists_data = pandas.DataFrame(columns=['Name', 'Phone', 'Street', 'PostBox'])

        self.driver.get(self.hostname)

        try:
            WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="scrollToResultat"]/div/div[2]/div')))
        finally:
            for psychologist in range(1, nr_of_psychologists + 1):
                try:
                    name_element = self.driver.find_element_by_xpath(str.format('//*[@id="scrollToResultat"]/div/div[2]/div/div[{}]/search-result-item/h3/a', psychologist))
                    name = name_element.text
                except NoSuchElementException:
                    name = '-'

                try:
                    phone_element = self.driver.find_element_by_xpath(str.format('//*[@id="scrollToResultat"]/div/div[2]/div/div[{}]/search-result-item/div[1]/div[1]/p/span/a', psychologist))
                    phone = phone_element.text
                except NoSuchElementException:
                    phone = '-'

                try:
                    address_street_element = self.driver.find_element_by_xpath(str.format('//*[@id="scrollToResultat"]/div/div[2]/div/div[{}]/search-result-item/div[1]/div[1]/div[2]/div[1]', psychologist))
                    address_street = address_street_element.text
                except NoSuchElementException:
                    address_street = '-'

                try:
                    address_postbox_element = self.driver.find_element_by_xpath(str.format('//*[@id="scrollToResultat"]/div/div[2]/div/div[{}]/search-result-item/div[1]/div[1]/div[2]/div[2]', psychologist))
                    address_postbox = address_postbox_element.text
                except NoSuchElementException:
                    address_postbox = '-'

                psychologists_data.loc[len(psychologists_data)] = [name, phone, address_street, address_postbox]
                psychologists_data.to_csv('Psychologists data.csv', header=True, sep=",")

                # The following was used for testing
                # print('{:5}. {:10}{}'.format(psychologist, 'Name:', name))
                # print('{:7}{:10}{}'.format('', 'Phone:', phone))
                # print('{:7}{:10}{}'.format('', 'Street:', address_street))
                # print('{:7}{:10}{}'.format('', 'PostBox:', address_postbox))

        self.driver.quit()
