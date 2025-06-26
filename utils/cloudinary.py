import cloudinary
import cloudinary.uploader
import os
from dotenv import load_dotenv

load_dotenv()

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

def upload_mp3(file):
    result = cloudinary.uploader.upload(
        file,
        resource_type="video",  # Use "video" to allow audio files
        folder="music_uploads",
        public_id=file.filename.rsplit('.', 1)[0],
        format="mp3"
    )
    return result["secure_url"]