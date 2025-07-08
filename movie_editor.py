from moviepy.editor import *

def assemble_full_movie(scenes, voice_clips, image_clips):
    clips = []

    for i in range(len(scenes)):
        # Main scene image
        img = ImageClip(image_clips[i]).set_duration(10)

        # Scene label text (e.g., "(b)" or "Scene 2")
        scene_label = f"Scene {i + 1}"  # or "(b)", "(c)" if custom
        txt_clip = TextClip(scene_label, fontsize=40, color='white', font='Arial-Bold')
        txt_clip = txt_clip.set_position(('center', 'bottom')).set_duration(10)

        # Combine image with text
        composite = CompositeVideoClip([img, txt_clip])

        # Add voice
        audio = AudioFileClip(voice_clips[i])
        composite = composite.set_audio(audio)

        clips.append(composite)

    # Concatenate all scene clips
    movie = concatenate_videoclips(clips, method="compose")
    output_path = "storage/final_movie.mp4"
    movie.write_videofile(output_path, fps=24)
    return output_path
