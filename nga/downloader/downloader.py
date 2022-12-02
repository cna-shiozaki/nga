import os
import regex as re
import requests
from tqdm import tqdm

class Downloader():
    """
    Basic downloader class.
    Responsible for downloading a set of pictures to a local directory.
    """

    def __init__(self) -> None:
        pass

    def create_if_null(self,target_directory):
        if not os.path.exists(target_directory):
            os.mkdir(target_directory)

    def remove_unwanted_chars(self, s : str):
        return s.replace('"','').replace('/','').replace('\\','').replace(':','').replace('?','')

    def sequential_download(self, items, target_directory):
        """
        Sequential download of a set of items (pictures) in the target directory
        """
        
        self.create_if_null(target_directory)
        os.chdir(target_directory)
        
        for item in tqdm(items):

            # Download the picture
            response = requests.get(item["download"])

            # Remove unwanted characters : allow the file to be saved in Windows/Linux file systems 
            title = self.remove_unwanted_chars(item["title"])

            # Create a new file name (from the artist name concatenated with the title of the work)
            file_name = item["artist"] + "__" + title

            # Get the file extension (usually .jpg)
            file_extension = re.search(pattern="\.[0-9a-z]+$",string="file.jpg").group(0)

            # Save to local FS
            with open(file_name + file_extension, "wb") as f:
                f.write(response.content)
    


