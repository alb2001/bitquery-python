import requests


def run_query(apikey, query):
    """
    A simple function to use requests. post to make the API call.

    :param apikey: Your API Key here
    :param query: Your query
    :return: returns a request in JSON format
    """

    headers = {'X-API-KEY': apikey}
    request = requests.post('https://graphql.bitquery.io/',
                            json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed and return code is {}.      {}'.format(request.status_code, query))
