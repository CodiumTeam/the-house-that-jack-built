import unittest
from the_house_that_jack_built.song_builder import SongBuilder

class KataTest(unittest.TestCase):

    def test_single(self):
        sentences = ['the house that Jack built',
                     'the malt that lay in',
                     'the rat that ate',
                     'the cat that killed',
                     'the dog that worried']

        s = SongBuilder(sentences)
        r = s.regular()
        self.assertEqual(r, "This is the house that Jack built.\nThis is the malt that lay in the house that Jack built.")


        # [0,1,0,2,1,0,3,2,1,0,4,3,2,1]


        # s.reverse()
        # s.echo()
        #
        #
        # song()
        # regular()
        #
        # s = new regularSong()
        # s.display()
        #
        # s = new reverseSong()
        # s.display()
        #
        # s = new echoSong()
        # s.display()



