import wave


#get started with audio files in python

#each signal has following parameters:
# ----------------------------------- # of channels (1--> mono, 2 --> stereo)
# ----------------------------------- sample width: # of bytes for each sample
# ----------------------------------- framerate / sample-rate: # of samples per second
# ----------------------------------- # of frames
# ----------------------------------- value of a frame
obj = wave.open("file_example_WAV_1MG.wav" , "rb" )
print("# of channels: ", obj.getnchannels())
print("obj width: ", obj.getsampwidth())
print("frame rate: ", obj.getframerate())
print("# of frames: ", obj.getnframes())
print("parameters: ", obj.getparams())

audio_duration = obj.getnframes() / obj.getframerate()

print(audio_duration)

frames = obj.readframes(-1)
print(type (frames), type (frames[0]))
print(len(frames))
obj.close()

#now lets create a wave audio file, and set params for it
obj_clone = wave.open("file_example_WAV_1MG_2.wav", "wb")
obj_clone.setnchannels(2)
obj_clone.setsampwidth(2)
obj_clone.setframerate(8000)
obj_clone.writeframes(frames)

print("duration: ", obj_clone.getnframes() / obj_clone.getframerate())

obj_clone.close()
