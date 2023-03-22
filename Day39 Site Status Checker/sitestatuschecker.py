# Day 39: Site status checker (Up or down)

import sys
import requests

def check_site_status():
    url = input("Enter the URL you want to check: ")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url} is up!")
        else:
            print(f"{url} is down with status code {response.status_code}.")
    except requests.ConnectionError:
        print(f"{url} is down!")

if __name__ == "__main__":
    check_site_status()
