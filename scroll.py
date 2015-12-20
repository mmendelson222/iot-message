#This code allows us to scroll a message on an OLED display. 

import math
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

import Image
import ImageFont
import ImageDraw

import sys
import os

# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# 128x32 display with hardware SPI:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# Initialize library.
disp.begin()

# Get display width and height.
width = disp.width
height = disp.height

# Clear display.
disp.clear()
disp.display()

# Create image buffer.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (width, height))

# Load default font.
font = ImageFont.load_default()

dir = os.path.dirname(os.path.realpath(__file__)) + '/fonts/'

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as this python script!
# Some nice fonts to try: http://www.dafont.com/bitmap.php
sFont = 'VCR_OSD_MONO_1.001.ttf'
sFont = '04B_30__.TTF'
#sFont = 'PIXEAB__.TTF'
#sFont = 'PIXEARG_.TTF'

#sFont = 'runescape_uf.ttf'

font = ImageFont.truetype(dir + sFont, 14)

# Create drawing object.
draw = ImageDraw.Draw(image)

def doloop(text):
   
   # Set animation parameters.
   offset = height/2 - 4
   velocity = -8
   startpos = width

   # Define text and get total width.
   maxwidth, unused = draw.textsize(text, font=font)

   pos = startpos
   while True:
	# Clear image buffer by drawing a black filled box.
	draw.rectangle((0,0,width,height), outline=0, fill=0)
	x = pos
	for i, c in enumerate(text):
		# Stop drawing if off the right side of screen.
		if x > width:
			break
		# Calculate width but skip drawing if off the left side of screen.
		if x < -10:
			char_width, char_height = draw.textsize(c, font=font)
			x += char_width
			continue
		# Calculate offset from sine wave.
		y = offset 
		# Draw text.
		draw.text((x, y), c, font=font, fill=255)
		# Increment x position based on chacacter width.
		char_width, char_height = draw.textsize(c, font=font)
		x += char_width
	# Draw the image buffer.
	disp.image(image)
	disp.display()
	# Move position for next frame.
	pos += velocity
	# Start over if text has scrolled completely off left side of screen.
	if pos < -maxwidth:
		pos = startpos
	# Pause briefly before drawing next frame.
	time.sleep(0.1)

doloop(sys.argv[1])
