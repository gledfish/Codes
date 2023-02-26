import time
import threading

def coding():
    for i in range(3):
        print("coding ")
        time.sleep(1)

def music():
    for i in range(3):
        print("Music ")
        time.sleep(1)

if __name__ == '__main__':

# coding()
# music()

    coding_thread = threading.Thread(target=coding)
    music_thread = threading.Thread(target=music)

    coding_thread.start()
    music_thread.start()
