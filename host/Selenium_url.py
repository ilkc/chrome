from tabnanny import check
from selenium.webdriver.common.by import By
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import time
import json
import re
from bs4 import BeautifulSoup
import os
import time
from urllib import request
from urllib.error import HTTPError
import virust_file as vi
import url_virus as urlvi

url = "https://www.kisa.or.kr/401/form?postSeq=2912&page=2"
#url = "https://www.mokpo.ac.kr/planweb/board/view.9is?pBoardId=BBSMSTR_000000000101&contentUid=4a94e3926d1a8834016d66a5f49a36ac&boardUid=4a94e3926f265c99016fd11bb7137b59&categoryUid1=0&nowPageNum=1&dataUid=4a94e3926cad5966016cadc4d5cd001c&nttId=848968"
#url = "https://www.kisa.or.kr/401/form?postSeq=2916&page=2"
#url = "https://kin.naver.com/qna/detail.naver?d1id=1&dirId=102020101&docId=415372793&qb=7LKo67aA7YyM7J28&enc=utf8&section=kin.ext&rank=1&search_sort=0&spq=0"
#url = "https://ipsi.mokpo.ac.kr/planweb/board/view.9is?dataUid=4a94e3926cad5966016cadc4d5cd001c&nttId=845138&boardUid=4a94e3926cb3823a016cb78d7336021f&contentUid=4a94e3926cb382ab016cb6ca44310023&layoutUid=&searchType=&keyword=&nowPageNum=1&categoryUid1=0"

#urlvi.url_vi()
url = urlvi.url_vi()
print(url)

global check_dynamic
r = requests.get(url)
os.chdir('file')
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("headless")
options.add_argument("disable-gpu")
options.add_argument("lang=ko_KR")
options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\Users\hatae\OneDrive\바탕 화면\목대\강의\창공\Selenium_url_in\file",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

driver = webdriver.Chrome("C:\work\chromedriver.exe", options=options)
driver.implicitly_wait(200)
driver.get(url)
driver.maximize_window()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
count = 1


def bs4_down(inp_tag, name):
    try:
        request.urlretrieve(inp_tag, name)
    except HTTPError as e:
        pass

def file_extention(driver, extention, name, inp_tag):
    num = name.find(extention)
    try:
        print(check_dynamic)
        if(check_dynamic == 1):
            click = driver.find_element(By.LINK_TEXT,name)
            click.click()
            time.sleep(1)
    except:
        pass
    name = name[0:num+ len(extention)]
    #print(name)
    bs4_down(inp_tag, name)       


for f in soup.find_all('a'):
    try:
        inp_tag = f.get('href')
        #inp_tag = f.find('href')
        #inp_tag = f.get_attribute("href")
        #print(inp_tag)
        #name = soup.find("a", attrs={'href':inp_tag}).text
        #print(name)
        if(inp_tag == "#"):
            continue
        if(inp_tag[0:10] == "javascript"):
            continue
        if(inp_tag[0:1] == "/"):
            if(url[-1] == "/"):
                url = url.strip("/")    
            inp_tag = url + inp_tag
        if(inp_tag[-2]+inp_tag[-1] == "do"):
            continue
        if(inp_tag[-3] + inp_tag[-2]+inp_tag[-1] == "php"):
            continue
        if(inp_tag[-4] + inp_tag[-3] + inp_tag[-2]+inp_tag[-1] == "html"):
            continue

        name = f.text
        if(name.find("pdf") > 0):
            if(len(str(f.get('onclick'))) > 4):
                check_dynamic = 1
            else:
                check_dynamic = 0
            file_extention(driver, "pdf", name, inp_tag)         
        if(name.find("jpg") > 0):
            if(len(str(f.get('onclick'))) > 4):
                check_dynamic = 1
            else:
                check_dynamic = 0
            file_extention(driver, "jpg", name, inp_tag)
        if(name.find("hwp") > 0):
            if(len(str(f.get('onclick'))) > 4):
                check_dynamic = 1
            else:
                check_dynamic = 0
            file_extention(driver, "hwp", name, inp_tag)
        if(name.find("png") > 0):
            if(len(str(f.get('onclick'))) > 4):
                check_dynamic = 1
            else:
                check_dynamic = 0
            file_extention(driver, "png", name, inp_tag)
        if(name.find("xlsx") > 0):
            if(len(str(f.get('onclick'))) > 4):
                check_dynamic = 1
            else:
                check_dynamic = 0
            file_extention(driver, "xlsx", name, inp_tag)
        if(name.find("zip") > 0):
            if(len(str(f.get('onclick'))) > 4):
                check_dynamic = 1
            else:
                check_dynamic = 0
            file_extention(driver, "zip", name, inp_tag)
        if(name.find("ps1") > 0):
            if(len(str(f.get('onclick'))) > 4):
                check_dynamic = 1
            else:
                check_dynamic = 0
            file_extention(driver, "ps1", name, inp_tag)
        if(name.find("py") > 0):
            if(len(str(f.get('onclick'))) > 4):
                check_dynamic = 0
            else:
                check_dynamic = 1
            file_extention(driver, "py", name, inp_tag)
        if(name.find("exe") > 0):
            if(len(str(f.get('onclick'))) > 4):
                check_dynamic = 0
            else:
                check_dynamic = 1
            file_extention(driver, "exe", name, inp_tag)
        
    except:
        pass


driver.quit()

time.sleep(2)


vi.virus_file()
