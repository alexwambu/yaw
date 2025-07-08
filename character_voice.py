from gtts import gTTS
import os

def generate_voice_per_scene(scenes):
    voice_paths = []
    os.makedirs("storage", exist_ok=True)

    for scene in scenes:
        speech = scene['text'][:500]
        tts = gTTS(speech)
        path = f"storage/voice_{scene['id']}.mp3"
        tts.save(path)
        voice_paths.append(path)

    return voice_paths
