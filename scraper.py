import requests
import argparse

from bs4 import BeautifulSoup

WORM_URL = 'https://parahumans.wordpress.com/2011/06/11/1-1/'
WARD_URL = 'https://www.parahumans.net/2017/10/21/glow-worm-0-1/'

class Scraper:
	def __init__(self, url, output):
		self.url = url
		self.output = output

	def main(self):
		pass
		
if __name__ == '__main__':
	parser = argparse.ArgumentParser(prog='Webserial to E-Book', description='Scraper to convert webserials to ebook format.')
	parser.add_argument('-u', '--url', action='store', dest='url', default=WORM_URL, required=False, help='First chapter URL, ')
	parser.add_argument('-o', '--output', action='store', dest='output', required=True, help='File destination')
	args = parser.parse_args()

	if((args.url).lower() == 'ward'):
		args.url = WARD_URL
	
	if((args.url).lower() == 'worm'):
		args.url = WORM_URL

	c = Scraper(args.url, args.output)
	c.main()