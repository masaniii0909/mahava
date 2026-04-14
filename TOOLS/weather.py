import argparse as ap
from requests_html import HTMLSession

parser = ap.ArgumentParser(description='get the weather for an area')
parser.add_argument('--prompt')
args = parser.parse_args()
prompt = args.prompt


s = HTMLSession()

#query=str(prompt).replace(' ', '+')
query = 'what+is+the+weather+in+tiverton'
url = f'https://www.google.com/search?q={query}'
r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:149.0) Gecko/20100101 Firefox/149.0'})
print(r.html.find('span#wob_tm', first=True).text)
