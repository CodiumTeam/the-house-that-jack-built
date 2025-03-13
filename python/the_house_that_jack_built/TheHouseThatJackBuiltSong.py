

class TheHouseThatJackBuiltSong:
    @classmethod
    def generate_song(cls):
        first = "the house that Jack built"
        second = "the malt that lay in"
        third = "the rat that ate"
        fourth = "the cat that killed"
        fifth = "the dog that worried"
        verses = [
            cls._generate_verse([first]),
            cls._generate_verse([second, first]),
            cls._generate_verse([third, second, first]),
            cls._generate_verse([fourth, third, second, first]),
            cls._generate_verse([fifth, fourth, third, second, first])
        ]
        return verses


    @classmethod
    def _generate_verse(cls, verse_block: list[str]):
        verse = ["This is"]
        for block in verse_block:
            verse.append(block)
        return ' '.join(verse) + '.'