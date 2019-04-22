from pydub import AudioSegment
sound = AudioSegment.from_mp3(SampleAudio.mp3)
sound.export(OutputAudio.wav,format="wav")

