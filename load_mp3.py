from pydub import AudioSegment

#export wave file as an mp3 file
audio = AudioSegment.from_wav("file_example_WAV_1MG.wav").export("output.mp3", format="mp3")
#print Done to make sure that our program works
print("Done.")