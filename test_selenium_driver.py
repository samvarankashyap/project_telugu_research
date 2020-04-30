from time import sleep
from selenium import webdriver
import os  
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  
import html2text
chrome_options = Options()  
chrome_options.add_argument("--headless")  


browser = webdriver.Chrome(
        executable_path=os.path.abspath("chromedriver"),
        options=chrome_options
        )

browser.get('http://www.andhrabharati.com/dictionary/')


textbox = browser.find_element_by_id("strSearch")
telugu_word = "తెలుపు"
textbox.send_keys(telugu_word)
sleep(1)
searchbtn =  browser.find_element_by_id("button2")
searchbtn.click()
sleep(2)
#search_results = browser.find_element_by_id("content")
search_results = browser.find_element_by_id("content")
#tstring = search_results.get_attribute('innerHTML')
tstring = search_results.text
#tstring = html2text.html2text(tstring)
open("1.txt","w").write(tstring)
sleep(5)

