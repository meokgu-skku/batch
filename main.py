import json

import redis

import pandas as pd


def decompose_korean_char(char):
  """
  Manually decompose a Korean character into its constituent parts (choseong, jungseong, jongseong).
  This is an improved implementation that also handles double jongseong and jungseong.
  """
  # Korean character decomposition
  if '가' <= char <= '힣':
    base = ord(char) - ord('가')
    jongseong = base % 28
    jungseong = ((base - jongseong) // 28) % 21
    choseong = ((base - jongseong) // 28) // 21

    # Korean character components
    choseong_chars = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
    jungseong_chars = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"
    jongseong_chars = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ',
                       'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ',
                       'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    # Handling double jongseong and jungseong
    double_jongseong_map = {'ㄳ': 'ㄱㅅ', 'ㄵ': 'ㄴㅈ', 'ㄶ': 'ㄴㅎ', 'ㄺ': 'ㄹㄱ',
                            'ㄻ': 'ㄹㅁ',
                            'ㄼ': 'ㄹㅂ', 'ㄽ': 'ㄹㅅ', 'ㄾ': 'ㄹㅌ', 'ㄿ': 'ㄹㅍ',
                            'ㅀ': 'ㄹㅎ', 'ㅄ': 'ㅂㅅ'}
    double_jungseong_map = {'ㅘ': 'ㅗㅏ', 'ㅙ': 'ㅗㅐ', 'ㅚ': 'ㅗㅣ', 'ㅝ': 'ㅜㅓ',
                            'ㅞ': 'ㅜㅔ', 'ㅟ': 'ㅜㅣ', 'ㅢ': 'ㅡㅣ'}

    # Decompose double jongseong and jungseong
    jongseong_char = double_jongseong_map.get(jongseong_chars[jongseong],
                                              jongseong_chars[jongseong])
    jungseong_char = double_jungseong_map.get(jungseong_chars[jungseong],
                                              jungseong_chars[jungseong])

    return choseong_chars[choseong], jungseong_char, jongseong_char
  else:
    return char, '', ''


def generate_autocomplete_data(input_str):
  """
  Generate autocomplete data from the input string by decomposing Korean characters.
  This version handles double jongseong and jungseong and includes partial syllables in the result.
  """
  result = []
  temp_str = ""
  complete_char = ""

  for char in input_str:
    # Decompose the Korean character
    choseong, jungseong, jongseong = decompose_korean_char(char)
    complete_char += char

    # Add partial syllables to the result
    if choseong:
      temp_str += choseong
      result.append((temp_str, complete_char))
    if jungseong:
      temp_str += jungseong
      result.append((temp_str, complete_char))
    if jongseong:
      temp_str += jongseong
      result.append((temp_str, complete_char))

  return result


def apply_highlighting(org_data, highlighted_data):
  """
  Apply HTML <strong> tag to the highlighted part of the original data.
  """
  # Finding the index where the highlighted data ends in the original data
  end_index = org_data.find(highlighted_data) + len(highlighted_data)

  # Constructing the new string with the <strong> tag applied
  highlighted_org_data = org_data[:end_index].replace(
    highlighted_data,
    f"<strong>{highlighted_data}</strong>") + org_data[
                                              end_index:]

  return highlighted_org_data


file_path = 'restaurants.csv'
df = pd.read_csv(file_path)

restaurant_names = df['name'].tolist()
data = {}

for org_data in restaurant_names:
  candidates = [org_data]
  candidates.extend(org_data.split())
  candidates.append(org_data.replace(" ", ""))
  for candidate in candidates:
    generated_data = generate_autocomplete_data(candidate)

    for gd, gdc in generated_data:
      json_data = {
        'org_display': org_data,
        'highlighted_display': apply_highlighting(org_data, gdc),
        'data_type': 'query',
      }
      if gd in data:
        if json_data not in data[gd]:
          data[gd].append(json_data)
      else:
        data[gd] = [json_data]

r = redis.Redis(host='localhost', port=6379, db=0)
version = '20240403232030'
r.set('restaurant:v1:version', version)

for key, value in data.items():
  r.set('restaurant:v1:' + version + ':' + key, json.dumps(value))
