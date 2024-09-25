import sounddevice as sd
import soundfile as sf
import time

CLEAR = "\033[2J"   # used to clear the terminal.
CLEAR_AND_RETURN = "\033[H" # Make the print out statement in one line. Make the cursor return to same position.


def alarm(seconds):
    time_elasped = 0
    print(CLEAR)

    while time_elasped < seconds:
        time.sleep(1)
        time_elasped += 1
        
        time_left = seconds - time_elasped
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f'{CLEAR_AND_RETURN}Alarm will ring in: {minutes_left:02d}:{seconds_left:02d}')

    data, samplerate = sf.read('project/alarm1.wav')
    sd.play(data, samplerate)
    sd.wait()

def convert_to_seconds(min, sec):
    total_seconds = min * 60 + sec
    alarm(total_seconds)


minutes = int(input("Enter minutes to wait: "))
seconds = int(input("Enter seconds to wait: "))
# total_seconds = minutes * 60 + seconds
convert_to_seconds(minutes, seconds)


