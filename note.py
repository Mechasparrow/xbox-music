class Note(object):
    def __init__(self):
        self.notes = {"A": 440, "B": 493.88, "C": 523.25, "D": 587.33, "E": 659.26, "F": 698.46, "G": 783.99, "A2": 880}
        pass;
    def note(self, note):
        return self.notes[note]
