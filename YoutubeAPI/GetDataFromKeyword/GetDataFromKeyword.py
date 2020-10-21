#Importing build library from apiclient library and youtube as an object
from apiclient.discovery import build
#Enter your API Key
api = ""
youtube = build('youtube','v3',developerKey = api)
type(youtube)

#Function to get top 50 video search results for each keyword and write them to Main.csv file
def get_data_from_keyword(key) :
    res = youtube.search().list(q = key, part = 'snippet', type = 'video',maxResults = 50).execute()
    import csv
    with open('Main.csv','a+', newline='',encoding="utf-8") as f:
         fieldnames = ['Video ID','Channel Name', 'Channel ID']
         writer = csv.DictWriter(f,fieldnames = fieldnames)
        
         for item in res['items'] :
              print(item['snippet']['channelId'],item['snippet']['channelTitle'],item['id']['videoId'])
              writer.writerow({'Video ID' :item['id']['videoId'],
                               'Channel Name' :item['snippet']['channelTitle'],
                               'Channel ID' : item['snippet']['channelId']})
#To take the input of keywords from Input.csv file
import csv
X = [] 
with open("Input.csv") as csvfile:
    inputcsv = csv.reader(csvfile, delimiter=',')
    for row in inputcsv:
        X.append(row[0])
len(X)
for i in range(len(X)):
    print(X[i])
    key = get_data_from_keyword(X[i])



            

              
              
    
   
