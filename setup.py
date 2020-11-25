#!/bin/python3

import subprocess
import os
from time import sleep
from colorama import init
init()
#################
CR='\033[31;1m' #
CG='\033[32;1m' #
CY='\033[33;1m' #
CB='\033[34;1m' #
CC='\033[36;1m' #
CW='\033[37;1m' #
#################

def file():
	print(f'{CR}[{CY}#{CR}]{CG} Star Setuping......\n')
	log = os.path.exists('/usr/bin/macqish')
	sleep(1)
	if log != True:
		if os.path.exists('MacQish.tar.gz'):
			print(f"{CR}[{CY}#{CR}]{CG} MacQish.tar.gz File Found !\n")
			sleep(2)
			os.system(f'tar -xvf MacQish.tar.gz >/dev/null 2>&1;')
			os.system(f'mv macqish /usr/bin/')
			print(f"{CR}[{CY}#{CR}] Successfull......\n")
			print(f"{CR}[{CY}+{CR}]{CC} Now Just Type 'macqish' \n")

		else:
			print(f'{CR} File Not Exists !!')
	else:
		print(f"{CR}[{CY}+{CR}]{CC} File Already Exiest Now Just Type 'macqish' \n")
		os._exit(0)

if __name__ == '__main__':
	euid = os.getegid()
	if euid == 0:
		file()
	else:
		print(f"{CR}\n\t\tRun As Root !\n")
		os._exit(0)
