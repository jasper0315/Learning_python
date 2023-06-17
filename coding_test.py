import requests
import json
import time
import pandas as pd
from pprint import pprint

# 1. 楽天レシピのレシピカテゴリ一覧を取得する

res = requests.get('https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426?applicationId=1009993429057254143')

json_data = json.loads(res.text)

print(json.dumps(json_data, indent=2, sort_keys=True))

print (pd.__version__)