"""Manage a music playlist by adding, editing, deleting, and viewing songs."""

# Song tracker.
# Allows the user to track all songs.
# Drishti.
# 17.
# 06.07.26.

songs = []


def add_songs():
    """Add a song and its running time."""
    song_name = input("Enter song name: ")

    while True:
        try:
            time = float(input("Enter running time (seconds): "))
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
    """Edit the length of a song."""
    found = False

    for item in songs:
        if item["song"].lower() == name.lower():
            item["time"] = time
            print("Song updated")
            found = True
            break

    if not found:
        print("Song not found")


def delete_song(name):
    """Delete a song from the playlist."""
    found = False

    for i in range(len(songs)):
        if songs[i]["song"].lower() == name.lower():
            del songs[i]
            print("Song deleted")
            found = True
            break

    if not found:
        print("Song not found")


def total_time():
    """Display the running time of a selected song."""
    song_name = input("Enter song name: ")

    found = False

    for item in songs:
        if item["song"].lower() == song_name.lower():
            print(item["song"], "is", item["time"], "seconds long.")
            found = True
            break

    if not found:
        print("Song not found.")


songs = [
    {"song": "Cruel Summer", "time": 230},
    {"song": "Espresso", "time": 175},
    {"song": "Birds of a Feather", "time": 210},
    {"song": "Iris", "time": 200}
]


def view_songs():
    """Display all songs in the playlist."""
    if len(songs) == 0:
        print("No songs in playlist.")
    else:
        print("\nPlaylist")
        for item in songs:
            print(f"Song: {item['song']}")
            print(f"Time: {item['time']} seconds")
            print("-" * 20)


# Loop to keep the menu running.
running = True

while running:
    print("\nMenu")
    print("A. Add song")
    print("E. Edit song")
    print("D. Delete song")
    print("T. Time of songs")
    print("P. Print all songs")
    print("Q. Quit")

    choice = input("Enter a choice: ")

    if choice == "A":
        add_songs()

    elif choice == "E":
        song = input("Enter song name: ")
        new_time = float(input("Enter new length of song: "))
        edit_song(song, new_time)

    elif choice == "D":
        song = input("Enter song name: ")
        delete_song(song)

    elif choice.upper() == "T":
        total_time()

    elif choice.upper() == "P":
        view_songs()

    elif choice == "Q":
        running = False
        print("Goodbye!")

    else:
        print("Invalid choice. Please try again.")


        
 
