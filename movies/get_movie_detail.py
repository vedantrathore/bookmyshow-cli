from bs4 import BeautifulSoup
import requests

def get_movie_details(movie):
	url=str(movie['url'])
	response=requests.get(url)
	response.raise_for_status()
	soup=BeautifulSoup(response.text,'html.parser')
	name=soup.findAll('h1',{'class':'__name'})[0].string
	synopsis=(soup.findAll('div',{'class':'synopsis'})[0].blockquote.findAll(text=True))
	synopsis=str(' '.join(synopsis))
	synopsis=synopsis.strip(' \t\n')
	critic_rating=soup.findAll('span',{'class':'__rating'})[0].ul.attrs['data-value']
	trailer_code=soup.findAll('div',{'class':'banner-main synopsis-banner'})[0].attrs['data-trailer-code']
	trailer_url="www.youtube.com/watch?v="+trailer_code
	cast_list=soup.findAll('span',{'itemprop':'actor'})
	cast=[]
	for cast_member in cast_list:
		cast_name=cast_member.a.div.attrs['content']
		cast.append(cast_name)
	booking_url_code=soup.findAll('div',{'class':'more-showtimes'})[0].a.attrs['href']
	booking_url="https://in.bookmyshow.com"+booking_url_code
	movie_detail={
		'name': name,
		'synopsis' : synopsis,
		'critic_rating' : critic_rating,
		'trailer-url': trailer_url,
		'lead_cast': cast[0:4],
		'booking_url': booking_url 
	}
	return movie_detail

if __name__ == '__main__':
	from pprint import pprint
	from get_data import get_final_list
	location="kota"
	mlist=get_final_list(location)
	pprint(mlist[0])
	details=get_movie_details(mlist[0])
	pprint(details)