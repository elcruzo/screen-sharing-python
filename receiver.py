import threading
from vidstream import ScreenShareClient

receiver = ScreenShareClient('11.34.48.13', 9999)
#usually it's the Public IP Address but because I'm connecting on the same computer that's why I'm using the same IP Address

t = threading.Thread(target=receiver.start_stream)
t.start()

while input("") != 'STOP':
    continue

receiver.stop_stream()
