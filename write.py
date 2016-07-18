import click,sys
import textwrap
from movies.get_data import *

def colors():
	"""Creates an enum for colors"""
	enums = dict(
		#TIME_LEFT="red",
		name="yellow",
		title="magenta",
		genre="green",
		synopsis="cyan",
		duration="blue",
		dimension="red"
	)
	return type('Enum', (), enums)


def write_movie_list_header():
	sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=40, cols=110))
	click.secho("\n %-3s  %-40s   %-30s %-10s %-15s" % 
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


def write_movie(movie):
	click.echo()
	name=movie['name']
	critic_rating=movie['critic_rating']
	cast=movie['lead_cast']
	synopsis="\033[35m"+movie['synopsis']
	trailer=movie['trailer-url']
	click.secho("   Name     :  ",nl=False,fg=colors().synopsis)
	click.secho(" %-30s"%name,bold=True,fg=colors().duration)
	prefix="   Synopsis :   "
	preferredWidth=70
	wrapper = textwrap.TextWrapper(initial_indent=prefix, width=preferredWidth,subsequent_indent=' '*len(prefix))
	click.secho(wrapper.fill(synopsis),fg=colors().synopsis)
	click.secho("   Cast     :   ",nl=False,fg=colors().synopsis)
	cast_names=", ".join(cast)
	click.secho(cast_names,fg=colors().genre)
	click.secho("   Rating   :   ",nl=False,fg=colors().synopsis)
	click.secho(critic_rating)
	click.secho("   Trailer  :   ",nl=False,fg=colors().synopsis)
	click.secho(trailer,fg=colors().name)
	click.echo()

if __name__ == '__main__':
	location="kota"
	movie={'critic_rating': u'2.5',
 'lead_cast': [u'Riteish Deshmukh',
			   u'Vivek Oberoi',
			   u'Aftab Shivdasani',
			   u'Urvashi Rautela'],
 'name': u'Great Grand Masti',
 'synopsis': 'Great Grand Masti is the third film in the Masti trilogy. The  Adult Comedy  stars the terrific trio of - Riteish Deshmukh, Aftab Shivdasani and Vivek Oberoi.  They meet Ragini (Urvashi Rautela) in a village. The movie revolves around how the trio find out that Ragini is not the hot girl she appears at first.',
 'trailer-url': u'www.youtube.com/watch?v=ZojV0FC-KdI'}
	write_movie(movie)