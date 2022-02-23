
import time


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(f"\r{timer}", end='')
        time.sleep(1)
        t -= 1

    print("\nTime Completed!")


t = int(input("Enter the time in second: "))


if __name__ == "__main__":
    countdown(t)
