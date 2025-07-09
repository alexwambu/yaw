from moviepy.editor import (
    ImageClip,
    AudioFileClip,
    TextClip,
    CompositeVideoClip,
    concatenate_videoclips
)
import os

def assemble_full_movie(scenes, voice_clips, image_clips):
    clips = []

    # Safe Linux font path (works on Streamlit Cloud with packages.txt)
    FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

    for i in range(len(scenes)):
        img = ImageClip(image_clips[i]).set_duration(10)

        # Label format: (a), (b), (c)...
        scene_label = f"({chr(97 + i)})"

        try:
            txt_clip = TextClip(
                scene_label,
                fontsize=40,
                color='white',
                font=FONT_PATH
            ).set_position(('center', 'bottom')).set_duration(10)
        except Exception as e:
            print(f"TextClip error: {e}")
            txt_clip = None

        video = CompositeVideoClip([img, txt_clip] if txt_clip else [img])
        audio = AudioFileClip(voice_clips[i])
        video = video.set_audio(audio)
        clips.append(video)

    movie = concatenate_videoclips(clips, method="compose")
    output_path = "storage/final_movie.mp4"
    movie.write_videofile(output_path, fps=24)
    return output_path
