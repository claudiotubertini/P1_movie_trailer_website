import media
import fresh_tomatos

space_odissey = media.Movie("2001 A Space Odissey",
				"1968",
				"During a mysterious space mission, the ship's computer system, HAL, "
				"begins to display increasingly strange behavior, leading up to a tense "
				"showdown between man and machine that results in a mind-bending trek "
				"through space and time in search of human knowledge.",
				"http://gvshp.org/blog/wp-content/uploads/2014/04/2001-Space-Odyssey_11.jpg",
				"https://youtu.be/XHjIqQBsPjk")
annie_hall = media.Movie("Annie Hall",
				"1977",
				"Comedian Alvy Singer examines the rise and fall of his relationship with "
				"struggling nightclub singer Annie Hall.", 
				"https://upload.wikimedia.org/wikipedia/en/e/e6/Anniehallposter.jpg",
				"https://youtu.be/OqVgCfZX-yE")
shane = media.Movie("Shane",
				"1953",
				"Enigmatic gunslinger Shane rides into a small Wyoming town with "
				"hopes of quietly settling down as a farmhand. Taking a job on homesteader "
				"Joe Starrett's farm, Shane is drawn into a battle between the townsfolk "
				"and ruthless cattle baron Rufus Ryker.",
				"https://upload.wikimedia.org/wikipedia/en/a/a0/Shaneposter.png",
				"https://youtu.be/SWdPmapuOd4")
blade_runner = media.Movie("Blade Runner",
				"1982",
				"Deckard is forced by the police Boss to continue his old job "
				"as Replicant Hunter. His assignment: eliminate four escaped "
				"Replicants from the colonies who have returned to Earth.",
				"https://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg",
				"https://youtu.be/eogpIG53Cis")
matrix = media.Movie("Matrix",
				"1999",
				"Neo believes that Morpheus, an elusive figure considered to be the most "
				"dangerous man alive, can answer his question -- What is the Matrix? "
				"Neo is contacted by Trinity, who leads him into an underworld "
				"where he meets Morpheus.",
				"http://t0.gstatic.com/images?q=tbn:ANd9GcQq3pIz-aKgkmYX1dJ-EL-AlHSPcOO7wdqRIJ5gJy9qNinXpmle",
				"https://youtu.be/m8e-FF8MsqU")
trois_couleurs_bleu = media.Movie("Trois couleurs: Bleu",
				"1993",
				"Julie is haunted by her grief after living through a tragic auto wreck "
				"that claimed the life of her composer husband and young daughter.",
				"http://www.gstatic.com/tv/thumb/movieposters/15793/p15793_p_v7_aa.jpg",
				"https://youtu.be/Hxu6my_t4pM")

movies = [shane, space_odissey, trois_couleurs_bleu, annie_hall,  blade_runner, matrix]
fresh_tomatos.open_movies_page(movies)
