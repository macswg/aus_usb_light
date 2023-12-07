#sudo thonny
import time
import board
import neopixel
import mido
from mido import MidiFile, MidiTrack, Message
import time
from rpi_ws281x import *
import argparse

# LED strip configuration:
LED_COUNT      = 32     # Number of LED pixels.
LED_PIN        = 10      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 80  # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


def note_action():
#    if channel == 4:
        #print("Detected Channel 4! Performing action lightworks.py")
        # Trigger Light
        # lightworks.py
    print("light trigger")
   
    # Define functions which animate LEDs in various ways.
    def colorWipe(strip, color, wait_ms=50):
        """Wipe color across display a pixel at a time."""
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            
            

    if __name__ == '__main__':
        # Process arguments
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
        args = parser.parse_args()

        # Create NeoPixel object with appropriate configuration.
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        # Intialize the library (must be called once before other functions).
        strip.begin()
        
        
        #try:

            #while True:
    print ('Color wipe animations.')
    colorWipe(strip, Color(0, 0, 255))  # Red wipe
    colorWipe(strip, Color(0, 0, 0))  # Blue wipe
    #colorWipe(strip, Color(0, 0, 255))  # Green wipe
    #colorWipe(strip, Color(0, 0, 0))
    print('done')
            
    print('MIDI STOP')    
        

def main():
    # Open the first available MIDI input port
    with mido.open_input('USB MIDI Interface:USB MIDI Interface MIDI 1 28:0') as inport:
        print('Listening to MIDI messages...')
        for msg in inport:
            #print(msg.channel)
            #print(msg)
            if msg.channel == 4:
                print("Detected Channel 5! Triggering Light")
                note_action()
                #note_action(msg.note)
            else:
                pass

if __name__ == '__main__':
    main()

