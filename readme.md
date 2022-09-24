# Chowdown

A simple recipe site, soft-forked from: [http://chowdown.io](http://chowdown.io)

# Getting Started

- Install ruby 2.7.6
- `gem install bundler jekyll` (for more info see https://jekyllrb.com/)
- `jekyll serve --live` to run locally

# Importing a recipe
- Install python 3
- Run `python ./recipe-importer/main.py '<url_of_recipe>'`
# Writing a Recipe

The recipes are stored in the collection "Recipes" (the folder /_recipes).

They are written in Markdown and contain a few special sections:

- The frontmatter, which contains:
 - Title, Image, and Layout (which is "recipe")
 - Ingredients (a list of things in the dish)
 - Directions (a list of steps for the dish)
- Body content (for intros, stories, written detail)

# Writing a component/recursive recipe

A component recipe is a recipe made up of other recipes. To make a new component recipe:

- Add a `recipes` list to your page
- reference the recipe you wish to include by its filename