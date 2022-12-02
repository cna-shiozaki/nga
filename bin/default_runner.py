import json
from nga.query.painting_query import PaintingQuery
from nga.downloader.downloader import Downloader

"""
Simple use-case : download a set of pictures matching the filter found in the configuration.
The pictures are downloaded in the directory specified in the configuration. 
"""

# 1 - Read configuration for target 
with open("nga/config/configurator.json", "r+") as file:
    configurator = json.load(file)

# 2 - Identify ressources 
pq = PaintingQuery()

pq.set_filter(configurator["filter"])
count = pq.execute_count()
resp = pq.execute_query(count)

print(f"{count} results found")

# 3 - Download the ressources to directory
d = Downloader()
d.sequential_download(items=resp, target_directory=configurator["target_directory"])

print("Done!")
