import time
from plyer import notification

def take_a_break():
    # Show a notification to take a break
    notification.notify(
        title="Take a Break",
        message="It's time to take a break from your work!",
        timeout=10
    )

if __name__ == "__main__":
    while True:
        # Wait for 20 minutes
        time.sleep(20 * 60)  # 20 minutes in seconds

        # Take a break
        take_a_break()
