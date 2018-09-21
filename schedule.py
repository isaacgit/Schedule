import schedule
import time

import subprocess




def njob():
    audio_file = "bell.mp3"
    return_code = subprocess.call(["afplay", "bell.mp3"])
njob()
'''
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
'''
