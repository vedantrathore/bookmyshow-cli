from movieData import *
import json
from pprint import pprint

def getMovieList():
	with open(file) as df:
		data=json.load(df)
	mlist=[]
	nmovies=numberOfMovies()
	for i in range(0,nmovies-1):
		movies={
			'Title': data['moviesData']['BookMyShow']['arrEvents'][i]['EventTitle'],
			'Duration':data['moviesData']['BookMyShow']['arrEvents'][i]['EventGrpDuration'],
			'Genre':data['moviesData']['BookMyShow']['arrEvents'][i]['EventGrpGenre'],
			'Censor':data['moviesData']['BookMyShow']['arrEvents'][i]['EventGrpCensor']	
		}
		movies['id']=i+1
		movies['Extra']=[]
		if numberOfChildEvents(i)>0:
			for j in range(1,numberOfChildEvents(i)+1):
				extra={
					'Dimension':data['moviesData']['BookMyShow']['arrEvents'][i]['ChildEvents'][j-1]['EventDimension'],
					'Language':data['moviesData']['BookMyShow']['arrEvents'][i]['ChildEvents'][j-1]['EventLanguage'],
					'isNew':data['moviesData']['BookMyShow']['arrEvents'][i]['ChildEvents'][j-1]['isNewEvent']
				}
				movies['Extra'].append(extra)

		mlist.append(movies)
	return mlist

if __name__ == '__main__':
	pprint(getMovieList())