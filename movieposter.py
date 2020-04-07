import os
import re
import sys
from tkinter import messagebox, Tk
from urllib.request import urlopen
from PIL import Image
import webbrowser
 
from bs4 import BeautifulSoup
import pyperclip
import requests
 
def error():
    messagebox.showerror('Error', 'Please copy a valid movie url to the clipboard')
    sys.exit()
 
# Stop ugly default tk window appearing if error message box is used.
root = Tk()
root.withdraw()
 
# Get URL of film from clipboard.
movie_url = pyperclip.paste()
 
# Show error and quit if not imdb address.
if not(movie_url.startswith('https://www.imdb.com/title/') or  movie_url.startswith('https://alternativemovieposters.com/')):
    error()
 
# Read the html source code from the URL.
html = urlopen(movie_url)
btfl_soup = BeautifulSoup(html.read(), 'lxml')
print('Scraping, URL')
 

if(movie_url.startswith('https://www.imdb.com/title/')):
        #find the poster image
    imdb_soup = btfl_soup.find('div', {'class':'poster'})
    cover_img = imdb_soup.find('img', {'src':re.compile('.jpg')})

elif(movie_url.startswith('https://alternativemovieposters.com/')):
    rt_soup = btfl_soup.find('div', {'class':'fusion-flexslider'})   
    cover_img =rt_soup.find('img', {'src':re.compile('.jpg')})


 

 
# Grab just the URL from the surrounding tags
# Check to make sure have found something
# before getting link and causing crash if none found
if cover_img:
    cover_img_link = (cover_img['src'])
 
# Save the jpg image from the resulting URL.
# Note: At present this will overwtite previous scrape cover image.
if cover_img_link:
    with open('cover.jpg', 'wb') as handle:
        img_response = requests.get(cover_img_link, stream=True)
        for block in img_response.iter_content(1024):
            if not block:
                break
            handle.write(block)
 
 
print('Image Downloaded ')
 

# converting image to icon 


filename = r'cover.jpg'
img = Image.open(filename)
img.save('cover.ico')

print('Image Converted to .ico')


