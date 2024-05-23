# MassYoutubeDownloader
Requirements:
```pip install yt-dlp```

## Usage
```
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
```

Obviously you can download single videos aswell
