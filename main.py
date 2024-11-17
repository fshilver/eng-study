import json

from openai import OpenAI

client = OpenAI()

audio_file = open("audio.mp3", "rb")
response = client.audio.transcriptions.create(
    model="whisper-1", file=audio_file, timestamp_granularities=["segment"], language="en", response_format="verbose_json"
)

data = []
for segment in response.segments:
    data.append({"start": segment.start, "end": segment.end, "text": segment.text})

json.dump(data, open("transcription.json", "w"), indent=4)

# TranscriptionVerbose
# {
#     "duration": 287.9800109863281,
#     "language": "english",
#     "text": "All right, let's get started. ...",
#     "segments": [
#         {
#             "id": 0,
#             "avg_logprob": -0.22449339926242828,
#             "compression_ratio": 1.7084745168685913,
#             "end": 3.359999895095825,
#             "no_speech_prob": 0.03787604719400406,
#             "seek": 0,
#             "start": 0.0,
#             "temperature": 0.0,
#             "text": " All right, let's get started.",
#             "tokens": [
#                 50364,
#                 1057,
#                 558,
#                 11,
#                 718,
#                 311,
#                 483,
#                 1409,
#                 13,
#                 50532
#             ]
#         },
