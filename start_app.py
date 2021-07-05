"""
SOURCE LINES:
    https://askubuntu.com/questions/62858/turn-off-monitor-using-command-line
    https://askubuntu.com/questions/235126/simulate-media-keys-in-terminal
"""

from win32 import win32api
# import win32api
from socket import gethostbyname, gethostname
from flask import Flask, render_template, request

from win32con import (
                    VK_MEDIA_PLAY_PAUSE,
                    VK_VOLUME_DOWN,
                    VK_VOLUME_UP,
                    VK_MEDIA_NEXT_TRACK,
                    VK_MEDIA_PREV_TRACK,
                    VK_VOLUME_MUTE,
                    KEYEVENTF_EXTENDEDKEY
                )


app = Flask(__name__)
LOCAL_IPV4_ADDR = gethostbyname(gethostname())


def call_key(command):
    if command == 'switch_up':
        win32api.keybd_event(VK_MEDIA_NEXT_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)
    elif command == 'switch_down':
        win32api.keybd_event(VK_MEDIA_PREV_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)
    elif command == 'volume_up':
        win32api.keybd_event(VK_VOLUME_UP, 0, KEYEVENTF_EXTENDEDKEY, 0)
    elif command == 'volume_down':
        win32api.keybd_event(VK_VOLUME_DOWN, 0, KEYEVENTF_EXTENDEDKEY, 0)
    elif command == 'pause':
        win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)
    elif command == 'mute':  # mute & unmute
        win32api.keybd_event(VK_VOLUME_MUTE, 0, KEYEVENTF_EXTENDEDKEY, 0)


def is_able_to_go(command) -> bool:
    if command in ['switch_up', 'switch_down', 'volume_up',
                   'volume_down', 'pause', 'mute']:
        return True
    return False


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        print(request.form.get('query'))
        if is_able_to_go(request.form.get('query')):
            print(request.form.get("query"))
            call_key(request.form.get("query"))
    return render_template('index.html')


if __name__ == '__main__':
    print("Server have started on {}".format(LOCAL_IPV4_ADDR))
    app.run(host=LOCAL_IPV4_ADDR, port=5000, debug=True)
