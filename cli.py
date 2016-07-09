import click,sys
from movies.get_data import *
from write import *

def main():
	location=raw_input("Enter the Location: ")
	location=location.lower().replace(" ", "+")
	write_movie(location)
	input_movie=int(raw_input("\nEnter a movie ID or -1 to exit : "))
	if input_movie == -1:
		sys.exit()
	get_movie_details(input_movie)

if __name__ == '__main__':
	main()