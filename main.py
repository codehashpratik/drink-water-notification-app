import time
from plyer import notification
if __name__ == "__main__":
    notification.notify(
        title="please drink water",
        message="The U.S. National Academies of Sciences,Engineering, and Medicine determined that an adequate daily fluid intake is:About 15.5 cups(3.7 liters) of fluids a day for men.About 11.5 cups(2.7 liters) of fluids a day for women.",
        app_icon="E:\more python programs for practice\drink water notification app\icon.ico",
        timeout=10
    )
    time.sleep(60*60)
