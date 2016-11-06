import numpy as np
import simpleaudio as sa

class Soundgenerator():
    def __init__(self, freq, soundtype = "sine", sample_rate = 44100):
        self.sample_rate = sample_rate
        if (soundtype == "sine"):
            self.generateSine(freq)
        pass

    def generateSine(self, freq):
        sample_rate = 44100
        T = 0.2
        t = np.linspace(0, T, T * sample_rate, False)

        # generate sine wave notes
        note = np.sin(freq * t * 2 * np.pi)

        # concatenate notes
        audio = np.hstack((note))
        # normalize to 16-bit range
        audio *= 32767 / np.max(np.abs(audio))
        # convert to 16-bit data
        audio = audio / 16
        audio = audio.astype(np.int16)

        self.audio = audio

    def playsound(self):
        play_obj = sa.play_buffer(self.audio, 1, 2, self.sample_rate)
        play_obj.wait_done()
        pass
