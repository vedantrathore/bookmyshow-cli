import click,sys
from movies import *
from write import *

def main():
	location=raw_input("Enter the Location: ")
	location=location.lower().replace(" ", "+")
	movie_list=write_movie_list(location)
	input_movie_id=int(raw_input("\nEnter a movie ID or -1 to exit : "))
	if input_movie_id == -1:
		sys.exit()
	movie_details=get_movie_details(movie_list[input_movie_id-1])
	write_movie(movie_details)

if __name__ == '__main__':
	main()