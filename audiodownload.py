import subprocess
import re
import random
import shutil

## DOWNLOAD YTDLP, pip install yt-dlp

class YoutubeDownloader:
    def __init__(self) -> None:
        """This realistically should work with any webpage with a link but youtube works best"""
        pass

    @staticmethod
    def getVideoTitle(url:str, ytDLP:str="yt-dlp.exe"):
        """Gets the video title of a current URL"""
        command = [ytDLP, '--get-title', url]
        
        try:
            result = subprocess.run(command, capture_output=True, text=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print("Error:", e)
            return None
        
    @staticmethod
    def downloadAudio(url: str, ytDLP: str = "yt-dlp.exe", output:str=""):
        """
            Downloads the audio from a specific url, NOTE This should work with any webpage but gl
            Returns success and the location of the dowloaded file
        """
        title = YoutubeDownloader.getVideoTitle(url)
        if title.strip() == "":
            title = str(random.randint(1111,9999))

        output_file = re.sub(r'[<>:"/\\|?*]', '', title) + ".mp3" # Clean the title
        command = [ytDLP, "--extract-audio", "--audio-format", "mp3", "--output", output_file, url]
            
        try:
            subprocess.run(command, check=True)
            if output != "":
                shutil.move(output_file,output)
            return True, output_file
        except subprocess.CalledProcessError as e:
            print("Error:", e)
            return False, None

# Example usage:
if __name__ == "__main__":
    # Mainly used for mass downloading videos
    urls = [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    ]

    for url in urls:
        downloaded_file = YoutubeDownloader.downloadAudio(url,output="aa")
        print(downloaded_file)