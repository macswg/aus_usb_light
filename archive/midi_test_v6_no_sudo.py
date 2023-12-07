import time
import board
import neopixel
import mido
from mido import MidiFile, MidiTrack, Message


def note_action():
#    if channel == 4:
        #print("Detected Channel 4! Performing action lightworks.py")
        # Trigger Light
        # lightworks.py
    print("note action running")
        #Initialise a strips variable, provide the GPIO Data Pin
        #utilised and the amount of LED Nodes on strip and brightness (0 to 1 value)
        pixels1 = neopixel.NeoPixel(board.D10, 32, brightness=.2)

        #Also create an arbitary count variable
        #x=0

        #Focusing on a particular strip, use the command Fill to make it all a single colour
        #based on decimal code R, G, B. Number can be anything from 255 - 0. Use a RGB Colour
        #Code Chart Website to quickly identify a desired fill colour.
        pixels1.fill((0, 0, 255))

        #Below demonstrates how to individual address a colour to a LED Node, in this case
        #LED Node 10 and colour Blue was selected
        #pixels1[10] = (0, 20, 255)

        #Sleep for three seconds, You should now have all LEDs showing light with the first node
        #Showing a different colour
        time.sleep(2)

        #Little Light slider script, it will produce a nice loading bar effect all the way up
        #and then all the way back
        #This was created using a While Loop taking advantage of that arbitary variable to determine
        #which LED Node we will taget/index with a different colour

        #Below will loop until variabe x has value 35
        #while x<35:
            
            #pixels1[x] = (255, 0, 0)
            #pixels1[x-5] = (255, 0, 100)
            #pixels1[x-10] = (0, 0, 255)
            #Add 1 to the counter
            #x=x+1
            #Add a small time pause which will translate to 'smoothly' changing colour
            #time.sleep(0.05)

        #below section is the same process as above loop just in reverse
        #while x>-15:
            #pixels1[x] = (255, 0, 0)
            #pixels1[x+5] = (255, 0, 100)
            #ixels1[x+10] = (0, 255, 0)
            #x=x-1
            #time.sleep(0.05)

        #Add a brief time delay to appreciate what has happened    
        #time.sleep(4)

        #Complete the script by returning all the LED to off
        pixels1.fill((0, 0, 0))
        pixels1.fill((0, 0, 0))
        print('all done')
    

def main():
    # Open the first available MIDI input port
    with mido.open_input('USB Uno MIDI Interface:USB Uno MIDI Interface MIDI 1 20:0') as inport:
        print('Listening to MIDI messages...')
        for msg in inport:
            #print(msg.channel)
            if msg.channel == 4:
                print("Detected Channel 5! Performing action lightworks.py")
                note_action()
                #note_action(msg.note)

if __name__ == '__main__':
    main()
