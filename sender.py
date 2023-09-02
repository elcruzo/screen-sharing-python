import threading
from vidstream import StreamingServer

sender = StreamingServer('11.34.48.13', 9999)
#Got the IP Address by running ipconfig getifaddr en0

t = threading.Thread(target=sender.start_server)
t.start()

while input("") != 'STOP':
    continue

sender.stop_server()