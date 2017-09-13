import csv
import psycopg2



conn = psycopg2.connect("dbname=pokemondb user=postgres")
cursor = conn.cursor()

cursor.execute("CREATE TABLE pokemon_table(INSTANCE_ID INTEGER,SPECIES VARCHAR, SPECIES_ID INTEGER, HEIGHT INTEGER , WEIGHT INTEGER, BASE_EXPERIENCE INTEGER, POK_ORDER INTEGER, IS_DEFAULT INTEGER);")

with open('pokemon.csv', 'r', encoding='utf-8') as pkmn:
    pok = csv.reader(pkmn)
    next(pok)
    for row in pok:

        cursor.execute("INSERT INTO pokemon_table(instance_id,species,species_id,height,weight,base_experience, pok_order, is_default) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",row)

conn.commit()
cursor.close()
conn.close()

