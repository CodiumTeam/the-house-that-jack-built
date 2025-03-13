

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

        verses = [
            cls._generate_verse(blocks, 1),
            cls._generate_verse(blocks, 2),
            cls._generate_verse(blocks, 3),
            cls._generate_verse(blocks, 4),
            cls._generate_verse(blocks, 5)
        ]
        return verses


    @classmethod
    def _generate_verse(cls, blocks: list[str], verse_number):
        verse = ["This is"]
        for block in range(verse_number - 1, -1, -1):
            verse.append(blocks[block])
        return ' '.join(verse) + '.'