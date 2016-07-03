from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler
import cookielib,requests
import json

def getCookies(website):	
	cj=cookielib.CookieJar()
	opener=build_opener(HTTPCookieProcessor(cj),HTTPHandler)
	req=Request(website)
	f=opener.open(req)
	return cj

def getMovieData(location):
	website="https://in.bookmyshow.com/"+location+"/movies"
	cj=getCookies(website)
	cookies={}
	for cookie in cj:
		cookies[cookie.name]=cookie.value
	url="https://in.bookmyshow.com/serv/getData?cmd=QUICKBOOK&type=MT"
	response=requests.get(url,cookies=cookies)
	response.raise_for_status()
	Data=(json.loads(response.text))
	return Data


def main():
	location=raw_input("Enter a location: ")
	movieData=getMovieData(location)	

if __name__ == '__main__':
	main()