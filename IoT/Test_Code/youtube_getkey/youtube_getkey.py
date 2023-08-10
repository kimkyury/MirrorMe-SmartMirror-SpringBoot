import requests

youtube_url = "https://www.googleapis.com/youtube/v3/search"

params = {
          "key": "AIzaSyDTwgayRnYmoB4oqElnAXtl6fsUgOw1c4w",
          "part": "snippet",
          "type": "video",
          "q": "요가 영상",
        }

result = requests.get(  youtube_url,
                        params=params)

# data = json.loads(result.json())

# data['items'][0]['id']['videoId']

print(result.json()['items'][0]['id']['videoId'])
