# Add gmail cookie to each session to make captcha much easier to solve
# after bypass spalsh, copy hmac cookie. (contains ip and useragent) might help to bypass again. (using same ip)
# need multiple emails
# wait until captcha box is loaded, then alert!
# export and add gmail cookies like an hour before
# copy cookie once validated 10 minutes

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import json, time, os
import threading
from threading import Thread

f = open("gcookie.json", "r")
data = f.read()
gcookie = json.loads(data)

bproxies = ["191.96.37.242:3128", \
            "191.96.244.26:3128", \
            "191.96.244.199:3128",\
            "191.96.62.134:3128", \
            "191.96.48.88:3128", \
            "191.96.62.44:3128", \
            "191.96.48.198:3128", \
            "191.96.48.194:3128", \
            "191.96.37.250:3128", \
            "191.96.37.244:3128", \
            "191.96.48.202:3128", \
            "191.96.62.228:3128", \
            "191.96.244.100:3128", \
            "191.96.62.71:3128", \
            "191.96.244.142:3128", \
            "191.96.62.168:3128", \
            "191.96.62.180:3128", \
            "191.96.244.227:3128", \
            "191.96.37.234:3128", \
            "191.96.48.165:3128", \
            "191.96.37.54:3128", \
            "191.96.48.236:3128", \
            "191.96.48.74:3128", \
            "191.96.62.55:3128"\
           ]

cproxies = ["52.71.71.243:38750",\
            "52.71.71.243:38751",\
            "52.71.71.243:38752",\
            "52.71.71.243:38753",\
            "52.71.71.243:38754",\
            "52.71.71.243:38755",\
            "52.71.71.243:38756",\
            "52.71.71.243:38757",\
            "52.71.71.243:38758",\
            "52.71.71.243:38759",\
            "52.71.71.243:38760",\
            "52.71.71.243:38761",\
            "52.71.71.243:38762",\
            "52.71.71.243:38763",\
            "52.71.71.243:38764",\
            "52.71.71.243:38765",\
            "52.71.71.243:38766",\
            "52.71.71.243:38767",\
            "52.71.71.243:38768",\
            "52.71.71.243:38769",\
            "52.71.71.243:38770",\
            "52.71.71.243:38771",\
            "52.71.71.243:38772",\
            "52.71.71.243:38773",\
            "52.71.71.243:38774"\
            ]

freeproxies = ["74.207.250.191:3128","165.227.165.197:80","35.200.115.50:3128","67.203.151.77:3128", "192.240.150.133:8080"]
freeproxies2 = ["35.193.170.34:3128","35.185.110.28:3128","144.217.160.111:3128"]

windows=[]

for proxy in cproxies:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % proxy)

    chrome = webdriver.Chrome(chrome_options=chrome_options)
    chrome.get("http://www.adidas.com/yeezy")
#    chrome.execute_script("$(window.open('http://gmail.com'))")

    windows.append(chrome)

time.sleep(5)

for chrome in windows:
    chrome.set_window_size(500, 800)

#while True:
#    for chrome in windows:
#        try:
#            chrome.find_element_by_xpath("//div[@id='g-recaptcha']/div/div")
#            os.system('say "Alert, captcha detected"')
#        except NoSuchElementException:
#            os.system(®'say "no captcha"')



# for cookie in gcookie:
#    chrome.add_cookie(cookie)
# time.sleep(10)
# chrome.get("https://www.google.com/recaptcha/api2/demo")
