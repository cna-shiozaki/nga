import requests


class PaintingQuery():
    """
    Perform a query on the database to find pictures matching the filter.
    The query retrieves a JSON file containing info about a set of picture items.
    Each picture item contains : (artist name, picture_name, file_url for download)
    """


    url_host_and_path = "https://www.nga.gov/bin/ngaweb/collection-search-result/" 
    url_meta_info = "search.pageSize__30.pageNumber__1.json" 
    url_query_parameters = "classification=painting" \
                           "&sortOrder=DEFAULT" \
                           "&artobj_downloadable=Image_download_available" 

    def __init__(self):
        pass

    def set_filter(self, dict_filter : dict):
        if "lifespan" in dict_filter:
                self.url_query_parameters += '&' + 'artobj_lifespan=' + dict_filter["lifespan"]

        if "nationality" in dict_filter:
                self.url_query_parameters +=  '&' + 'artobj_vbnationality=' + dict_filter["nationality"]

        if "style" in dict_filter:
                self.url_query_parameters +=  '&' + 'artobj_style=' + dict_filter["style"]


    def execute_count(self):
        """
        Retrieves the number of pictures matching the result.
        """        
        query_meta_info = "search.pageSize__1.pageNumber__1.json"
        
        url = self.url_host_and_path + query_meta_info + '?' + self.url_query_parameters 

        response = requests.get(url)
        jresp = response.json()

        return jresp["totalcount"]

    def execute_query(self, count):
        """
        Retrieves the info (artist name, picture_name, file_url for download) about pictures matching the result.
        """                
        query_meta_info = f"search.pageSize__{count}.pageNumber__1.json"
        
        url = self.url_host_and_path + query_meta_info + '?' + self.url_query_parameters 

        response = requests.get(url)
        jresp = response.json()
        results = jresp["results"] 
        
        results = list( map( lambda res : ({ "title": res["title"], "artist": res["attributionInv"], "download": res["download"] }), results))

        return results






