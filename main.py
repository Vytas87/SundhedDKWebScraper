from Crawlers import PsychologistsCrawler

psychologists_crawler = PsychologistsCrawler('https://www.sundhed.dk/borger/guides/find-behandler/?Page=1&Pagesize=100&RegionId=0&MunicipalityId=0&Sex=0&AgeGroup=0&DisabilityFriendlyAccess=false&GodAdgang=false&EMailConsultation=false&EMailAppointmentReservation=false&EMailPrescriptionRenewal=false&TakesNewPatients=false&Name=psykolog&TreatmentAtHome=false&WaitTime=false',
                                             chrome_binary_location='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe')
psychologists_crawler.get_psychologist_data()
