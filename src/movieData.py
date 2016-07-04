from getCookies import getCookies
import json,requests

file='/home/nero/github/bookmyshow-cli/src/data/movies.json'

def getMovie(website):
	cookies=getCookies(website)
	url="https://in.bookmyshow.com/serv/getData?cmd=QUICKBOOK&type=MT"
	response=requests.get(url,cookies=cookies)
	response.raise_for_status()
	# Data=(json.loads(response.text))
	with open(file,'w') as outf:
		outf.write(response.content)

def numberOfMovies():
	movieData=json.loads(open(file).read())
	return len(movieData['moviesData']['BookMyShow']['arrEvents'])

def numberOfChildEvents(i):
	movieData=json.loads(open(file).read())
	return len(movieData['moviesData']['BookMyShow']['arrEvents'][i]['ChildEvents'])	

if __name__ == '__main__': 
	location="kota"
	website="https://in.bookmyshow.com/"+location+"/movies"
	print numberOfMovies()
	print numberOfChildEvents(0)