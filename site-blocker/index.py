import time 
from datetime import datetime as dt

# hosts Files
# Windows c:\\windows\sistem32\drivers\etc
# Mac & Linux /etc/hosts

HOSTS_PATH_WINDOWS = r'C:\Windows\System32\drivers\etc\
hosts'
HOSTS_UNIX_WINDOWS = '/etc/hosts'
HOST_DIR = "hosts"
REDIRECT = "127.0.0.1"

websites_list = [
    "www.facebook.com",
    "facebook.com",
    "mail.google.com",
    "youtube.com"
]

from_hour = 10
to_hour = 18

while True:

    if dt(dt.now().year, dt.now().month, dt.now().day, from_hour) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, to_hour):
        print('Working')
        with open(HOST_DIR, 'r+') as file:
            content = file.read()
            
            for website in websites_list:
                if website in content:
                    pass
                else:
                    file.write(REDIRECT + " " + website + "\n")
    else:
        print('Fun')
        with open(HOST_DIR, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_list):
                    file.write(line)
            file.truncate()    
    time.sleep(1)