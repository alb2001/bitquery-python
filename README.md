# bitquery-python

A simple package to query GraphQL using [Bitquery](https://bitquery.io)

## Installation

```
pip install bitquery-python
```

## Obtaining API Key
You will need to create an account on the [GraphQL IDE](https://graphql.bitquery.io/ide) to be able to obtain an API key.


## Running queries
Here is an example code to run a query

```
from bitquery import bitquery

API_KEY = "YOUR API KEY"

query = """
query{
  bitcoin{
    blocks{
      count
    }
   }
}
"""

result = bitquery.run_query(API_KEY, query)
print(result)
```

## Authors
* [alb2001](https://github.com/alb2001)


## More information
* [bitquery-python on PyPI](https://pypi.org/project/bitquery-python)
* [GraphQL APIs using Python](https://bitquery.io/blog/graphql-with-python-javascript-and-ruby#GraphQL_APIs_using_Python)
* [GraphQL IDE](https://graphql.bitquery.io/ide)
* [Bitquery](https://bitquery.io)
