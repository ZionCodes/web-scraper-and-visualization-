import requests
from bs4 import BeautifulSoup

def main():
    url = "https://news.ycombinator.com/item?id=29782099"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.find_all(class_="comment", indent=0)
    comments = [e.find_next(class_="comment") for e in elements]
    print(f"Elements: {len(elements)}")

if __name__ == "__main__":
    main()