import re
import argparse
import requests


parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='The URL to extract the URLs from')
args = parser.parse_args()

# Get the url from the arguments
url = args.url

# Send a request to the web page (like using CURL)
with requests.get(url) as response:
# Read the content of the web page
    html = response.text


# Some regex to filter the results we need
urls = re.findall(r'(https?:\/\/[^"<>\s]*)', html)

for urlfound in urls:
    print(urlfound)
