import yt_dlp
import os
def download_youtube_video(url,output_path="Downloads"):
    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        
        ydl_opts ={
            'format': 'bestvideo+bestaudio/best',

            'outtmpl':f'{output_path}/%(title)s.%(ext)s',
            'noplaylist': True,
        }
        print(f"downloading:{url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Download completed and the video saved to {output_path}")

    

    except yt_dlp.utils.DownloadError as de:
        print(f"Download error: {str(de)}")
        print("\nhere are the available formats..")
        try:
            with yt_dlp.YoutubeDL({'listformats': True}) as ydl:
                ydl.download([url])
        except Exception as e:
            print(f"Failed to list formats: {str(e)}")
    except Exception as e:
        print(f"An error occured: {str(e)}")


if __name__ == "__main__":
    video_url =input("Enter thy youtube url: ")
    download_youtube_video(video_url)