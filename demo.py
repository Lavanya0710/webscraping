import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(service=Service(chromedriver_autoinstaller.install()))
driver.maximize_window()
driver.get("https://www.mynextmove.org/")
assert "My Next Move" in driver.title
time.sleep(1)
dataDictionary = {}
# m = 1

elements=driver.find_element(By.ID,"c")
drp=Select(elements)
all_options=drp.options
drp_ele=[]
for option in all_options:
    a=option.text
    drp_ele.append(a)


def CareerByIndustry(b):
    DropDown_elements=driver.find_elements(by=By.TAG_NAME,value="option")
    i = 0
    while i < len(DropDown_elements):

        if(DropDown_elements[i].text==b):
            DropDown_elements[i].click()
        i = i + 1

    Browse = driver.find_element(By.XPATH, "//tbody/tr[2]/td[3]/form[1]/div[2]/input[1]")
    driver.execute_script("arguments[0].click()", Browse)
    datas = driver.find_elements(By.XPATH, "//tbody/tr/td/a")
    data = []
    for i in datas:
        j = i.text
        data.append(j)

    dataDictionary[b] = data
    driver.back()

for k in drp_ele:
    CareerByIndustry(k)
    # m = m + 1
    # if m == 4:
    #     break

with pd.ExcelWriter(r'F:\WebScraping\ExatactData.xlsx') as writer:
    for key, value in dataDictionary.items():
        dataFrame = pd.DataFrame({key: value})
        sht_name = ''.join(filter(str.isalnum, key))
        dataFrame.to_excel(writer, sheet_name=sht_name, index=False)
driver.quit()
