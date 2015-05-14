__author__ = 'fredriksvard'

url = 'http://api.scb.se/OV0104/v1/doris/sv/ssd/BE/BE0101/BE0101A/BefolkningNy'

import pandas as pd
from pandas import DataFrame
import requests


r = requests.get(url)

print r.status_code

my_json =  r.json()



ds = pd.read_json(my_json)

print ds.head()

