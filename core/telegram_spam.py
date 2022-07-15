"""
╔═════════════════════════════════════════════════════════════════════════════════╗
║                                                                                 ║
║                                     Beast bomber                                ║
║  Author:                                                                        ║
║  https://github.com/ebankoff                                                    ║
║                                                                                 ║
║  The author of this program is not responsible for its use!                     ║
║  When posting this code on other resources, please indicate the author!         ║
║                                                                                 ║
║                               All rights reserved.                              ║
║                           Copyright (C) 2022 ebankoff                           ║
║                                                                                 ║
╚═════════════════════════════════════════════════════════════════════════════════╝
"""

import time
import random
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


def telegram(name, count, msg, cn, prx):
	if prx == 'yes':
		proxy = []
		with open(r"input/proxies.txt", "r", encoding="utf-8") as file:
			for line in file:
				proxy.append(line)

		proxy = [line.rstrip() for line in proxy]

		PROXY = str(random.choice(proxy))

		chrome_options = Options()
		chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
		chrome_options.add_experimental_option('useAutomationExtension', False)
		chrome_options.add_experimental_option('prefs', {
			'profile.default_content_setting_values.notifications': 2,
			'credentials_enable_service': False,
			'profile': {
				'password_manager_enabled': False
			}
		})
		chrome_options.add_argument("--disable-popup-blocking")
		driver = webdriver.Chrome(chromedriver.install(), chrome_options=chrome_options)
		driver.set_window_size(1200, 700)

		webdriver.DesiredCapabilities.CHROME['proxy']={
		    "httpProxy":PROXY,
		    "ftpProxy":PROXY,
		    "sslProxy":PROXY,
		    
		    "proxyType":"MANUAL",
		    
		}

		stealth(driver,
			languages=["en-US", "en"],
			vendor="Google Inc.",
			platform="Win32",
			webgl_vendor="Intel Inc.",
			renderer="Intel Iris OpenGL Engine",
			fix_hairline=True,
		)

		driver.get("https://web.telegram.org/k/")

		search = WebDriverWait(driver, 35).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='telegram-search-input']")))
		time.sleep(8)
		search.send_keys(name)
		time.sleep(2)
		driver.refresh()
		time.sleep(2)
		search = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='telegram-search-input']")))
		search.send_keys(name)

		action = ActionChains(driver)
		action.send_keys(Keys.TAB)
		time.sleep(1)
		action.send_keys(Keys.TAB)
		time.sleep(1)
		action.send_keys(Keys.ENTER)
		action.perform()

		msgBox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='editable-message-text']")))

		for i in range(count):
			try:
				msgBox.send_keys(msg, Keys.ENTER)
				cn+=1
				print("\033[32m {}" .format(f'ATTACKING') + "\033[37m {}" .format('|') + "\033[36m {}" .format(str(cn)) + "\033[37m {}" .format('|') + "\033[35m {}" .format(name))
			except:
				cn+=1
				print("\033[32m {}" .format(f'ATTACKING') + "\033[37m {}" .format('|') + "\033[36m {}" .format(str(cn)) + "\033[37m {}" .format('|') + "\033[35m {}" .format(name))

		print("\033[32m {}" .format("Success!"))
		print(f"{cn} messages were sent to {name}")

	else:
		chrome_options = Options()
		chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
		chrome_options.add_experimental_option('useAutomationExtension', False)
		chrome_options.add_experimental_option('prefs', {
			'profile.default_content_setting_values.notifications': 2,
			'credentials_enable_service': False,
			'profile': {
				'password_manager_enabled': False
			}
		})
		chrome_options.add_argument("--disable-popup-blocking")
		driver = webdriver.Chrome('core/chromedriver', chrome_options=chrome_options)
		driver.set_window_size(1200, 700)

		stealth(driver,
			languages=["en-US", "en"],
			vendor="Google Inc.",
			platform="Win32",
			webgl_vendor="Intel Inc.",
			renderer="Intel Iris OpenGL Engine",
			fix_hairline=True,
		)

		driver.get("https://web.telegram.org/k/")

		search = WebDriverWait(driver, 35).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='telegram-search-input']")))
		time.sleep(8)
		search.send_keys(name)
		time.sleep(2)
		driver.refresh()
		time.sleep(2)
		search = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='telegram-search-input']")))
		search.send_keys(name)

		action = ActionChains(driver)
		action.send_keys(Keys.TAB)
		time.sleep(1)
		action.send_keys(Keys.TAB)
		time.sleep(1)
		action.send_keys(Keys.ENTER)
		action.perform()

		msgBox = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='editable-message-text']")))

		for i in range(count):
			try:
				msgBox.send_keys(msg, Keys.ENTER)
				cn+=1
				print("\033[32m {}" .format(f'ATTACKING') + "\033[37m {}" .format('|') + "\033[36m {}" .format(str(cn)) + "\033[37m {}" .format('|') + "\033[35m {}" .format(name))
			except:
				cn+=1
				print("\033[32m {}" .format(f'ATTACKING') + "\033[37m {}" .format('|') + "\033[36m {}" .format(str(cn)) + "\033[37m {}" .format('|') + "\033[35m {}" .format(name))

		print("\033[32m{}" .format("\nSuccess!"))
		print(f"{cn} messages were sent to {name}")