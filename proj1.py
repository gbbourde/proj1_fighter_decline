import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def fighter_page():
    driver = webdriver.Chrome('/Users/mcmlxviii/Documents/NYCDS Academy/PROJECT_1/chromedriver')
    driver.get('https://www.tapology.com/fightcenter/fighters/daniel-cormier')

    driver.fullscreen_window()

    driver.implicitly_wait(2)

    records = driver.find_elements_by_xpath("//div[@class='result']")
    fight_record = [rec.text for rec in records]

    fight_record = [i.split('\n') for i in fight_record]
    return fight_record

fighter = fighter_page()


import re
def get_next_fighter(name):
    driver = webdriver.Chrome('/Users/mcmlxviii/Documents/NYCDS Academy/PROJECT_1/chromedriver')
    driver.get('https://www.tapology.com/fightcenter/fighters/miesha-tate-takedown')

    driver.fullscreen_window()

    driver.implicitly_wait(2)

    input=driver.find_element_by_id("siteSearch")
    name = re.sub(r'[^A-Za-z ]',' ',name.lower())
    fighter = name
    print(fighter)

    input.send_keys( fighter )
    input.send_keys(Keys.ENTER)

    driver.implicitly_wait(2)

    # THE div w/class name of 'blah' then the table followed by // which means the 
    # nested occurrence of tr then td
    rows = driver.find_elements_by_xpath("//div[@class='searchResultsFighter']/table//tr/td/a")
    next_fighter = [row.get_attribute("href") for row in rows]
    
    # EMPTY STRINGS ARE FALSY
    if not next_fighter[0]:
        return None
    return next_fighter[0]

    driver.close()
    print( next_fighter )

