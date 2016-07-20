from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler
import cookielib,requests

def get_cookies(location):
	website="https://in.bookmyshow.com/"+location+"/movies"
	cj=cookielib.CookieJar()
	opener=build_opener(HTTPCookieProcessor(cj),HTTPHandler)
	req=Request(website, headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30"})
	f=opener.open(req)
	cookies={}
	for cookie in cj:
		cookies[cookie.name]=cookie.value
	return cookies