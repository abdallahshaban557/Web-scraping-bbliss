#from urllib.request import urlopen as uReq
#import urllib.parse
from bs4 import BeautifulSoup

import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


#x = urllib.request.urlopen('https://pythonprogramming.net')



try:

    #Stop remember me from showing up
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', {
        'credentials_enable_service': False,
        'profile': {
            'password_manager_enabled': False
        }
    })


    #Open the chrome driver, and navigate to the page
    driver = webdriver.Chrome("chromedriver/chromedriver.exe",chrome_options=chrome_options)
    driver.get("https://www.activistshorts.com/users/sign_in")

    #Isolate the input fields, and insert data to form
    USERNAME = driver.find_element_by_css_selector('#user_email')
    USERNAME.send_keys('bbliss@sandiego.edu')
    PASSWORD = driver.find_element_by_css_selector('#user_password')
    PASSWORD.send_keys('fsu-stu712bb')
    LOGIN = driver.find_element_by_xpath("//input[@value='Sign in']")

    #Submit Data
    LOGIN.click()

    #navigate to search result - remember to implement loop here
    driver.get("https://www.activistshorts.com/search/results?company%5Btickers%5D=VRX")
    time.sleep(3)

    #Get to the last required page
    link_to_search_result = driver.find_element_by_css_selector(".tablesorter td:nth-child(1)")
    link_to_search_result.click()
    time.sleep(3)

    #Synopsis copy
    time.sleep(3)
    synopsis = driver.find_element_by_css_selector(".synopsis p")
    print(synopsis.text)

    #Bottom links counter
    documents_table = driver.find_elements_by_xpath("//*[@id='203']/div/div[4]/div/div/div[8]/div/table/tbody/tr")

    size_documents_table = len(documents_table)
    time.sleep(3)
    print(size_documents_table)

    # #Actually login
    # with requests.Session() as c:
    #     #Initial login page info setup
    #     url = 'https://www.activistshorts.com/users/sign_in'
    #     USERNAME = 'bbliss@sandiego.edu'
    #     PASSWORD = 'fsu-stu712bb'
    #
    #     #Login page call - HTML cleanup and hidden token extraction
    #     login_page = c.get(url,verify=False)
    #     login_page_html = BeautifulSoup(login_page.text, "lxml")
    #     website_token= login_page_html.find_all('input', {'name': 'authenticity_token'})[0]['value']
    #
    #     login_data = {'authenticity_token': website_token, 'user[email]': USERNAME, 'user[password]': PASSWORD, 'user[remember_me]': 0,'user[remember_me]': 0, 'commit': 'Sign In', 'utf8' : '&#x2713'}
    #     #login_data = dict(utf8='&#x2713', authenticity_token=website_token, user[email]=USERNAME, user[password]=PASSWORD,user[remember_me]=0,user[remember_me]=1,commit='Sign in')
    #     first_page = c.post(url, data=login_data, headers={"Referer": "http://www.google.com"})
    #
    #     # Dashboard URL call
    #     #dashboard_url = 'https://www.activistshorts.com/search/results?company%5Btickers%5D=VRX'
    #
    #     user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'
    #     headers = {'User-Agent': user_agent}
    #
    #
    #     search_url = 'https://www.activistshorts.com/companies/203/campaigns/1018'
    #     search_url = c.get(search_url, verify=False, headers=headers)
    #     search_url_soup = BeautifulSoup(search_url.text, 'html.parser')
    #     print(search_url_soup.prettify())

except Exception as e:
    print(str(e))







#
#     MyURL = 'https://www.activistshorts.com/users/sign_in'
#
#     #Grabbing page
#     uClient = uReq(MyURL)
#
#     page_html = uClient.read()
#
#     uClient.close()
#
#     #HTML Parsing
#     page_soup = soup(page_html, "html.parser")
#
#     #Grab individual inputs
#     username = page_soup.findAll("input", {"type": "email"})
#     username_id = username[0]["id"]
#     print(username_id)
#     print(username)
#     password = page_soup.findAll("input",{"type":"password"})
#     print(password)
#     hidden_input = page_soup.findAll("input",{"type":"hidden"})
#     print(hidden_input)
#
#     url= 'https://www.google.com?q=test'
#
#     headers = {}
#     headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
#     req = urllib.request.Request(url, headers=headers)
#     resp = urllib.request.urlopen(req)
#     respData = resp.read()
#
#     saveFile = open('withHeaders.txt', 'w')
#     saveFile.write(str(respData))
#     saveFile.close()
#
