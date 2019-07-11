import re
import requests
import argparse

from bs4 import BeautifulSoup

WORM_URL = 'https://parahumans.wordpress.com/2011/06/11/1-1/'
WARD_URL = 'https://www.parahumans.net/2017/10/21/glow-worm-0-1/'

class Scraper:
    def __init__(self, url, output):
        self.url = url
        self.output = output

    def url_content(self):
        r = requests.get(self.url)
        return(r.text)

    def get_next_chapter(self, content):
        try:
            next_c = content.find('a', string=re.compile('Next Chapter'))['href']
        except:
            next_c = None
        return(next_c)

    def get_title(self, content, title_list):
        title = content.find(class_='entry-title').text
        title_list.append(title)
        return(title_list)

    def get_chapter_text(self, content):
        paragraphs = []
        main_text = content.find(class_='entry-content')
        prgh = main_text.find_all('p')
        for p in prgh:
            if (re.search('Next Chapter', p.text) == None):
                fixed_text = p.text.replace(u'\xa0', '')
                paragraphs.append(fixed_text)
        return(paragraphs)    
        # return(fixed_text)  

    def main(self):
        source_code = self.url_content()
        content = BeautifulSoup(source_code, 'html.parser')

        title_list = []
        next_c = self.get_next_chapter(content)
        title_list = self.get_title(content, title_list)
        t = self.get_chapter_text(content)
        
        with open(f'./abc/{title_list[0]}.txt', 'w', encoding="utf-8") as f:
            f.write("\n\n".join(t))

        print(f"{title_list[0]} -> {next_c}")
        if next_c != None:
            self.url = next_c
            return(next_c)
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Webserial to E-Book', description='Scraper to convert webserials to ebook format.')
    parser.add_argument('-u', '--url', action='store', dest='url', default=WORM_URL, required=False, help='First chapter URL, ')
    parser.add_argument('-o', '--output', action='store', dest='output', required=False, help='File destination')
    args = parser.parse_args()

    if((args.url).lower() == 'ward'):
        args.url = WARD_URL
    
    if((args.url).lower() == 'worm'):
        args.url = WORM_URL

    c = Scraper(args.url, args.output)
    l = c.main()
    while(l != None):
        l = c.main()