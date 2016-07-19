import sys
from write import write_movie_list,write_movie
from movies.get_movie_detail import get_movie_details
import webbrowser

def main():
	location=raw_input("Enter the Location: ")
	location=location.lower().replace(" ", "+")
	movie_list=write_movie_list(location)
	input_movie_id=int(raw_input("\nEnter a movie ID or -1 to exit : "))
	if input_movie_id == -1:
		sys.exit()
	movie_details=get_movie_details(movie_list[input_movie_id-1])
	write_movie(movie_details)
	book=int(raw_input("Enter any key to Book Movie or -1 to exit : "))
	if book == -1:
		sys.exit()
	webbrowser.open_new(movie_details['booking_url'])

if __name__ == '__main__':
	main()