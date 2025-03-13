import unittest

from python.the_house_that_jack_built.TheHouseThatJackBuiltSong import TheHouseThatJackBuiltSong


class KataTest(unittest.TestCase):

    def test_regular_song_generates_first_verse(self):
        verses = TheHouseThatJackBuiltSong().generate_song()

        self.assertEqual("This is the house that Jack built.", verses[0])

    def test_regular_song_generates_second_verse(self):
        expected_verses = "This is the malt that lay in the house that Jack built."
        verses = TheHouseThatJackBuiltSong().generate_song()

        self.assertEqual(expected_verses, verses[1])
