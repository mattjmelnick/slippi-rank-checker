from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.slippi.gg/user/mjm-939")
print(driver.title)
driver.quit()