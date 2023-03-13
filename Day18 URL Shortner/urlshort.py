# Day 18: URL shortener

import requests

def shorten_url(): #using tinyurl service (APIless)
    long_url = input('Enter a long URL to shorten: ')
    endpoint = 'https://tinyurl.com/api-create.php'
    params = {'url': long_url}
    response = requests.get(endpoint, params=params)
    if response.ok:
        short_url = response.text
        print(f'Short URL: {short_url}')
    else:
        print('Error: Could not generate short URL.')

# Call the function to generate a short URL for a long URL entered by the user.
shorten_url()
