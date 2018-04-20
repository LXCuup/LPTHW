class Song():

    def __init__(self, lyrics):
    	self.lyrics = lyrics

    def sing_me_a_song(self):
    	for line in self.lyrics:
    		print (line)

    def print_song(self):
    	print ("\nlyrics of song.\n")

happy_bday = ["Happy birthday to you",
				 "I don't want to get sued",
				 "So I'll stop right there"]

bulls_on_parade = ["They rally around tha family",
					"With pockets full of shells",
                    "It a nice day."]

happy = Song("ASDF")
happy.sing_me_a_song()
happy.print_song()

Song(happy_bday).sing_me_a_song()

Song(happy_bday).print_song()

Song(bulls_on_parade).sing_me_a_song()

