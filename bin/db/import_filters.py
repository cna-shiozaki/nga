import os
import sqlite3
import requests

"""
Script to install the possible filters used to query the database
The values of the filters are found in the 'search the database' web page ; they are populated with dynamic AJAX calls (initiated by javascript) returning JSONs
Intented to be run as a module (python -m bin.db.import_filters)
"""

def insert_into_filters_db(table_name: str, items_tuples):
    """ Insert entries into a table_name that will hold values for filters """
    con = sqlite3.connect("filters.db")
    cur = con.cursor()

    cur.executemany(f"INSERT INTO {table_name} VALUES(?)", items_tuples)

    con.commit()
    con.close()

os.chdir("./nga/filters")

print("Fetching adequate filter values for artist's nationality...")
url = "https://www.nga.gov/content/ngaweb/collection/artists/jcr:content/parmain/facetcomponent/parList/artistlistings.pageSize__0.pageNumber__1.json"
page = requests.get(url)

nationalities = list(filter( lambda el : el['name'] == 'CONSTITUENT_VISUALBROWSERNATIONALITY', page.json()["facets"]))[0]['map']
nationalities = list(map(lambda el : el["label"],nationalities ))

nationalities_tuples = list(map(lambda el : (el,),nationalities))


print("Fetching adequate filter values for painting style...")
url = "https://www.nga.gov/bin/ngaweb/collection-search-result/search.pageSize__1.pageNumber__1.json?classification=painting&sortOrder=DEFAULT"
page = requests.get(url)

styles = list(filter( lambda el : el['name'] == 'ARTOBJECT_VISUALBROWSERSTYLE', page.json()["facets"]))[0]['map']
styles = list(map(lambda el : el["label"],styles ))

styles_tuples = list(map(lambda el : (el,),styles))


insert_into_filters_db(table_name="nationality", items_tuples=nationalities_tuples)
insert_into_filters_db(table_name="style", items_tuples=styles_tuples)



print("Done. The filter database is up-to-date.")
