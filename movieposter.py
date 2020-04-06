import csv
import os
import re
import sys
from PIL import Image
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, Tk
m = tk.Tk()
import webbrowser
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup
import pyperclip



# scraping the posters and saving to a particular location





def url_error():
    messagebox.showerror('Error', 'No IMDB URL found on clipboard.')
    sys.exit()
 
# Stop ugly default tk window appearing if error message box is used.
root = Tk()
root.withdraw()


def download():

	m2= tk.Toplevel(m)
	m2.geometry('400x300')
	m2.title('Paste the URL of film')

	textBox=Text(m2, height=5, width=30)
	textBox.pack(pady=(20,0), ipadx=50, ipady=5)
	
	inputValue=textBox.get("1.0","end-1c")

	box = messagebox.showinfo("Done","Image downloaded successfully")  

	

	mainloop()

def get_input():
        global inputValue
        inputValue=textBox.get("1.0","end-1c")
        inp = re.match(r'^(https:|)[/][/]([^/]+[.])*imdb.com', inputValue)
        
        if inp:
            t = threading.Thread(target=download)
            t.start()
        
        else:
            box3 = messagebox.showerror("Error","Unknown Error!!")  

 
# Show error and quit if not imdb address.
if not inputValue.startswith('https://www.imdb.com/title/'):
    url_error()
 
# Read the html source code from the URL.
imdb_html = urlopen(inputValue)
btfl_soup = BeautifulSoup(imdb_html.read(), 'lxml')
print('Scraping, URL')
 

 

 
#find the poster image
imdb_soup = btfl_soup.find('div', {'class':'poster'})
cover_img = imdb_soup.find('img', {'src':re.compile('.jpg')})
 
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
 
# Open image with systems viewer
webbrowser.open('cover.jpg')
 
print('Done scraping.')
 
# To do, text output needs cleaning up.
# Try to find out the except error names.
# Save imdb.txt and cover.jpg in films name
# so as not overwrite previous scrape.

# converting image to icon 


filename = r'logo.jpg'
img = Image.open(filename)
img.save('logo.ico')

# setting the icon to a particular folder



# GUI


m = tk.Tk() #master shortened to m
m.title('PosterMan')
m.geometry('300x200')

b1 = ttk.Button(m, text="Download Poster")#, command=changer)
b1.pack(pady=(20,0), ipadx=50, ipady=5)
b1 = ttk.Button(m, text="Convert to .ico")#, command=cover)
b1.pack(pady=(20,0), ipadx=50, ipady=5)
b1 = ttk.Button(m, text="Set Icon")#, command=open_browser)
b1.pack(pady=(20,0), ipadx=30, ipady=5)

m.mainloop()

