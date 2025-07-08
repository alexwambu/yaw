from moviepy.editor import *

def assemble_full_movie(scenes, voice_clips, image_clips):
    clips = []

    for i in range(len(scenes)):
        img = ImageClip(image_clips[i]).set_duration(10)
        audio = AudioFileClip(voice_clips[i])
        img = img.set_audio(audio)
        clips.append(img)

    movie = concatenate_videoclips(clips, method="compose")
    output_path = "storage/final_movie.mp4"
    movie.write_videofile(output_path, fps=24)
    return output_path
