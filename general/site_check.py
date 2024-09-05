import random
import time
from os import getcwd
import tor
from termcolor import colored
username=None
total_exists=0
non_existes=0
diff_res=0
list_exist=[]
list_non_exist=[]
list_diff_res=[]
url=""
    
    
    
def check(name):
    global username
    username=name.replace(" ","-")
    dirt=str(getcwd())
    tor.start_tor()
    with open(f"{dirt}\\resource\\Site.txt", "r") as f1:
        for line in f1.readlines():
            url = line.strip()
            res_detail(url)
            time.sleep(random.uniform(2,6))
            
    tor.stop_tor()
    
    
    
#response details          
def res_detail(URL):
    global url
    url=f"{URL}/{username}"
    res=tor.tor_request(url)
    
    if(res==200):
        global total_exists
        global non_existes
        global diff_res
        total_exists+=1
        list_exist.append(tor.site_name(url))
        print(f"[{colored(tor.site_name(url),'green')}]: The {tor.site_name(url)} account '{username}' exists....")
    
    elif(res==429):
        i=0
        for i in range(0,5):
            print(f"[{tor.site_name(url)}]: The {tor.site_name(url)} request rate limit is exists for the username '{username}'....")
            print(f"[{tor.site_name(url)}]wait for 60 sec...")
            time.sleep(60)
            res=tor.tor_request(url)
            if(res==200):
                print(f"[{tor.site_name(url)}]: The {tor.site_name(url)} account '{username}' exists....")
                total_exists+=1
                list_exist.append(tor.site_name(url))
                break
            time.sleep(60)
        
        if(i==4):
            diff_res+=1
            list_diff_res.append(tor.site_name(url))
            print(f"[{tor.site_name(url)}]: Try after some times...")
    elif(res==403):
        diff_res+=1
        list_diff_res.append(tor.site_name(url))
        print(f"{colored(tor.site_name(url),'blue')} permission denied")
    elif(res==999):
        diff_res+=1
        list_diff_res.append(tor.site_name(url))
        print(f"[{colored(tor.site_name(url),'red')}]: Security system eliminated your requests..")
    else:
        non_existes+=1
        list_non_exist.append(tor.site_name(url))
        print(f"{tor.site_name(url)} {colored("Bad Response...","light_magenta")}")

