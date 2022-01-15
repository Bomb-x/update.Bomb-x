bgreen="\033[1;32m"       # Green
bblack="\033[1;30m"       # Black
r="\033[1;31m"         # Red
bgreen="\033[1;32m"       # Green
y="\033[1;33m"      # Yellow
bblue="\033[1;34m"        # Blue
p="\033[1;35m"      # Purple
c="\033[1;36m"        # Cyan
bwhite="\033[1;37m"       # White
logo=bgreen+str("""
______                    _                   
| ___ \                  | |                  
| |_/ /  ___   _ __ ___  | |__   ______ __  __
| ___ \ / _ \ | '_ ` _ \ | '_ \ |______|\ \/ /
| |_/ /| (_) || | | | | || |_) |         >  < 
\____/  \___/ |_| |_| |_||_.__/         /_/\_\ 
===============================================
     ***Devoloper : Mishkat Zaman***
===============================================
            Version : 2.0
""")
import os
while True:
	os.system("clear")
	print(logo)
	print(r+""" [1] Sms bomber\n [2] E-Mail bomber\n [3] Mask phishlink\n [4] Exit """)
	a=str(input(c+""" 
[√] Select your option : """+y))
	if a=="1":
		os.system("python3 01.py")
		a=input()
	elif a=="2":
		os.system("python3 02.py")
		a=input()
	elif a=="3":
		os.system("python3 03.py")
		a=input()
	elif a=="4":
		print(""" 
		Thanks for using Bomb-x
		""")
		quit()
		a=input()
	else:
		print(p+"wrong")
		a=input()