import requests
import random

def get_random_dog_image():
    # Fetch the list of all dog breeds
    url = 'https://dog.ceo/api/breeds/image/random'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # get a random dog image url
        image_url = data['message']
        print(f"Dog image URL: {image_url}")
    else:
        print(f"Failed to fetch dog image URL. Status code {response.status_code}")

if __name__ == '__main__':
    get_random_dog_image()
