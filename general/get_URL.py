import requests
from bs4 import BeautifulSoup

proxy = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

def add_unique_lines( new_lines,file_path="new_web.txt"):
    # Read existing lines into a set to track unique lines
    try:
        with open(file_path, 'r') as file:
            existing_lines = set(file.read().splitlines())
    except FileNotFoundError:
        existing_lines = set()  # If file does not exist, start with an empty set

    # Add new lines to the set (duplicates will be ignored automatically)
    existing_lines.update(new_lines)

    # Write the unique lines back to the file
    with open(file_path, 'w') as file:
        file.write("\n".join(existing_lines))



      

def search(inp):
    res=requests.get(f"http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/search/?q={inp}",proxies=proxy)
    print("Searched successfull....")
    result=res.text
    res.close()
    return result


def find_link(inp):
    inp=inp.replace(" ","+")
    List=set()
    content=search(inp)
    soup = BeautifulSoup(content, 'html.parser')
    for i in soup.find_all("cite"):
        List.add(i.get_text()+"/")
    print(List)
    return  List

def main():    
    while True:
        inp=str(input("Enter a Query >>> "))
        List=find_link(inp)
        add_unique_lines(List)

