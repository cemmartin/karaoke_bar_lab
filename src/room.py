class Room:
    def __init__(self, input_name): #input name should connect to a name in Guests (I believe)
        self.name = input_name
        self.singers = [] #might want to use guest here
        self.songs = []

    def add_guest_to_room(self, input_singer):
        self.singers.append(input_singer) #adds a singer to the list

    def kick_guest_from_room(self, input_singer):
        self.singers.remove(input_singer) #remove singer from the list

    def add_songs_to_room(self, input_song): #should this have two parameters?
        self.songs.append(input_song)





