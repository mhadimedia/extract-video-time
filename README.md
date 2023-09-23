# Extract Video Time: A Timecode Generator for Video Files

## Overview

**Extract Video Time** is a Python script designed to help you manage your video files more efficiently. If you've ever downloaded videos from cloud storage platforms like Google Drive, you'll know that Finder or other file management systems often don't display the exact recording date in the metadata. This script solves that problem by extracting and organizing your video files based on their recording date and time. 

Additionally, it converts these timestamps into a standardized timecode format, starting from a base time of 3 PM PST. This feature is particularly useful for video editors who need to sync multiple clips in a timeline.

## Features

- Extracts the recording date, hour, minute, and second from video metadata.
- Sorts video files in ascending order based on their recording time.
- Converts recording timestamps into a standardized timecode, starting from 3 PM PST as 00:00:00.

## Prerequisites

- The latest version of Python is installed
- Access to the video files you wish to process

## Installation

1. Download the Python script from this repository.
2. Place it in the directory where your video files are stored.

## Configuration

- Open the Python script in a text editor.
- Locate the `process_video_folder` variable and set its value to the path of the folder containing the videos you want to process.
- Optionally, you can change the default timezone by editing the relevant variable, or the default start time of 3 PM PST.

## Usage

1. Navigate to the directory where the Python script is located.
2. Run the script using the command `python timestamps.py`.
3. The script will process the videos in the specified folder and output a list of files sorted by their recording time, along with their corresponding timecodes.

## Example

If you have a video recorded at 3:15:34 PM PST, the script will generate a timecode of 00:15:34 for that video.

## Support

For any issues or feature requests, please open an issue on this GitHub repository.

## License

This project is open-source and available under the MIT License.

---

Feel free to contribute and make this tool even better!
