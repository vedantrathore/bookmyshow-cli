from getCookies import getCookies
import json,requests

def getMovie(website):
	cookies=getCookies(website)
	url="https://in.bookmyshow.com/serv/getData?cmd=QUICKBOOK&type=MT"
	response=requests.get(url,cookies=cookies)
	response.raise_for_status()
	Data=(json.loads(response.text))
	return Data