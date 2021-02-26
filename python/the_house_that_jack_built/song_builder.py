
class SongBuilder:

    def __init__(self, sentences):
        self.sentences = sentences

    def regular(self):
        return f"This is {self.sentences[0]}.\nThis is {self.sentences[1]} {self.sentences[0]}."
