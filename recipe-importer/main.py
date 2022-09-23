from recipe_scrapers import scrape_me
from PIL import Image
import sys
import requests

recipe_template = """---
layout: recipe
title: "{title}"
image: {image}
tags:

ingredients:
- {ingredients}

directions:
- {directions}
---
"""

def write_image(url, filename):
    ext = url.split('.')[-1]

    filepath = './images/{file}.{ext}'.format(file=filename, ext=ext)
    with open(filepath, 'wb') as handle:
        response = requests.get(url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)
    
    im = Image.open(filepath)
    size = 612, 306
    im.thumbnail(size, Image.Resampling.LANCZOS)
    im.save(filepath)

def scrape(url):
    scraper = scrape_me(url)
    filename = scraper.title().lower().replace(" ", "-")

    ingredients = "\n- ".join(scraper.ingredients())

    directions = "\n- ".join(scraper.instructions_list())

    img_path = write_image(scraper.image(), filename)
    img_ext = scraper.image().split('.')[-1]

    recipe = recipe_template.format(title = scraper.title(), image=filename+'.'+img_ext, ingredients=ingredients, directions=directions)

    f = open("./_recipes/{}".format(filename) + ".md", "w")
    f.write(recipe)
    f.close()

if len(sys.argv) != 2:
    print('Needs exactly 1 argument - the url to scrape the recipe from')
else:
    print(scrape(sys.argv[1]))