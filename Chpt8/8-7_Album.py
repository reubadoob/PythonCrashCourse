def make_album(artist_name, album_title, tracks=None):
	"""Return a dictionary of an album's information."""
	album_dict = {
		'artist': artist_name.title(),
		'title': album_title.title(),
		}
	if tracks:
		album_dict['tracks'] = tracks
	return album_dict

album_1 = make_album('michael jackson', 'thriller')
album_2 = make_album('the beatles', 'abbey road', 15)
album_3 = make_album('beyonce', 'lemonade', 11)

print(album_1)
print(album_2)
print(album_3)