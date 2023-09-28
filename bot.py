from seleniumwire import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as ex
import time
import os
from collections import Counter
from fake_useragent import UserAgent
import numpy as np
import re
import random

# the interceptor function is used to set the request headers
def interceptor(request):
    # delete the "User-Agent" header and
    # set a new one
    del request.headers["user-agent"]  # Delete the header first
    del request.headers["sec-ch-ua"]  # Delete the header first
    del request.headers["sec-ch-ua-platform"]  # Delete the header first
    request.headers["user-agent"] = uagent
    # set the "Sec-CH-UA" header
    request.headers["sec-ch-ua"] = sec
    # set the "referer" header
    # request.headers["referer"] = referer
    request.headers["sec-ch-ua-platform"] = os
    request.headers["sec-fetch-mode"] = "navigate"
    request.headers["sec-fetch-user"] = "?1"
    request.headers["sec-ch-ua-mobile"] = "?0"
    request.headers["accept-Language"] = language
    request.headers["accept-Encoding"] = encoding
    request.headers["accept"] = accept
    request.headers["upgrade-insecure-requests"] = "1"

# this function get the browser name from the generated random user agent
def get_browser(agent):
    if 'Chrome/' in agent and 'Edg/' not in agent:
        browser = 'Chrome'
    elif 'Safari/' in agent and 'Chrome/' not in agent:
        browser = 'Safari'
    elif 'Firefox/' in agent:
        browser = 'Firefox'
    elif 'Edg/' in agent:
        browser = 'Edge'
    return browser

# this function get the sec-ch-ua from the generated random user agent
def get_sec(browser, user):
    if browser == 'Chrome':
        ver = get_ver(user)
        sec = f'"Google Chrome";v={ver}, "Not;A=Brand";v="8", "Chromium";v={ver}'
    elif browser == 'Edge':
        ver = get_ver(user)
        sec = f'"Microsoft Edge";v={ver}, "Not;A=Brand";v="8", "Chromium";v={ver}'
    return sec

# this function get the browser version from the generated random user agent
def get_ver(user):
    # Define a regular expression pattern to match the version number after "Chrome/"
    try:
        pattern = r'Chrome/(\d+\.\d+\.\d+\.\d+)'
        match = re.search(pattern, user)
    except:
        pattern = r'Edg/(\d+\.\d+\.\d+\.\d+)'
        match = re.search(pattern, user)

    if match:
        v = match.group(1)
        ver = v.split('.')[0]
    return ver

# this function get the operating system from the generated random user agent
def get_os(agent):
    if 'Windows' in agent:
        os = 'windows'
    elif 'Mac' in agent:
        os = 'Macintosh'
    elif 'Linux' in agent:
        os = 'Linux'
    return os
  
# this function uses windscribe vpn for proxy rotation to bypass rate limiting, external proxies can also be used. 
def vpn(action, location=None):
    w_path = r"C:\\Program Files\\Windscribe\\Windscribe-cli.exe"
    if location is None:
        command = f'"{w_path}" {action}'
    else:
        command = f'"{w_path}" {action} {location}'
    os.system(command)

def b_1():
    b = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div[2]/div[2]/div[2]/button')
    return b

def b_2():
    b = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div[2]/div[2]/div[2]/button[2]')
    return b

# function to get the appointment dates
def get_dates():
    b1 = b_1() 
    while True:
        t_group = driver.find_element(By.XPATH, '//*[@class="tls-time-group"]')
        dates = t_group.find_elements(By.XPATH, './/*[@class="tls-time-group--slot"]')
        for date in dates:
            dt =  date.find_element(By.XPATH, './/*[@class="tls-time-group--header-title"]').text
            try:
                avail = date.find_element(By.XPATH, ".//*[@class='tls-time-unit  -available']")
                available_dates.append(dt)
            except:
                try:
                    avail = date.find_element(By.XPATH, ".//*[@class='tls-time-unit  -available -prime']")
                    available_dates.append(dt)
                except:
                    continue
            time.sleep(2)
        try:
            b_2().click()
        except:
            try:
                b1.click()
                b1 = False
            except:
                break


while True:
# windscribe free servers list
    connect_list = ["Atlanta Mountain", "Dallas Ranch",  "Chicago Cub", "Miami Snow", "Miami Vice", 
                    "New York Empire", "New York Grand Central", "Washington DC Precedent", "Los Angeles Dogg",
                    "seattle Cobain", "Montreal Expo 67", "Toronto Comfort Zone", " Toronto The 6",
                    "Vancouver Granville", "Vancouver Vansterdam", "Paris Seine", "Paris Jardin", "Amsterdam Canal", 
                    "Amsterdam Red Light", "Amsterdam Tulip", "Oslo Fjord", "Zurich Alphorn", "Zurich Lindenhof",
                    "London Crumpets", "London Custard", "Istanbul Lygos", "Hong Kong Phooey", "Hong Kong Victoria",
                    ""]
    loca = random.choice(connect_list)
    vpn("connect", loca)
    # time.sleep(5)

# if using proxy api like scraper api or zenrows
    # API_KEY = ''
    # s_options = {
    #     'proxy': {
    #         'http': f'http://scraperapi:{API_KEY}@proxy-server.scraperapi.com:8001',        
    #         'https': f'http://scraperapi:{API_KEY}@proxy-server.scraperapi.com:8001',
    #         'verify_ssl': True,
    #     },
    # }


    accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    encoding = "gzip, deflate, br"
    language = "en-GB,en-US;q=0.9,en;q=0.8"
    referer = "https://visas-fr.tlscontact.com/visa/gb"

    # random user agent generation to avoid bot detection
    uagent = UserAgent().random

    # tls username and password
    username =
    password = 

    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    driver = uc.Chrome(options=chrome_options, use_subprocess=True)

    brow = get_browser(uagent)
    if brow == 'Chrome' or brow == 'Edge':
        sec = get_sec(brow, uagent)
        ver = get_ver(uagent)
    else:
        sec = None
    os = get_os(uagent)

    driver.request_interceptor = interceptor
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.maximize_window()
    wait = WebDriverWait(driver, 200)

    try:
        driver.get("https://visas-fr.tlscontact.com/visa/gb/gbLON2fr/home")
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Login"]')))
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[text()="Login"]').click()
        element = driver.find_element(By.XPATH, '//input[@name="username"]')
        time.sleep(3)
        element.send_keys(username)
        element = driver.find_element(By.XPATH, "//input[@name='password']")
        element.send_keys(password)
        element.send_keys(Keys.RETURN)
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="My Application"]'))).click()
        time.sleep(5)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="tls-button-primary button-neo-inside"]'))).click()

        js_code = "arguments[0].scrollIntoView();"
        scroll = driver.find_element(By.XPATH, '//*[@class="button-neo-inside -primary"]')
        driver.execute_script(js_code, scroll)
        js_scroll = "window.scrollBy(0, 1200);"
        driver.execute_script(js_scroll)

        time.sleep(2)

        available_dates = []

        get_dates()

        if len(available_dates) == 0:
            print("No dates available!!!")
        else:
            print(available_dates)
    except:
        pass

    driver.quit()
    vpn("disconnect")

    # to run the code every 5 minutes
    time.sleep(300)
