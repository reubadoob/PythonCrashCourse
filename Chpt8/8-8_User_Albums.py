def make_album(artist_name, album_title, tracks=None):
	"""Return a dictionary of an album's information."""
	album_dict = {
		'artist': artist_name.title(),
		'title': album_title.title(),
		}
	if tracks:
		album_dict['tracks'] = tracks
	return album_dict

albums = []

while True:
	print("\nPlease enter an album's artist and title. Enter 'q' at any time to quit. ")
	artist_name = input("Artist Name: ")
	if artist_name == 'q':
		break

	album_title = input("Album Title: ")
	if album_title == 'q':
		break

	album = make_album(artist_name, album_title)
	albums.append(album)

print("\nHere are the albums you have entered:")
for album in albums:
	print(album)