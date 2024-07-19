import requests
import threading

# Hosted Server URL
URL = "http://localhost:8000/chat/completions"
MODEL_NAME = "gemma-2b-oasst2-01"
NUM_THREADS = 100
USER_CONTENT = "Hello, how are you?"

# Function to send a request
def send_request():
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "user", "content": USER_CONTENT}
        ]
    }
    try:
        response = requests.post(URL, json=payload, headers=headers)
        print(f"Status Code: {response.status_code}, Response: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")

threads = []
for _ in range(NUM_THREADS):
    thread = threading.Thread(target=send_request)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("Stress test complete.")
