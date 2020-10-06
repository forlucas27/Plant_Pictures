# Plant Pictures posted to Twitter

import sys
import os
import tweepy
import cv2
from VideoCapture import Device

videoCaptureObject = cv2.VideoCapture(0)
result = True
while(result):
    ret,frame = videoCaptureObject.read()
    cv2.imwrite("NewPicture.jpg",frame)
    result = False
videoCaptureObject.release()
cv2.destroyAllWindows()
 

twitter_auth_keys = { 
    "consumer_key"        : "shpSVvF0zvzUNuBmRCAI2VRtI",
    "consumer_secret"     : "7WYCHOPR0RpXW4MSYb67f7gMWB7knCyfVGEMSW9B3wttQQlQTv",
    "access_token"        : "1313166944099422208-8iv7tVnAvUN1DPD5oIjX1lJ0xBQDAL",
    "access_token_secret" : "cPBRvdoQueGzxlwP4pv627hEElPpupqNdP8vhlWAgmLnn"
}
 
auth = tweepy.OAuthHandler(
        twitter_auth_keys['consumer_key'],
        twitter_auth_keys['consumer_secret']
        )
auth.set_access_token(
        twitter_auth_keys['access_token'],
        twitter_auth_keys['access_token_secret']
        )
api = tweepy.API(auth)
 
# Upload image
photo = open('NewPicture.jpg','rb')
media = api.media_upload('NewPicture.jpg')

import requests 
from bs4 import BeautifulSoup 
  
URL = 'http://www.keepinspiring.me/famous-quotes/'
response = requests.get(URL) 
  
response.raise_for_status()
html_contents = response.text
soup = BeautifulSoup(html_contents, 'html.parser')

quote_divs = soup.find_all('div', class_='author-quotes')
quotes = [div.text.strip() for div in quote_divs]

# Print out extracted contents for now.
j = len(quotes)
print(quotes[j-1])
#for i, quote in enumerate(quotes):
    #print(i, quote)
 
# Post tweet with image
tweet = quotes[j-1]
post_result = api.update_status(status=tweet, media_ids=[media.media_id])