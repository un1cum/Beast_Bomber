'''
╔═════════════════════════════════════════════════════════════════════════════════╗
║				                                                  ║
║		                     BoMbEr 2.0                                   ║
║  Authors:                                                                       ║
║  https://github.com/ebankoff                                                    ║
║  https://github.com/cludeex		                                          ║
║  https://github.com/ncorbuk                                                     ║
║  https://github.com/Nikait							  ║
║                                                   				  ║
║  The authors of this program are not responsible for its use!                   ║
║  When placing this code on third-party resources, please indicate the authors!  ║ 
║                                                                                 ║
║  			        All rights reserved.                              ║
║			    Copyright (C) 2021 ebankoff                           ║                                           								  
║		                                                                  ║
╚═════════════════════════════════════════════════════════════════════════════════╝
'''

#--------------------------------------(setup)--------------------------------------

import os
import time
from progress.bar import Bar
from progress.spinner import Spinner

os.system("cls")

print("\033[34m{}" .format('''
╔══╗   ╔═╗╔═╦╗ ╔═══╗   ╔═══╦═══╦════╦╗ ╔╦═══╗
║╔╗║   ║ ╚╝ ║║ ║╔══╝   ║╔═╗║╔══╣╔╗╔╗║║ ║║╔═╗║
║╚╝╚╦══╣╔╗╔╗║╚═╣╚══╦═╗ ║╚══╣╚══╬╝║║╚╣║ ║║╚═╝║
║╔═╗║╔╗║║║║║║╔╗║╔══╣╔╝ ╚══╗║╔══╝ ║║ ║║ ║║╔══╝
║╚═╝║╚╝║║║║║║╚╝║╚══╣║  ║╚═╝║╚══╗ ║║ ║╚═╝║║
╚═══╩══╩╝╚╝╚╩══╩═══╩╝  ╚═══╩═══╝ ╚╝ ╚═══╩╝
	'''))

def pb():              
	spinner = Spinner('Setup ', max=20)
	for i in range(20):
		time.sleep(.20)
		spinner.next()
	spinner.finish()

pb()

print("")

try:
	os.system('pip install about-time')
	print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + "\033[37m {}" .format('|') + "\033[33m {}" .format('Installed') + "\033[37m {}" .format('|') + "\033[32m {}" .format(f'SUCCESS') + "\033[37m {}" .format('|') + "\033[35m {}" .format('about-time'))

	os.system('pip install progressbar')
	print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + "\033[37m {}" .format('|') + "\033[33m {}" .format('Installed') + "\033[37m {}" .format('|') + "\033[32m {}" .format(f'SUCCESS') + "\033[37m {}" .format('|') + "\033[35m {}" .format('progressbar'))

	os.system('pip install progress')
	print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + "\033[37m {}" .format('|') + "\033[33m {}" .format('Installed') + "\033[37m {}" .format('|') + "\033[32m {}" .format(f'SUCCESS') + "\033[37m {}" .format('|') + "\033[35m {}" .format('progress'))

	os.system('pip install datetime')
	print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + "\033[37m {}" .format('|') + "\033[33m {}" .format('Installed') + "\033[37m {}" .format('|') + "\033[32m {}" .format(f'SUCCESS') + "\033[37m {}" .format('|') + "\033[35m {}" .format('datetime'))

	os.system('pip install requests')
	print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + "\033[37m {}" .format('|') + "\033[33m {}" .format('Installed') + "\033[37m {}" .format('|') + "\033[32m {}" .format(f'SUCCESS') + "\033[37m {}" .format('|') + "\033[35m {}" .format('requests'))

	os.system('pip install selenium')
	print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + "\033[37m {}" .format('|') + "\033[33m {}" .format('Installed') + "\033[37m {}" .format('|') + "\033[32m {}" .format(f'SUCCESS') + "\033[37m {}" .format('|') + "\033[35m {}" .format('selenium'))

	os.system('pip install webdriver-manager')
	print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + "\033[37m {}" .format('|') + "\033[33m {}" .format('Installed') + "\033[37m {}" .format('|') + "\033[32m {}" .format(f'SUCCESS') + "\033[37m {}" .format('|') + "\033[35m {}" .format('webdriver-manager'))

	os.system('pip install wheel')
	print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + "\033[37m {}" .format('|') + "\033[33m {}" .format('Installed') + "\033[37m {}" .format('|') + "\033[32m {}" .format(f'SUCCESS') + "\033[37m {}" .format('|') + "\033[35m {}" .format('wheel'))

	os.system('pip install user-agent')
	print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + "\033[37m {}" .format('|') + "\033[33m {}" .format('Installed') + "\033[37m {}" .format('|') + "\033[32m {}" .format(f'SUCCESS') + "\033[37m {}" .format('|') + "\033[35m {}" .format('user-agent'))

	os.system('pip install asyncio')
	print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + "\033[37m {}" .format('|') + "\033[33m {}" .format('Installed') + "\033[37m {}" .format('|') + "\033[32m {}" .format(f'SUCCESS') + "\033[37m {}" .format('|') + "\033[35m {}" .format('asyncio'))

	print("\033[32m{}" .format("\nSetup is COMPLETE!"))

except:
	print("\033[31m{}" .format("\nSetup FAILED!"))

input()
