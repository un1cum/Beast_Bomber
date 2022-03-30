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
from selenium.webdriver.support import expected_conditions as EC


def whatsapp(name, count, msg, cn, prx):
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
			'credentials_enable_service': False,
			'profile': {
				'password_manager_enabled': False
			}
		})
		chrome_options.add_argument("--disable-popup-blocking")
		driver = webdriver.Chrome('core/chromedriver', chrome_options=chrome_options)
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

		driver.get("https://web.whatsapp.com")
		search = WebDriverWait(driver, 35).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='side']/div[1]/div/label/div/div[2]")))
		search.send_keys(name, Keys.ENTER)
		time.sleep(7)
		msgBox = driver.find_element(By.XPATH,"//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]")

		for i in range(count):
			try:
				msgBox.send_keys(msg, Keys.RETURN)
				cn+=1
				print("\033[32m {}" .format(f'ATTACKING') + "\033[37m {}" .format('|') + "\033[36m {}" .format(str(cn)) + "\033[37m {}" .format('|') + "\033[35m {}" .format(name))
			except:
				cn+=1
				print("\033[32m {}" .format(f'ATTACKING') + "\033[37m {}" .format('|') + "\033[36m {}" .format(str(cn)) + "\033[37m {}" .format('|') + "\033[35m {}" .format(name))

		print("\033[32m{}" .format("\nSuccess!"))
		print(f"{cn} messages were sent to {name}")

	else:
		chrome_options = Options()
		chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
		chrome_options.add_experimental_option('useAutomationExtension', False)
		chrome_options.add_experimental_option('prefs', {
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

		driver.get("https://web.whatsapp.com")
		search = WebDriverWait(driver, 35).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='side']/div[1]/div/label/div/div[2]")))
		search.send_keys(name, Keys.ENTER)
		time.sleep(7)
		msgBox = driver.find_element(By.XPATH,"//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]")

		for i in range(count):
			try:
				msgBox.send_keys(msg, Keys.RETURN)
				cn+=1
				print("\033[32m {}" .format(f'ATTACKING') + "\033[37m {}" .format('|') + "\033[36m {}" .format(str(cn)) + "\033[37m {}" .format('|') + "\033[35m {}" .format(name))
			except:
				cn+=1
				print("\033[32m {}" .format(f'ATTACKING') + "\033[37m {}" .format('|') + "\033[36m {}" .format(str(cn)) + "\033[37m {}" .format('|') + "\033[35m {}" .format(name))

		print("\033[32m{}" .format("\nSuccess!"))
		print(f"{cn} messages were sent to {name}")
