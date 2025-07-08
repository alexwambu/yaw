from PIL import Image
import io
import os

def generate_scene_image(scenes, uploaded_images):
    os.makedirs("storage", exist_ok=True)
    images = []

    for i, scene in enumerate(scenes):
        img_index = i % len(uploaded_images)
        img_bytes = uploaded_images[img_index].read()
        img = Image.open(io.BytesIO(img_bytes)).resize((1280, 720))
        img_path = f"storage/scene_{scene['id']}.png"
        img.save(img_path)
        images.append(img_path)

    return images
