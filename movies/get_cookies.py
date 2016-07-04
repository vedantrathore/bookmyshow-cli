from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler
import cookielib,requests

def get_cookies(website):
	cj=cookielib.CookieJar()
	opener=build_opener(HTTPCookieProcessor(cj),HTTPHandler)
	req=Request(website)
	f=opener.open(req)
	cookies={}
	for cookie in cj:
		cookies[cookie.name]=cookie.value
	return cookies