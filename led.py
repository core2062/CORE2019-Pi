# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import signal

def sigint_handler(signum, frame):
    print('Ending...')
    pixels.fill((0,0,0))
    pixels.show()
    exit(0)

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 300

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False,
                           pixel_order=ORDER)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 340:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    elif pos < 255:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    else:
        pos -= 255
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

def lightTail(wait,color,tail):
    for j in range(num_pixels+tail-1):
        if (j < num_pixels):
            pixels[j]=color
        pixels.show()
        pixels[j-tail+1]=(0,0,0)
        time.sleep(wait)
    for j in range(num_pixels+tail):
        pixel=num_pixels-j
        if(num_pixels-j-1 >= 0):
            pixels[num_pixels-j-1]=color
        pixels.show()
        if (num_pixels-j+tail-2 < num_pixels):
            pixels[num_pixels-j+tail-2]=(0,0,0)
        time.sleep(wait)
    pixels.show()

def lightTailRainbow(wait,tail):
    for j in range(num_pixels+tail-1):
        if (j < num_pixels):
            pixels[j]=wheel(j)
        pixels.show()
        pixels[j-tail+1]=(0,0,0)
        time.sleep(wait)
    for j in range(num_pixels+tail):
        pixel=num_pixels-j
        if(num_pixels-j-1 >= 0):
            pixels[num_pixels-j-1]=wheel(j)
        pixels.show()
        if (num_pixels-j+tail-2 < num_pixels):
            pixels[num_pixels-j+tail-2]=(0,0,0)
        time.sleep(wait)
    pixels.show()
    

def fillLight(wait,color):
    for j in range(num_pixels):
        pixels[j]=color
        pixels.show()
        time.sleep(wait)
    for j in range(num_pixels):
        pixels[num_pixels-j-1]=(0,0,0)
        pixels.show()
        time.sleep(wait)

signal.signal(signal.SIGINT, sigint_handler)

while True:
    ## Comment this line out if you have RGBW/GRBW NeoPixels
    #pixels.fill((255, 0, 0))
    ## Uncomment this line if you have RGBW/GRBW NeoPixels
    ## pixels.fill((255, 0, 0, 0))
    #pixels.show()
    #time.sleep(1)

    ## Comment this line out if you have RGBW/GRBW NeoPixels
    #pixels.fill((0, 255, 0))
    ## Uncomment this line if you have RGBW/GRBW NeoPixels
    ## pixels.fill((0, 255, 0, 0))
    #pixels.show()
    #time.sleep(1)

    ## Comment this line out if you have RGBW/GRBW NeoPixels
    #pixels.fill((255, 255, 255))
    ## Uncomment this line if you have RGBW/GRBW NeoPixels
    ## pixels.fill((0, 0, 255, 0))
    #pixels.show()
    #time.sleep(1)

    #rainbow_cycle(0.001)    # rainbow cycle with 1ms delay per step
    #lightTail(0.001,(255,0,0),10)
    #lightTail(0.001,(255,24,0),10)
    #lightTail(0.001,(0,255,0),10)
    #lightTail(0.001,(0,0,255),10)
    #fillLight(0.001,(255,0,0))
    #fillLight(0.001,(0,255,0))
    #fillLight(0.001,(0,0,255))
    
    lightTailRainbow(0.001,10)
    lightTailRainbow(0.001,10)
    lightTailRainbow(0.001,10)
    lightTailRainbow(0.001,10)
    

