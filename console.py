import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist1 = Artist("Andrew Bird")
artist_repository.save(artist1)
artist2 = Artist("Blur")
artist_repository.save(artist2)

found_artist = artist_repository.select(artist1.id)
print(found_artist.__dict__)

album1 = Album("My Finest Work Yet", "Indie", artist1)
album_repository.save(album1)
album2 = Album("Are You Serious", "Indie", artist1)
album_repository.save(album2)
album3 = Album("13", "BritPop", artist2)
album_repository.save(album3)
album4 = Album("Leisure", "BritPop", artist2)
album_repository.save(album4)

found_album = album_repository.select(album1.id)
print(found_album.__dict__)

found_all_artists = artist_repository.select_all()
for artist in found_all_artists:
    print(artist.__dict__)

found_all_albums = album_repository.select_all()
for album in found_all_albums:
    print(album.__dict__)

albums_by_artist = album_repository.select_by_artist(artist1.id)
for album in albums_by_artist:
    print(album.__dict__)

artist2.change_name("Gorillaz")
artist_repository.update(artist2)
updated_artist = artist_repository.select(artist2.id)
print(updated_artist.__dict__)

album3.change_title("Plastic Beach")
album_repository.update(album3)
updated_album = album_repository.select(album3.id)
print(updated_album.__dict__)

album_repository.delete(album3.id)
album_repository.delete(album4.id)
show_deleted_album = album_repository.select_all()
for album in show_deleted_album:
    print(album.__dict__)

artist_repository.delete(artist2.id)
show_deleted_artist = artist_repository.select_all()
for artist in show_deleted_artist:
    print(artist.__dict__)

pdb.set_trace()