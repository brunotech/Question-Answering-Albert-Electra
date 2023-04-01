# %%
import requests
import bs4
import re
from googlesearch import search
import re


# %%
def get_url_text(text):
    urls = search(text, tld='com', lang='en-US', safe='on', stop=15)
    if not (link := next((url for url in urls if 'wikipedia' in url), None)):
        return None, None
    response = requests.get(link)
    lines = []
    if response is not None:
        html = bs4.BeautifulSoup(response.text, 'html.parser')
        title = html.select("#firstHeading")[0].text
        paragraphs = html.select("p")
        for para in paragraphs:
            text = re.sub(r'\[\w+\]', '', para.text)
            text = re.sub(r'\s\s+', '', text)
            text = re.sub(r'\n', '', text)
            if len(text.split()) > 5:
                lines.append(text)
    return link, lines
