import unittest

from python.the_house_that_jack_built.TheHouseThatJackBuiltSong import TheHouseThatJackBuiltSong


class KataTest(unittest.TestCase):

    def test_regular_song_generates_first_verse(self):
        verses = TheHouseThatJackBuiltSong().generate_song()

        self.assertEqual("This is the house that Jack built.", verses[0])
