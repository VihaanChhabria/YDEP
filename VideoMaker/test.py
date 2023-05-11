r"""from yt_dlp import YoutubeDL

ydl_opts = {'outtmpl': r'C:\Users\vihaa\YDEP\VideoMaker'}

with YoutubeDL(ydl_opts) as ydl: 
  info_dict = ydl.extract_info('https://www.youtube.com/watch?v=92IHEchAp1k', download=True)
  video_url = info_dict.get("url", None)
  video_id = info_dict.get("id", None)
  video_title = info_dict.get('title', None)
  print("Title: " + video_title) # <= Here, you got the video title"""

my_str = 'Missing Mum  Daddy Putdown  Bluey [5ZeTlI1kINE].webm'

separator = ' ['

result = my_str.split(separator, 1)[0]
print(result)  # 👉️ 'bobby'