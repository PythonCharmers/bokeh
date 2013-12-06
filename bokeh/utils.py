from __future__ import unicode_literals
from future import standard_library
import urllib.parse
from functools import reduce
def urljoin(*args):
    return reduce(urllib.parse.urljoin, args)

def get_json(request):
    """request from requests library handles backwards compatability for
    requests < 1.0
    """
    if hasattr(request.json, '__call__'):
        return request.json()
    else:
        return request.json

