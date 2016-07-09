import click,sys
from movies.get_data import *
from write import *

def main():
	location=raw_input("Enter the Location: ")
	location=location.lower().replace(" ", "+")
	get_movie_data(location)
	write_movie(location)

if __name__ == '__main__':
	main()