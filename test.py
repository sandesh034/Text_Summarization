import requests
import json
url="http://127.0.0.1:5000/summarize"


article = """

The Thirsty Crow

On a hot summer day, a thirsty crow flew around in search of water. The sun blazed in the sky, and the dry air made the crow feel even thirstier. After searching for a long time, it finally spotted a pot under a tree.

The crow excitedly flew down and looked into the pot. To its disappointment, the water level was very low, and its beak could not reach the water. The crow thought for a while, wondering how to get the water.

Suddenly, it had an idea! It noticed small pebbles scattered around the pot. The crow began picking up the pebbles one by one with its beak and dropping them into the pot. Slowly, the water level started to rise.

The crow continued its efforts until the water level was high enough to drink. With great relief, the crow quenched its thirst and flew away happily.
"""

data={
    "text":article,
    "max_length":400,
    "min_length":50,
    "num_beams":4
}

response=requests.post(url=url,json=data)

print(response.json())