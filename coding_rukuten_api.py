import requests
import json
from pprint import pprint

res = requests.get('https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426?applicationId=1009993429057254143')

json_data = json.loads(res.text)
pprint(json_data)
    
import pandas as pd

# mediumカテゴリの親カテゴリの辞書
parent_dict = {}

df = pd.DataFrame(columns=['category1','category2','category3','categoryId','categoryName'])

# 大カテゴリ
for category in json_data['result']['large']:
    df = df.append({'category1':category['categoryId'],'category2':"",'category3':"",'categoryId':category['categoryId'],'categoryName':category['categoryName']}, ignore_index=True)

# 中カテゴリ
for category in json_data['result']['medium']:
    df = df.append({'category1':category['parentCategoryId'],'category2':category['categoryId'],'category3':"",'categoryId':str(category['parentCategoryId'])+"-"+str(category['categoryId']),'categoryName':category['categoryName']}, ignore_index=True)
    parent_dict[str(category['categoryId'])] = category['parentCategoryId']

# 小カテゴリ
for category in json_data['result']['small']:
    df = df.append({'category1':parent_dict[category['parentCategoryId']],'category2':category['parentCategoryId'],'category3':category['categoryId'],'categoryId':parent_dict[category['parentCategoryId']]+"-"+str(category['parentCategoryId'])+"-"+str(category['categoryId']),'categoryName':category['categoryName']}, ignore_index=True)

# キーワードを含む行を抽出
df_keyword = df.query('categoryName.str.contains("魚s")', engine='python')

# 「煮魚」カテゴリの人気レシピを取得
res = requests.get('https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426?format=json&categoryId=32-339&applicationId=1009993429057254143')

json_data = json.loads(res.text)
pprint(json_data)