#from urllib.request import urlopen as uReq
#import urllib.parse
#from bs4 import BeautifulSoup as soup

import requests


#x = urllib.request.urlopen('https://pythonprogramming.net')


#print(x.read())
try:

    #Actually login
    with requests.Session() as c:
        url = 'https://www.activistshorts.com/users/sign_in'
        USERNAME = 'bbliss@sandiego.edu'
        PASSWORD = 'fsu-stu712bb'
        login_page = c.get(url,verify=False)
        website_token = c.cookies['_stealthystealth_session']
        print(website_token)
        headers = login_page.headers
        print(headers)

        print(login_page.content)
        print(login_page.status_code)

        #Continue trying to fix this
        login_data = {'authenticity_token': website_token, 'user[email]': USERNAME, 'user[password]': PASSWORD,
                      'user[remember_me]': 0, 'commit': 'Sign In', 'utf8' : 1}
        first_page = c.post(url, data=login_data, headers = headers)
        print(first_page.content)
        print(first_page.status_code)
        #After loginURL
        #next_page = c.post('https://www.activistshorts.com/dashboard')

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
