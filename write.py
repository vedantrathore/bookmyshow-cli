import click,sys
from movies.get_data import *

def colors():
	"""Creates an enum for colors"""
	enums = dict(
		#TIME_LEFT="red",
		name="yellow",
		genre="green",
		duration="blue",
		dimension="red"
	)
	return type('Enum', (), enums)


def write_movie_list_header():
	sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=40, cols=110))
	click.secho(" %-3s  %-40s   %-30s %-10s %-15s" % 
	("ID", "NAME", "GENRE", "3D","DURATION"))

def write_movie_list(location):
	write_movie_list_header()
	movie_list=get_final_list(location)
	for index,movie in enumerate(movie_list):
		name=movie['Title'].encode('utf-8')
		genres=movie['Genre'].split("|")
		extra=movie['Extra']
		duration=format(float(float(movie['Duration'])/60),'.2f')+' Hrs'
		click.echo()
		click.secho(" %-3s"%str(index+1),nl=False,bold=False)
		click.secho("  %-40s" %
					name,nl=False,fg=colors().name,bold=False)
		gs=""
		for genre in genres:
			genre=genre.title()
			# print genre
			gs=gs+genre+" "
			# print gs
		click.secho(" %-30s"%gs,nl=False,fg=colors().genre,bold=False)
		for i,child in enumerate(extra):
			td=False
			if extra[i]['Dimension']=='3D':
				td=True
		if td==True:
			click.secho("   %-10s"%'Yes',nl=False,bold=False)
		else:
			click.secho("   %-10s"%'No',fg=colors().dimension,nl=False,bold=False)
		
		click.secho(" %-5s"%duration,nl=False,bold=False)
		click.echo()
	return movie_list


def write_movie():
	pass

if __name__ == '__main__':
	location="kota"
	write_movie_list(location)