
##
#song tracker
#allows to track all songs
#drishti
#17
#06.07.26

songs = []

def add_songs():
    """Allows user to add song and running time"""

    song_name = input("Enter song name: ")

    while True:
        try:
            time = float(input("Enter running time (minutes): "))
            break
        except ValueError:
            print("Invalid choice, please enter a number.")

    new_song = {
        "song": song_name,
        "time": time
    }

    songs.append(new_song)
    print("Added")


def edit_song(name, time):
    """Allows user to edit the length of a song"""

    found = False

    for item in songs:
        if item["song"].lower() == name.lower():
            item["time"] = time
            print("Song updated")
            found = True
            break

    if not found:
        print("Song not found")


# Loop to keep menu running
running = True

while running:
    print("\nMenu")
    print("1. Add song")
    print("2. Edit song")

    choice = input("Enter a choice: ")

    if choice == "1":
        add_songs()

    elif choice == "2":
        song = input("Enter song name: ")
        new_time = float(input("Enter new length of song: "))
        edit_song(song, new_time)


    else:
        print("Invalid choice. Please try again.")
