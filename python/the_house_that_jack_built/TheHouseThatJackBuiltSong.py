

class TheHouseThatJackBuiltSong:
    @classmethod
    def generate_song(cls, song_type: str):
        blocks = [
            "the house that Jack built",
            "the malt that lay in",
            "the rat that ate",
            "the cat that killed",
            "the dog that worried"
        ]

        if song_type == 'reverse':
            blocks.reverse()

        verses = [cls._generate_verse(blocks, i) for i in range(1, len(blocks) + 1)]

        return verses


    @classmethod
    def _generate_verse(cls, blocks: list[str], verse_number):
        verse = []
        for index in range(verse_number):
            verse.insert(0, blocks[index])
        return "This is " + ' '.join(verse) + '.'