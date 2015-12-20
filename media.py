import webbrowser

class Movie():
	"""Movie data for an HTML static page.

Attributes:

    title (str): The title of the movie
	releasedate (str): The original movie release date
	storyline (str): A terse description of the plot
	poster_image (url): The URL of poster image
	trailer_youtube_url (url): The URL of the official trailer posted on youtube

"""
	
	def __init__(self,  title, releasedate, story, poster, trailer_url):
		self.title = title
		self.releasedate = releasedate
		self.storyline = story
		self.poster_image = poster
		self.trailer_youtube_url = trailer_url

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url, autoraise=True)



