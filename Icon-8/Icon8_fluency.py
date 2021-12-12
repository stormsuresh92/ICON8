from requests_html import HTMLSession
import os
from tqdm import tqdm



s = HTMLSession()

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'
    }

key = input('Enter your keyword here:')

cur_dir = os.getcwd()
out = cur_dir + f'/{key}'
if not os.path.exists(out):
    os.mkdir(out)


url = f'https://icons8.com/icon/set/{key}/fluency'
r = s.get(url, headers=headers)
icons = r.html.find('div.app-icon.grid-icon__icon.is-fluent')
for icon in tqdm(icons):
    title = icon.find('img', first=True).attrs['alt']
    urls = icon.find('img', first=True).attrs['srcset'].replace('2x', '').strip()
    image = s.get(urls, stream=True)
    with open(out + '/' + title + '.png', 'wb') as f:
        f.write(image.content)
