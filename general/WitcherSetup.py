from Banner import banner
from termcolor import colored

#Titile

banner()


def getInp():
    print("1.Check  for your username from the popular Socialmedia.")
    print("2.Check for gmail.")
    print("3.Use proxy")
    print("4.URL Generation")
    print("5.Exit")
    try:
        a=eval(input("Enter your option >>> "))
    except NameError:
        return "Enter a valid option...."
    return a


#general social media site.. checking
def option1():
    import site_check
    inp=str(input("Enter the username >>> "))
    site_check.check(inp)
    print(f"total number of profile exists : {site_check.total_exists}")
    try:
        inp=eval(input("if you want existing profile list....enter 1 >>> "))
        if inp==1:
            n=1
            for i in site_check.list_exist:
                print(colored(i,'green'),end=" ")
                if(n%5==0):
                    print()
                if(i==site_check.list_exist[:-1]):
                    print("\n")
                n+=1
    except:
        pass 
    print(f"total number of profile not exists : {site_check.non_existes}")
    try:
        inp=eval(input("if you want non existing profile list....enter 1 >>> "))
        if inp==1:
            n=1
            for i in site_check.list_non_exist:
                print(colored(i,'red'),end=" ")
                if(n%5==0):
                    print()
                if(i==site_check.list_non_exist[:-1]):
                    print("\n")
                n+=1
    except:
        pass 
    print(f"total number of different responses : {site_check.diff_res}")
    try:
        inp=eval(input("if you want different response list....enter 1 >>> "))
        if inp==1:
            n=1
            for i in site_check.list_diff_res:
                print(colored(i,'blue'),end=" ")
                if(n%5==0):
                    print()
                n+=1
            print("\n")        
                
    except:
        pass



#Checking g-mail from g-mail account and snap    
def option2():
    
    #checking gmail
    from Google_ui import check
    inp=str(input("Enter your gmail >>> "))
    check(inp)


def option3():
    import tor
    tor.start_tor()
    try:
        driver=tor.tor_driver()
        driver.get("https://duckduckgo.com/")
        input("Press Enter after closing the browser...")
    except:
        tor.stop_tor()
        driver.close()
    else:
        tor.stop_tor()
        driver.quit()

def option4():
    import tor
    import get_URL
    import time
    tor.start_tor()
    get_URL.main()
    time.sleep(3)
    tor.start_tor()
    
flag=True
if __name__=="__main__":
    try:
        while(flag==True):
            try:
                a=getInp()
                #checking username from general websites..
                if(a==1):
                    print("Option 1 selected")
                    option1()
                
                #checking gmail from gmail-account and snap
                elif(a==2):
                    print("Option 2 selected")
                    option2()
                
                #use proxy in google...
                elif(a==3):
                    print("Option 3 selected")
                    option3()
                elif(a==4):
                    print("Option 4 selected")
                    option4()
                else:
                    exit()
            except:
                #elif(a=="exit" or a=="Exit" or a==3):
                exit()
            
   
    except KeyboardInterrupt:
            exit()

#C:\Users\dinku\OneDrive\Desktop\Tor Browser\Browser\TorBrowser\Tor