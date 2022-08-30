from ntpath import join
import wave
import pyaudio

#set params for new audio that will be recorded
FRAMES_PER_BUFFER = 3200
CHANNELS = 1
FORMAT = pyaudio.paInt16
RATE = 16000

#create a pyAudio object
p = pyaudio.PyAudio()

#set params to the pyAudio object
stream = p.open(
    frames_per_buffer= FRAMES_PER_BUFFER,
    rate = RATE,
    channels= CHANNELS,
    format=FORMAT,
    input= True
)

print("Start recording ...")

#set recording time to second so you can change it later
#we are going to store frames in an array called frames
second = 5
frames = []

#append recieved frames to frames array for 5 seconds
for i in range (0, int(RATE/FRAMES_PER_BUFFER*second)) :
    data = stream.read(FRAMES_PER_BUFFER)
    frames.append(data)

#stop recording
stream.stop_stream()
stream.close()
p.terminate()

#export the recorded audio as "output.wav" file and set params for it
obj = wave.open("output.wav", "wb")
obj.setnchannels(CHANNELS)
obj.setframerate(RATE)
obj.setsampwidth(p.get_sample_size(FORMAT))
obj.writeframes(b"".join(frames))
obj.close()