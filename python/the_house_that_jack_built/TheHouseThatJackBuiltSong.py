

class TheHouseThatJackBuiltSong:
    @classmethod
    def generate_song(cls, song_type: str):
        first = "the house that Jack built"
        second = "the malt that lay in"
        third = "the rat that ate"
        fourth = "the cat that killed"
        fifth = "the dog that worried"

        if song_type == 'regular':
            verses = [
                cls._generate_verse([first]),
                cls._generate_verse([second, first]),
                cls._generate_verse([third, second, first]),
                cls._generate_verse([fourth, third, second, first]),
                cls._generate_verse([fifth, fourth, third, second, first])
            ]
        else:
            verses = [
                cls._generate_verse([fifth]),
                cls._generate_verse([fourth, fifth]),
                cls._generate_verse([third, fourth, fifth]),
                cls._generate_verse([second, third, second, fifth]),
                cls._generate_verse([first, fourth, third, fourth, fifth])
            ]
        return verses


    @classmethod
    def _generate_verse(cls, verse_block: list[str]):
        verse = ["This is"]
        for block in verse_block:
            verse.append(block)
        return ' '.join(verse) + '.'