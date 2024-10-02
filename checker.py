from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException 

def get_rank():
	user_code = input("Enter user code: ")
	while '#' not in user_code:
		user_code = input("Enter user code: ")
	user_code = user_code.split('#')

	chrome_options = Options()
	chrome_options.add_argument("--headless")

	driver = webdriver.Chrome(options=chrome_options)
	driver.get(f'https://www.slippi.gg/user/{user_code[0]}-{user_code[1]}')

	try:
		name = WebDriverWait(driver, 2).until(
			EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div/div[1]/p[1]'))
		)
		rank = WebDriverWait(driver, 2).until(
			EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div/div/p[3]'))
		)
		elo = WebDriverWait(driver, 2).until(
			EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div/div/p[4]'))
		)
		print(name.text)
		print(rank.text)
		print(elo.text)
	except TimeoutException:
		print('User not found')

	driver.close()
	get_rank()	

get_rank()