##
#song tracker
#allows to track all songs
#drishti
#17
#06.07.26

songs = []
def add_songs():
    """allows user to add song and running time"""
    
    song_name = input("Enter song name: ")
    time = int(input("Enter running time (minutes): "))

    new_song = {
        "song": song_name,
        "time": time
    }
 
    songs.append(new_song)
    print("added")

add_songs()
print(songs)
