# For local storage
set LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true
set LOCAL_FILES_SERVING_ENABLED=true
set LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT=D:\\label_studio_DCT\\storage

# youtube videos
## yt-dlp
pip install yt-dlp

yt-dlp -f "bestvideo[ext=mp4]" "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"

## extract frames
ffmpeg -i downloaded_video.mp4 -q:v 2 -vf "fps=30" frames/frame_%04d.png

https://www.youtube.com/watch?v=ZmxRbXUW-iU

finally
```sh 
ffmpeg -i "D:\label_studio_DCT\storage\videos\hazz1\The Quest Between Safa And Marwa January 6 2023 4K Stock Video - Download Video Clip Now - Mecca, Islam, Hajj - iStock.mp4" -vsync 0 output_frames/frame_%04d.png
```


# flask + model
conda install flask
pip install ultralytics