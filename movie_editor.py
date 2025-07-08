from moviepy.editor import (
    ImageClip,
    AudioFileClip,
    TextClip,
    CompositeVideoClip,
    concatenate_videoclips
)

def assemble_full_movie(scenes, voice_clips, image_clips):
    clips = []

    for i in range(len(scenes)):
        # Scene image
        img = ImageClip(image_clips[i]).set_duration(10)

        # Scene label overlay (e.g., (a), (b), (c)...)
        scene_label = f"({chr(97 + i)})"  # 'a' = 97, so scene 1 = (a)
        txt_clip = TextClip(scene_label, fontsize=40, color='white', font='Arial-Bold')
        txt_clip = txt_clip.set_position(('center', 'bottom')).set_duration(10)

        # Combine image with text label
        video = CompositeVideoClip([img, txt_clip])

        # Add voice clip
        audio = AudioFileClip(voice_clips[i])
        video = video.set_audio(audio)

        clips.append(video)

    # Stitch all scenes into one movie
    movie = concatenate_videoclips(clips, method="compose")
    output_path = "storage/final_movie.mp4"
    movie.write_videofile(output_path, fps=24)
    return output_path
