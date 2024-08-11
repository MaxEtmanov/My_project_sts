import whisper
from pprint import pprint
import time
import matplotlib.pyplot as plt


def score_time(model):
    model = whisper.load_model(model)
    start = time.time()
    result = model.transcribe("manager.mp3")
    end = time.time()
    return end - start


models = ["tiny", "base", "small", "medium", "large"]

times = []
for model in models:
    transcription_time = score_time(model)
    times.append(transcription_time)
    print(f"{model} model: {transcription_time:.2f} seconds")
    
    
plt.figure(figsize=(10, 6))
plt.bar(models, times)
plt.title("срванение скорости")
plt.xlabel("модель")
plt.ylabel("время")
plt.show()
