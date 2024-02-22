from datetime import datetime
import time


def printNowTime():
    now = datetime.now()
    current_time = now.strftime("%d.%m.%Y %H:%M:%S")
    print("Currenttime = ", current_time)
    return


while True:
    printNowTime()
    time.sleep(5)
