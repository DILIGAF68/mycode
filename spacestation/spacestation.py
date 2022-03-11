#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""

# import request library
import requests

# URL of API
URL= "http://api.open-notify.org/iss-now.json"

# define main fuction
def main():

    # set variable for request object
    resp= requests.get(URL).json()

    print( dir(resp )


    main()
