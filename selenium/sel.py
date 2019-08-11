import time
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType


lines = 0
with open("raw.txt") as f:
    lines = f.readlines()
ip = "https://www.twitch.tv/inqu_"
for i in lines:

    prox = Proxy()
    prox.proxy_type = ProxyType.MANUAL
    prox.ssl_proxy = i

    capabilities = webdriver.DesiredCapabilities.CHROME
    prox.add_to_capabilities(capabilities)

    driver = webdriver.Chrome("./chromedriver",desired_capabilities=capabilities)
    driver.get(ip);
