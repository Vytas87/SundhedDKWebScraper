from Crawlers import PsychologistsCrawler
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re

hostname = 'https://www.sundhed.dk/borger/guides/find-behandler/?Page=1&Pagesize=100&RegionId=0&MunicipalityId=0&Sex=0&AgeGroup=0&DisabilityFriendlyAccess=false&GodAdgang=false&EMailConsultation=false&EMailAppointmentReservation=false&EMailPrescriptionRenewal=false&TakesNewPatients=false&Name=psykolog&TreatmentAtHome=false&WaitTime=false'
chrome_binary_location = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
executable_path=r'C:/Users/irina/AppData/Local/Programs/Python/Python39/chromedriver.exe'

options = Options()
options.binary_location = chrome_binary_location
driver = webdriver.Chrome(options=options, executable_path=executable_path)

driver.implicitly_wait(10)

driver.get(hostname)

# Find the number of all psychologists
# NOTE: if the hostname with the 'Pagesize' attribute is created in the 'Crawlers' class and used again,
#       somehow Sundhed.dk servers actively refuse reopening the webpage with the modified attribute.
#       However, when it is created here and passed in as an argument when creating the PsychologistsCrawler
#       object, the trick passes through
nr_of_psychologists_element = driver.find_elements_by_xpath('//*[@id="scrollToResultat"]/div/div[1]/div[1]/span[1]/p')[0]
nr_of_psychologists_str = nr_of_psychologists_element.text.split()[6]
nr_of_psychologists = int(nr_of_psychologists_str)

driver.quit()

hostname = re.sub('Pagesize=[0-9]+', 'Pagesize=' + nr_of_psychologists_str, hostname)

psychologists_crawler = PsychologistsCrawler(hostname, executable_path, chrome_binary_location=chrome_binary_location)
psychologists_crawler.get_psychologist_data(nr_of_psychologists)
