class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Not recognized format")
        self.filename = filename

    def play(self):
        raise NotImplementedError("Subclass must be implement")

class MP3File(AudioFile):
    ext = "mp3"

    def play(self):
        print("Playing {self.filename} as mp3")

class WAVFile(AudioFile):
    ext = "wav"

    def play(self):
        print("Playing {self.filename} as wav")

class FLACFile:
    ext = "flac"
    def __int__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Not recognized format")
        self.filename = filename

    def play(self):
        print(f"Playing {self.filename} as flac")