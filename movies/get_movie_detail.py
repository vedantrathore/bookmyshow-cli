import requests
from get_data import *
from bs4 import BeautifulSoup

def get_movie_details(movie):
	url=str(movie['url'])
	response=requests.get(url)
	response.raise_for_status()
	soup=BeautifulSoup(response.text,'html.parser')
	name=soup.
	movie_detail={
		
	}

if __name__ == '__main__':
	location="kota"
	mlist=get_final_list(location)
	details=get_movie_details(mlist[0])