import os
from moviepy.editor import *

# Change the following with your folders paths
input_folder_path = 'C:\\Users\\USER\\OneDrive\\Downloads\\AllVideosRepaired'
output_folder_path = 'C:\\Users\\USER\\OneDrive\\Downloads\\VideosConvertedToMP4'


os.makedirs(output_folder_path, exist_ok=True)

def convert_to_mp4(input_path, output_path):
    try:
        video = VideoFileClip(input_path)
        output_file = os.path.splitext(os.path.basename(input_path))[0] + '.mp4'
        output = os.path.join(output_path, output_file)
        video.write_videofile(output, codec='libx264', audio_codec='aac')
        video.close()
        return True
    except Exception as e:
        print(f"Error converting {input_path}: {e}")
        return False


video_files = [f for f in os.listdir(input_folder_path) if f.endswith('.webm')]

# Convert each video file to MP4
for video_file in video_files:
    input_file_path = os.path.join(input_folder_path, video_file)
    success = convert_to_mp4(input_file_path, output_folder_path)
    if success:
        print(f"Converted {video_file} successfully.")
    else:
        print(f"Failed to convert {video_file}.")

print("All videos converted.")
