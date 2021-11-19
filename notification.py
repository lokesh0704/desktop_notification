import time
from plyer import notification


if __name__ == '__main__':
    while True:
        notification.notify(
            title="Please take 5min break",
            message="As not taking a break from the computer screen can often leads to headaches,"
                    " fatigue, and other undesirable effects.",
            timeout=5
        )
        time.sleep(1800)