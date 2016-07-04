from src.data import  getMovie
import argparse

parser=argparse.ArgumentParser(description='Get details about all movies')
parser.add_argument("location",help="The city you want movies for")
args=parser.parse_args()

location=args.location
location=location.replace(" ", "-").lower()

website="https://in.bookmyshow.com/"+location+"/movies"
movies=getMovie(website);

print movies['moviesData']['BookMyShow']['arrEvents'][2]['EventTitle']
