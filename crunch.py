#! /usr/bin/env python
import sys, requests, json

from pprint import pprint as pretty

from config import KEY

domain = 'http://api.crunchbase.com'

endpoint_dict = {
    'organizations': '/v/2/organizations', 
    'organization': '/v/2/organization/%(permalink)s',
    'people': '/v/2/people',
    'person': '/v/2/person/%(permalink)s',
    'products': '/v/2/products',
    'product': '/v/2/product/%(permalink)s',
    'fundinground': '/v/2/funding-round/%(uuid)s',
    'acquisition': '/v/2/acquisition/%(uuid)s',
    'ipo': '/v/2/ipo/%(uuid)s',
    'fundraise': '/v/2/fund-raise/%(uuid)s',
    'locations': '/v/2/locations',
    'categories': '/v/2/categories'
}

def main():
    return req('organization', permalink='beyond-curious')

def req(endpoint, **kwargs):
    if kwargs:
        #None of the endpoints take more than one variable
        k, v = kwargs.items()[0]
        r = requests.get(domain + endpoint_dict[endpoint] % {k: v} + '?user_key=' + KEY)
        return json.loads(r.content)
    else:
        r = requests.get(domain + endpoint_dict[endpoint] + '?user_key=' + KEY)
        return json.loads(r.content)

if __name__ == '__main__':
    pretty(main())
