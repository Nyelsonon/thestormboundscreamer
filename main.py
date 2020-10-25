#imports

import cv2

import pytesseract

import numpy as np

import pyautogui

import time

from playsound import playsound

#variables
#coordinate variables -DYNAMIC BASED ON COMPUTER- these are complicated, they are the region in which the health picture is taken. This depends on many factors such as fullscreen or not, and your resolution
x1 = 0
y1 = 0
x2 = 0
y2 = 0
#dont change these:
img = "image1.png"
#you can change these tho:
update_time = 5
#this is based on your starting health in stormbound
text = 12

def update_image():
	time.sleep(update_time)
	im1 = pyautogui.screenshot(region=(x1,y1,x2,y2))
	"""this path  down here WILL change  based on the comuter, dont fret Nyelson is here to provide you instructions.
	 MAC: left click on the folder you want to keep the proccess in, press alt and press copy path
	 WINDOWS: eh search it up
	 """
	im1.save('/Users/nealkotval/Desktop/ocr/image1.png')
	img = cv2.imread('image1.png')


#code stuff
while True:

	update_image()
	img = cv2.imread('image1.png')
	
	#grayscale stuffs dont mess witth this
	gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
	gray, img_bin = cv2.threshold(gray,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	gray = cv2.bitwise_not(img_bin)
	kernel = np.ones((2, 1), np.uint8)
	img = cv2.erode(gray, kernel, iterations=1)
	img = cv2.dilate(img, kernel, iterations=1)

	text_prev = text
	text = pytesseract.image_to_int(img)
	print(text)

	if text != text_prev:
		playsound('scream.mp3')
