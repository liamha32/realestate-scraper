from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

city = input("Choose a city: ")
state = input("Choose a state abbreviation: ")

website = f'https://www.zillow.com/homes/for_sale/{city},-{state}_rb/'
path = "D:\chromedriver-win64\chromedriver.exe"
driver = webdriver.Chrome(executable_path='D:\chromedriver-win64\chromedriver.exe')
driver.get(website)

listings = driver.find_elements(By.XPATH,'//li[@class="ListItem-c11n-8-102-0__sc-13rwu5a-0 StyledListCardWrapper-srp-8-102-0__sc-wtsrtn-0 hKdzLV kgwlbT"]')
prices = driver.find_elements(By.XPATH, '//div[@class="PropertyCardWrapper__StyledPriceGridContainer-srp-8-102-0__sc-16e8gqd-0 eFBhnu"]')
addresses = driver.find_elements(By.XPATH, '//address[@data-test="property-card-addr"]')
sizes = driver.find_elements(By.XPATH, '//ul[@class="StyledPropertyCardHomeDetailsList-c11n-8-102-0__sc-1j0som5-0 exCsDV"]')

# try:
#     next_page = driver.find_element(By.XPATH, '//a[@rel="next"]')
#     next_page.click()
# except:
#     pass


price = []
address = []
size = []
h = 0

while h < 19:
    for i in prices:
        i = i.text
        price.append(i)

        #time.sleep(2)

    for i in addresses:
        i = i.text
        address.append(i)

        #time.sleep(2)

    for i in sizes:
        i = i.text
        size.append(i)
    try:
        next_page = driver.find_element(By.XPATH, '//a[@rel="next"]')
        next_page.click()
    except:
        pass
    h += 1
    #time.sleep(2)




info = pd.DataFrame({'price':price,'address':address,'size':size})
info.to_csv('realestateprices.csv',index=False)
print(info)

driver.quit()