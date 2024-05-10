import datetime

import pandas as pd
from elasticsearch import Elasticsearch

restaurant_df = pd.read_csv('restaurants.csv')
menu_df = pd.read_csv('menus.csv')

now = datetime.datetime.now()
index_name = f"restaurant_{now.strftime('%Y_%m_%d_%H-%M')}"

# Elasticsearch 클라이언트 설정
es = Elasticsearch("http://es-singlenode:9200")

# 새 인덱스 생성 및 매핑 설정
if not es.indices.exists(index=index_name):
  es.indices.create(index=index_name, mappings={
    "properties": {
      "name": {"type": "text"},
      "category": {"type": "text"},
      "review_count": {"type": "text"},
      "address": {"type": "text"},
      "rating": {"type": "float"},
      "number": {"type": "text"},
      "image_url": {"type": "text"},
      "custom_category": {"type": "text"},
      "menus": {
        "type": "nested",
        "properties": {
          "menu_name": {"type": "text"},
          "price": {"type": "text"},
          "description": {"type": "text"},
          "is_representative": {"type": "text"},
          "image_url": {"type": "text"}
        }
      }
    }
  })

# 데이터 인덱싱
for _, row in restaurant_df.iterrows():
  menus = menu_df[menu_df['restaurant_id'] == row['id']].to_dict('records')

  for menu in menus:
    if pd.isna(menu['image_url']):
      menu.pop('image_url')  # image_url 필드가 NaN이면 제거

  if pd.isna(row['image_url']):
    restaurant_image_url = None  # NaN 값을 None으로 설정
  else:
    restaurant_image_url = row['image_url']

  if pd.notna(row['rating']):
    rating = float(row['rating'])
  else:
    rating = None

  response = es.index(index=index_name, document={
    "name": row['name'],
    "category": row['category'],
    "review_count": row['review_count'],
    "address": row['address'],
    "rating": rating,
    "number": row['number'],
    "image_url": restaurant_image_url,
    "custom_category": row['custom_category'],
    "menus": menus,
  })
  print(f"Indexed document ID: {response['_id']}, Result: {response['result']}")

# 앨리어스 확인 및 설정
if not es.indices.exists_alias(name="restaurant"):
  # 앨리어스가 없으면 새 인덱스에 앨리어스 생성
  es.indices.put_alias(index=index_name, name="restaurant")
else:
  # 기존에 앨리어스가 있다면, 앨리어스를 새 인덱스로 업데이트하고, 기존 인덱스 삭제
  old_indices = list(es.indices.get_alias(name="restaurant").keys())
  es.indices.update_aliases(body={
    "actions": [
      {"remove": {"index": "*", "alias": "restaurant"}},
      {"add": {"index": index_name, "alias": "restaurant"}}
    ]
  })
  for idx in old_indices:
    if idx != index_name:
      es.indices.delete(index=idx)

print("Indexing complete, and alias updated.")
