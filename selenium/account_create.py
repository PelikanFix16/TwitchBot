from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import string
import random
from selenium.webdriver.support.ui import Select
import asyncio
from proxybroker import Broker
from selenium.webdriver.common.proxy import Proxy, ProxyType
import os
import signal
from random import randint
import names
from selenium.webdriver.common.keys import Keys
import requests
x1 = random.randint(1,101)
x2 = random.randint(1,101)


n = names.get_first_name(gender='male')

username = 0

if random.choice([True, False]):
    if random.choice([True, False]):

        username = str(x1)+n+"_"+str(x2)
        if random.choice([True, False]):
            username = str(x1)+"_"+str(x2)+n+str(x1)
        else:
            username = str(x2)+n+"_"+str(x1)+"_"
    else:
        username = str(x2)+n+"_"+str(x2)
else:
    username = str(x2)+n+str(x1)+str(x2)



'''
prox1 = ""

async def show(proxies):
    global prox1
    while True:
        proxy = await proxies.get()
        if proxy is None: break
        prox1 = proxy.as_json()['host']+":"+str(proxy.as_json()["port"])



proxies = asyncio.Queue()
broker = Broker(proxies)
tasks = asyncio.gather(
    broker.find(types=['HTTPS'], limit=1),
    show(proxies))

loop = asyncio.get_event_loop()
loop.run_until_complete(tasks)


prox = Proxy()
prox.proxy_type = ProxyType.MANUAL

prox.ssl_proxy = prox1

capabilities = webdriver.DesiredCapabilities.CHROME
prox.add_to_capabilities(capabilities)
'''



def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension('./f.zip')
chrome_options.add_argument("--window-size=1000,700")
chrome_options.add_argument("--mute-audio")
driver = webdriver.Chrome('./chromedriver',options=chrome_options)#,desired_capabilities=capabilities)

try:
    driver.get('https://www.twitch.tv/')
except:

    os.kill(os.getppid(), signal.SIGHUP)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.minuteinbox.com/")
time.sleep(5)
#email = driver.find_element(By.CSS_SELECTOR,"input[class*='form-control']").get_attribute("value")
#email = driver.find_element_by_id("inputEmail3").get_attribute("value")
email = driver.find_element_by_id("email").get_attribute("innerHTML")

driver.switch_to.window(driver.window_handles[0])

time.sleep(12)
loginDiv = 0

password = randomString()

element = driver.find_element(By.XPATH,"//*[@data-a-target='signup-button']")
element.click()


try:
    loginDiv = driver.find_element(By.XPATH,"//*[@data-a-target='signup-username-input']")
except:
    try:
        loginDiv = driver.find_element(By.XPATH,"//*[@data-a-target='tray-input']")
    except:
        os.kill(os.getppid(), signal.SIGHUP)
try:
    loginInput = loginDiv.find_element_by_tag_name("input")
    loginInput.send_keys(username)
except:
    try:
        os.kill(os.getppid(), signal.SIGHUP)
    except:
        pass
    os.kill(os.getppid(), signal.SIGHUP)
passwordDiv = driver.find_element(By.XPATH,"//*[@data-a-target='signup-password-input']")
passwordInput = passwordDiv.find_element_by_tag_name("input")
passwordInput.send_keys(password)
select = Select(driver.find_element(By.XPATH,"//*[@data-a-target='birthday-month-select']"))
select.select_by_value("1")
brihDiv = driver.find_element(By.XPATH,"//*[@data-a-target='birthday-date-input']")
brihInput = brihDiv.find_element_by_tag_name("input")
brihInput.send_keys("12")
yearDiv = driver.find_element(By.XPATH,"//*[@data-a-target='birthday-year-input']")
yearInput = yearDiv.find_element_by_tag_name("input")
yearInput.send_keys("1999")
emailDiv = driver.find_element(By.XPATH,"//*[@data-a-target='signup-email-input']")
emailInput = emailDiv.find_element_by_tag_name("input")
emailInput.send_keys(email)

time.sleep(2)
registerBtn = driver.find_element(By.XPATH,"//*[@data-a-target='passport-signup-button']")
registerBtn.click()
time.sleep(3)
try:
    time.sleep(12)

    for i in range(10):
        try:
            driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[i])
            time.sleep(1)
            try:
                driver.find_element_by_id("recaptcha-verify-button")
                driver.quit()
                os.kill(os.getppid(), signal.SIGHUP)
            except:
                pass
            try:
                #div[class*='rc-doscaptcha-header-text']
                email = driver.find_element(By.CSS_SELECTOR,"//div[@class='rc-doscaptcha-header-text']")
                driver.quit()
                os.kill(os.getppid(), signal.SIGHUP)
            except:
                pass


        except:
            pass


    raise Exception('spam', 'eggs')

except Exception as e:
    print(str(e))

time.sleep(9)
driver.get("https://twitchapps.com/tmi/")
time.sleep(6)
try:
    driver.find_element_by_class_name("btn").click()
except:
    try:
        driver.quit()
    except:
        os.kill(os.getppid(), signal.SIGHUP)
    os.kill(os.getppid(), signal.SIGHUP)
time.sleep(5)
try:
    driver.find_element_by_class_name("js-authorize").click()
except:
    os.kill(os.getppid(), signal.SIGHUP)
time.sleep(5)
val = driver.find_element_by_id("tmiPasswordField").get_attribute("value")
dic = {"username":username,"password":password,"email":email,"oauth":val}
with open("dict.txt","a") as f:
    f.write(str(dic)+"\n")
driver.switch_to.window(driver.window_handles[1])
#driver.find_element(By.CSS_SELECTOR,"a[href*='wiadomosc1']").click()
driver.get("https://www.minuteinbox.com/window/id/2")
#//a[contains(@href, 'key_word')]

time.sleep(2)

frameD = driver.find_element_by_id("iframeMail")
driver.switch_to.frame(frameD)


lA = driver.find_elements_by_tag_name('a')

driver.get(lA[1].get_attribute("href"))

time.sleep(5)
os.kill(os.getppid(), signal.SIGHUP)
