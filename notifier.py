from plyer import notification
import time

title = 'Hi, Hello and Hi !'

message = 'If u reading this ~I LOVE U TO THE MOON AND BACK !!'
try:
  # new thing. for exception to check bug, use try and except
notification.notify(title = title,
                    message = message,
                    #creating icon for the notification
                    app_icon = "heart.ico",
                    #the notification stays for 15sec
                    timeout = 15,
                    toast = False)
except Exception as e:
    print(f"Oops! {e}")

#sleep for 1 hr => 60*60 sec
#notification repeats after every 1 hr
time.sleep(60*60)
