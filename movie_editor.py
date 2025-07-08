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

    # Use system font path (common Linux-safe)
    FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

    for i in range(len(scenes)):
        # Load scene image
        img = ImageClip(image_clips[i]).set_duration(10)

        # Label like (a), (b), (c), ...
        scene_label = f"({chr(97 + i)})"

        # Text overlay for scene label
        txt_clip = TextClip(scene_label, fontsize=40, color='white', font=FONT_PATH)
        txt_clip = txt_clip.set_position(('center', 'bottom')).set_duration(10)

        # Combine image and label
        video = CompositeVideoClip([img, txt_clip])

        # Add voiceover audio
        audio = AudioFileClip(voice_clips[i])
        video = video.set_audio(audio)

        clips.append(video)

    # Concatenate all scenes into one final video
    movie = concatenate_videoclips(clips, method="compose")
    output_path = "storage/final_movie.mp4"
    movie.write_videofile(output_path, fps=24)
    return output_path
