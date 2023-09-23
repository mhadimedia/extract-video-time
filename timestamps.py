import os
import subprocess
from pytz import timezone
from datetime import datetime
# Removed unused imports

pst = timezone('US/Pacific')
base_time = pst.localize(datetime.strptime("15:00:00", '%H:%M:%S'))

def get_creation_time(video_path):
    """Extracts the creation time of a video file."""
    command = ["mediainfo", "--Inform=General;%Encoded_Date%", video_path]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"mediainfo command failed: {result.stderr}")
        return None
    creation_time_str = result.stdout.strip()
    if not creation_time_str:
        print(f"Creation time not found for {video_path}")
        return None
    creation_time = datetime.strptime(creation_time_str, "%Y-%m-%d %H:%M:%S %Z")
    creation_time = creation_time.replace(tzinfo=timezone('UTC'))
    creation_time_pst = creation_time.astimezone(pst)
    return creation_time_pst

def get_timecode(creation_time):
    """Converts creation time to timecode."""
    time_diff = creation_time - base_time
    hours, remainder = divmod(time_diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def process_video_folder(folder_path):
    """Processes all video files in a folder and prints their timecodes."""
    print(f"Processing folder: {folder_path}")
    video_timecodes = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.mp4', '.mov')): # Edit the file formats as needed
            video_path = os.path.join(folder_path, filename)
            creation_time = get_creation_time(video_path)
            if creation_time:
                timecode = get_timecode(creation_time)
                video_timecodes.append((filename, timecode))
    video_timecodes.sort(key=lambda x: x[1])
    for filename, timecode in video_timecodes:
        print(f"{filename} {timecode}")

# Replace with the actual folder path
process_video_folder(r'your_folder_path_here')
