from src.movieList import  getMovie

#location=raw_input("Enter the location :")
location="Kota"
location=location.replace(" ", "-").lower()
print location
website="https://in.bookmyshow.com/"+location+"/movies"
movies=getMovie(website);
print movies['moviesData']['BookMyShow']['arrEvents'][0]['EventTitle']

