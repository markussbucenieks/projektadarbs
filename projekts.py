from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def get_links():
    find8 = driver.find_elements(By.CSS_SELECTOR, "[id^='dm_']")
    links = [element.get_attribute("href") for element in find8]
    return links

def save_links_to_file(links, filename="result2.txt"):
    with open(filename, "a", encoding="utf-8") as file:
        for link in links:
            file.write(link + "\n")

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

while True:
    url = "https://www.ss.lv/"
    driver.get(url)
    time.sleep(1)

   
    find = driver.find_element(By.ID, "mtd_97")
    find.click()
    time.sleep(1)

    find2 = driver.find_element(By.ID, "ahc_144")
    find2.click()
    time.sleep(2)

    find3 = driver.find_element(By.ID, "f_o_18_min")
    select = Select(find3)
    time.sleep(1)
    select.select_by_value("2010")

    find4 = driver.find_element(By.ID, "f_o_15_min")
    select1 = Select(find4)
    time.sleep(1)
    select1.select_by_value("2.0")

    find5 = driver.find_element(By.ID, "f_o_34")
    select2 = Select(find5)
    time.sleep(1)
    select2.select_by_visible_text("Benzīns")

    find6 = driver.find_element(By.ID, "f_o_35")
    select3 = Select(find6)
    time.sleep(1)
    select3.select_by_visible_text("Manuāla")
    time.sleep(1)

    find7 = driver.find_element(By.CLASS_NAME, 'a18')
    find7.click()
    time.sleep(1)

    new_links = get_links()

    with open("result.txt", "r", encoding="utf-8") as file:
        existing_links = file.read().splitlines()

    new_links = set(new_links) - set(existing_links)

    save_links_to_file(new_links)

    print("Jauni URL pievienoti")
    time.sleep(3 * 60 * 60)  
