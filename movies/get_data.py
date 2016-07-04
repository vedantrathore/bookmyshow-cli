from get_cookies import get_cookies
import json,requests,os
from pprint import pprint

file="/home/nero/python projects/bms/bms/movies/data/movies.json"

def get_movie_data(location):
	website="https://in.bookmyshow.com/"+location+"/movies"
	if os.stat(file).st_size==0: 
		cookies=get_cookies(website)
		url="https://in.bookmyshow.com/serv/getData?cmd=QUICKBOOK&type=MT"
		response=requests.get(url,cookies=cookies)
		response.raise_for_status()
		#Data=(json.loads(response.text))
		with open(file,'w') as outf:
			outf.write(response.content)
	else:
		movieData=json.loads(open(file).read())
		if movieData['cinemas']['BookMyShow']['aiVN'][0]['VenueSubRegionName'].lower()!=location:
			cookies=get_cookies(website)
			url="https://in.bookmyshow.com/serv/getData?cmd=QUICKBOOK&type=MT"
			response=requests.get(url,cookies=cookies)
			response.raise_for_status()
			#Data=(json.loads(response.text))
			with open(file,'w') as outf:
				outf.write(response.content)

def get_number_of_movies():
	movieData=json.loads(open(file).read())
	return len(movieData['moviesData']['BookMyShow']['arrEvents'])

def get_number_of_child_events(i):
	movieData=json.loads(open(file).read())
	return len(movieData['moviesData']['BookMyShow']['arrEvents'][i]['ChildEvents'])	

def get_movie_list():
	with open(file) as df:
		data=json.load(df)
	mlist=[]
	nmovies=get_number_of_movies()
	for i in range(0,nmovies-1):
		movies={
			'Title': data['moviesData']['BookMyShow']['arrEvents'][i]['EventTitle'],
			'Duration':data['moviesData']['BookMyShow']['arrEvents'][i]['EventGrpDuration'],
			'Genre':data['moviesData']['BookMyShow']['arrEvents'][i]['EventGrpGenre'],
			'Censor':data['moviesData']['BookMyShow']['arrEvents'][i]['EventGrpCensor']	
		}
		movies['id']=i+1
		movies['Extra']=[]
		if get_number_of_child_events(i)>0:
			for j in range(1,get_number_of_child_events(i)+1):
				extra={
					'Dimension':data['moviesData']['BookMyShow']['arrEvents'][i]['ChildEvents'][j-1]['EventDimension'],
					'Language':data['moviesData']['BookMyShow']['arrEvents'][i]['ChildEvents'][j-1]['EventLanguage'],
					'isNew':data['moviesData']['BookMyShow']['arrEvents'][i]['ChildEvents'][j-1]['isNewEvent']
				}
				movies['Extra'].append(extra)

		mlist.append(movies)
	return mlist

def get_rating():
	"""Implement RottenTomatoes api for ratings of movies"""
	pass

if __name__ == '__main__':
	location="kota"
	website="https://in.bookmyshow.com/"+location+"/movies"
	print get_number_of_movies()
	print get_number_of_child_events(0)
	pprint(get_movie_list())