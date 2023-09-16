import requests
import time
from json import loads
import json


def fetch_website(url):
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")

        # If you want to print the content, uncomment the next line

        data = response.text
        startidx = data.find('(')
        endidx = data.rfind(')')

        test = loads(data[startidx + 1:endidx])

        with open("sample.json", "w") as outfile:
            json.dump(test, outfile)

        # print(test)
    except requests.RequestException as e:
        print(f"Error fetching the website: {e}")


def main():
    # Replace with your target URL
    url = "http://static.sidearmstats.com/static/json_gvsu_football_stats.js"
    while True:
        fetch_website(url)
        time.sleep(1)


if __name__ == "__main__":
    main()
