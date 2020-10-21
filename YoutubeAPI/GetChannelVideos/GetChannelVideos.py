#Importing build library from apiclient library and youtube as an object
from apiclient.discovery import build
#Enter your API Key
api = ""
youtube = build('youtube','v3',developerKey = api)
type(youtube)

#DateTime Datatype with required format
from datetime import datetime
start = datetime(year = 2018,month = 10,day= 1).strftime('%Y-%m-%dT%H:%M:%SZ')
end = datetime(year = 2019,month = 10,day= 1).strftime('%Y-%m-%dT%H:%M:%SZ')

#Function to get videos of the whole channel and each video's attributes
def get_channel_videos(channel):
    rest= youtube.channels().list(id = channel,part = 'contentDetails').execute()
    playlistID =rest['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    
    vid = []
    next_page_token = None
    while 1 :
         play =  youtube.playlistItems().list(playlistId = playlistID,part = 'snippet',maxResults = 50,pageToken = next_page_token).execute()
         vid += play['items']
         next_page_token = play.get('nextPageToken')
         if next_page_token is None :
            break
    
    #To export the strings to .csv file under their respective Headers
    import csv
    with open(f'{channel}.csv','a+', newline='',encoding="utf-8") as f:
         fieldnames = ['Titles','Thumbnail URL', 'Video ID' ,'PublishedAt','Description','Views','Likes','Dislikes','Comments']
         writer = csv.DictWriter(f,fieldnames = fieldnames)
         writer.writeheader()
         for item in vid :
              print(item['snippet']['title'],item['snippet']['thumbnails']['default']['url'] , item['snippet']['resourceId']['videoId'] , item['snippet']['description'])
              X = item['snippet']['resourceId']['videoId']
              rest= youtube.videos().list(id = X, part = 'statistics').execute()
              print(rest['items'][0]['statistics']['viewCount'])
              writer.writerow({'Titles' : item['snippet']['title'] ,
                               'Thumbnail URL' : item['snippet']['thumbnails']['default']['url'],
                               'Video ID' :  item['snippet']['resourceId']['videoId'],
                               'PublishedAt' : item['snippet']['publishedAt'],
                               'Description' : item['snippet']['description'], 
                               'Views' : rest['items'][0]['statistics']['viewCount'],
                               'Likes' : rest['items'][0]['statistics']['likeCount'],
                               'Dislikes' : rest['items'][0]['statistics']['dislikeCount'],
                               'Comments' : rest['items'][0]['statistics']['commentCount']})


#To take the input of VideoID's from Input.csv file
import csv
X = [] 
with open("Input.csv") as csvfile:
    inputcsv = csv.reader(csvfile, delimiter=',')
    for row in inputcsv:
        X.append(row[0])
len(X)
for i in range(len(X)):
    print(X[i])
    vid = get_channel_videos(X[i])