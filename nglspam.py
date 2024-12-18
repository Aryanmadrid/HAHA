import requests
import threading
import time
import os
os.system('cls' if os.name == 'nt' else 'clear')

def logo():
	print("""####################
made by codecryptpythonic
	
use it for fun!
####################
	""")
logo()
def send_request(user, q, i):
    h = "https://ngl.link/api/submit"
    message = f"{q}"
    data = {
        "username": user,
        "question": message,
        "deviceId": "f6e16e07-0853-4bbb-b4b7-ed2fdb942642",
    }
    try:
        k = requests.post(h, data=data).text
        print("sent!")
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(0.5)

user = input("Enter your username: ")
q = input("Enter your message: ")
idd = int(input("How many times do you want to send requests: "))

threads = []
for i in range(1, idd + 1):
    thread = threading.Thread(target=send_request, args=(user, q, i))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
