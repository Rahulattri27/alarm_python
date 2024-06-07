import time
import pygame
file_path="alarm/audio.mp3"

CLEAR="\033[2J"
CLEAR_AND_RETURN="\033[H"

def alarm(seconds):
    time_elapsed=0
    print(CLEAR)
    while time_elapsed<seconds:
        time.sleep(1)
        time_elapsed+=1
        time_left=seconds-time_elapsed
        minutes_left=time_left//60
        seconds_left=time_left%60
        print(CLEAR_AND_RETURN)
        print(f"{minutes_left:02d}:{seconds_left:02d}")
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # Keep the program running while the sound is playing
    while pygame.mixer.music.get_busy():
        time.sleep(1)

print("Enter the minutes and seconds in Alarm")
minutes=int(input("Enter the minutes"))
seconds=int(input("Enter the seconds "))
total_seconds=minutes*60+seconds
alarm(total_seconds)




