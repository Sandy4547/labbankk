from audio import MP3File, WAVFile, FLACFile

mp3 = MP3File("audio.mp3")
mp3.play()

wav = WAVFile("audio.wav")
wav.play()

flac = FLACFile("audio.flac")
flac.play()