# Pocket Monsters Db

In this task we will create a Pokemon database, similiar to the ones you can find online. We'll need
to gather information, populate them into database and then create Flask app that will show us all
the data.

## Preparing an environment
For this app we'll need to install Postgresql (no Docker this time ;) ) locally. You'll also need Python 3
installed on your computer.

## Gathering the data.
Create all your code in the `project` directory. We'll split it into subdirectories to separate
different parts of the app. For gathering part create subfolder `scripts` and create `import_pokemon.py`
file. This is a script that will be probably run once in the real system - just to load initial
data, that's why we put it into scripts subfolder.

From the Pokedex project import [CSV
files](https://github.com/veekun/pokedex/tree/master/pokedex/data/csv) for pokemons list, pokemon
evolutions, pokemon types, types dictionary.

Think how to put these data into postgresql, create `schema.sql` where you'll put `CREATE TABLE`
definitions based on what you have found in these files. Try to run it on database (you can use
pipes `|` or unix output forwarding `<`)

What are the relations between these tables? How can we mark them in postgresql? Update schema.sql
to reflect these relations.

# Import the data
Write a script that will import data from csv to your database using Python. Verify that all your data is in database using `SELECT` statements

# Query the data
Write `assignment1.py` script inside `scripts` folder which will contains of the following functions:

1. Write a query that will return how many pokemons that weight more 100 are there
2. Write a query that for every type will return number of pokemons that has this type as the main type (first slot).
3. Return names of all water pokemon (main or secondary type) that can evolve by leveling after reaching 40 or greater level.
4. Return all the "pure-blood" pokemons (these that does not have secondary type)
5. Return 10 highest pokemons that contains "ha" in their names.
6. Which pokemon is the heaviest steel pokemon.

