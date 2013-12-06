from __future__ import unicode_literals
try:
    from urllib.parse import urljoin as urljoin_
except ImportError:   # Python 2
    from urlparse import urljoin as urljoin_

from functools import reduce
def urljoin(*args):
    return reduce(urljoin_, args)

def get_json(request):
    """request from requests library handles backwards compatability for
    requests < 1.0
    """
    if hasattr(request.json, '__call__'):
        return request.json()
    else:
        return request.json

