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


def delete_song(name):
    """Allows user to delete a song"""

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
    """Allows user to see running time of all songs"""

    total = 0

    for item in songs:
        total += item["time"]

    print("Total running time:", total, "minutes")


def view_songs():
    """Functionality to view all songs stored in list"""
    print("All songs")
    #loop over each item that is stored in the program
    for item in songs:
        print(item)
        

# Loop to keep menu running
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

        
 
