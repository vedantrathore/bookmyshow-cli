import click,sys
from movies import *
from write import *
from pprint import pprint
from movies.get_movie_detail import get_movie_details

def main():
	location=raw_input("Enter the Location: ")
	location=location.lower().replace(" ", "+")
	movie_list=write_movie_list(location)
	input_movie_id=int(raw_input("\nEnter a movie ID or -1 to exit : "))
	if input_movie_id == -1:
		sys.exit()
	movie_details=get_movie_details(movie_list[input_movie_id-1])
	pprint(movie_details)

if __name__ == '__main__':
	main()