# A National Gallery of Art paintings scrapper

The National Gallery of Art is a art museum based in Washington, DC.
It features a tremedous collection of Art from all over the world.

The museum provides a free access to thousands of high-quality pictures.
Those pictures are in the Public Domain and can be downloaded for free as mentioned in the [Open Access Policy](https://www.nga.gov/notices/open-access-policy.html). 

This [web page](https://www.nga.gov/collection-search-result.html?sortOrder=DEFAULT&artobj_downloadable=Image_download_available&pageNumber=1&lastFacet=artobj_downloadable.html) is the entry point of the collection. Filters are available to eliminate pictures that do not match the selected criteria.

However, from the website, it is not possible at the moment to download the entire collection of pictures matching specific criteria.
It's now possible with this project.

## Requirements
Docker Engine

## Installation

After cloning this project, run these two lines in a terminal : 
```docker
docker build . -t "nga_scrapper"
docker run -v "%cd%\nga\config:/nga/nga/config" -v "%cd%\download_dir:/nga/download_dir" -it nga_scrapper
``` 
(note : replace `%cd%` with `$(pwd)` if your host machine runs Linux)

## Usage

The last `docker run` command should open for you a shell prompt in the container environnement.
Now, you can edit the file `nga/config/configurator.json` and especially its `filter` attribute.

Then, to sequentially download the set of pictures matching the filters : 
```
python -m bin.default_runner
````
The pictures are downloaded in the `download_dir` folder.

## Todo
Add a UI interface with a Javascript single-page application.