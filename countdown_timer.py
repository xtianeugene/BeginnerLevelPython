import time

def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"\r{mins:02d}:{secs:02d}", end="")
        time.sleep(1)
        seconds -= 1
    print("\r00:00\nTime's up!")

if __name__ == "__main__":
    countdown(int(input("Seconds: ")))
