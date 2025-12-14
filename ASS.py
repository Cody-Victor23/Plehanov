# pip install sounddevice
# pip install numpy
# pip install SpeechRecognition
# pip install SpeechRecognition[google-cloud]

import sounddevice as sd
import numpy as np
import speech_recognition as sr
import io
import wave

duration = 5 #sec
sample_rate = 44100 #hz

record = sd.rec(
    int(duration * sample_rate), 
    samplerate=sample_rate,
    channels=1,
    dtype="float32"
    )
sd.wait()

print(record)