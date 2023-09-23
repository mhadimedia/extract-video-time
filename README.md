# Extract Video Time: Timecode Generator for Video Files

## Overview

**Extract Video Time** is a Python script designed to manage video files by extracting their recording date and time, sorting them, and converting these timestamps into a standardized timecode format. Ideal for video editors and content creators who need to sync multiple clips in a timeline.

## Features

- Extracts recording date and time from video metadata.
- Sorts video files based on their recording time.
- Converts recording timestamps into a standardized timecode.

## Prerequisites

- Python 3.x
- `mediainfo` command-line utility
- Python packages: `pytz`, `hachoir`

## Installation

### Dependencies

1. Install `mediainfo`:

    ```bash
    sudo apt-get install mediainfo  # For Ubuntu
    brew install mediainfo          # For macOS
    ```

2. Install required Python packages:

    ```bash
    pip install pytz hachoir
    ```

### Setup

1. Clone this repository or download the Python script.
2. Place the script in the directory containing the video files you want to process.

## Configuration

1. Open the Python script in a text editor.
2. Update the `process_video_folder` variable with the path to your video folder.
3. Optionally, you can change the default timezone by modifying the `pst` variable.

## Usage

1. Open a terminal and navigate to the directory containing the Python script.
2. Run the script:

    ```bash
    python timestamps.py
    ```

3. The script will output a list of video files sorted by their recording time, along with their corresponding timecodes.

## Example

A video recorded at 3:15:34 PM PST will generate a timecode of 00:15:34.

## Support

For issues, feature requests, or contributions, please open an issue or pull request on this GitHub repository.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details
