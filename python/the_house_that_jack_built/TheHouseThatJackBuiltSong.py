

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
            cls._generate_verse([blocks[0]]),
            cls._generate_verse([blocks[1], blocks[0]]),
            cls._generate_verse([blocks[2], blocks[1], blocks[0]]),
            cls._generate_verse([blocks[3], blocks[2], blocks[1], blocks[0]]),
            cls._generate_verse([blocks[4], blocks[3], blocks[2], blocks[1], blocks[0]])
        ]
        return verses


    @classmethod
    def _generate_verse(cls, verse_block: list[str]):
        verse = ["This is"]
        for block in verse_block:
            verse.append(block)
        return ' '.join(verse) + '.'