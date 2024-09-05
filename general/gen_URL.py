import requests
from bs4 import BeautifulSoup
from transformers import pipeline

# Proxy configuration for Tor
proxy = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

# Function to ensure unique lines in the output file
def add_unique_lines(new_lines, file_path="new_web.txt"):
    try:
        with open(file_path, 'r') as file:
            existing_lines = set(file.read().splitlines())
    except FileNotFoundError:
        existing_lines = set()  # If file does not exist, start with an empty set

    existing_lines.update(new_lines)

    with open(file_path, 'w') as file:
        file.write("\n".join(existing_lines))

# Function to perform the search
def search(inp):
    res = requests.get(f"http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/search/?q={inp}", proxies=proxy)
    print("Search successful....")
    result = res.text
    res.close()
    return result

# Function to find and extract links
def find_link(inp):
    inp = inp.replace(" ", "+")
    List = set()
    content = search(inp)
    soup = BeautifulSoup(content, 'html.parser')
    for i in soup.find_all("cite"):
        List.add(i.get_text() + "/")
    print(List)
    return List

# Step 3: GPT-Generated Query Integration
def generate_query(prompt):
    gpt_pipeline = pipeline('text-generation', model='gpt-2',tokenizer='gpt-2')  # You can use other models as well
    generated_text = gpt_pipeline(prompt, max_length=50, num_return_sequences=1)
    return generated_text[0]['generated_text']

# Main Loop with GPT Integration
while True:
    prompt = str(input("Enter a prompt for GPT >>> "))
    generated_query = generate_query(prompt)
    print(f"Generated Query: {generated_query}")
"""
    List = find_link(generated_query.strip())
    add_unique_lines(List)"""
