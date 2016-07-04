from movieList import getMovieList
from movieData import *
import os

def printd(i):
	for j in range(len(movies[i]['Extra'])+1):
		if movies[i]['Extra'][j-1]['Dimension'] is '2D':
			print 'N'
			# return
	# print 'Y'
	# return

def printlang(i):
	lang=set()
	for j in range(len(movies[i]['Extra'])+1):
		if movies[i]['Extra'][j-1]['Language'] not in lang:
			lang.add(movies[i]['Extra'][j]['Language'])
	print lang

width = os.popen('tput cols', 'r').readline()

print "="*int(width)

movies=getMovieList()

print "ID\tName\t\t\t\tGenre\t\t3D   Language\tDuration"
i=0
for i in range(len(movies)):
	print movies[i]['id'],"\t",movies[i]['Title'],"\t\t\t\t","Action","\t\t",printd(i),"   "#,printlang(i)#,"\t",printDuration(i-1)
	print "\n"
