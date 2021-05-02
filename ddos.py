#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- author: lzw5399 -*-
import os

while True:
    os.system('''curl 'https://redmine.synyi.com/projects/bank/issues/new' \
      -H 'authority: redmine.synyi.com' \
      -H 'cache-control: max-age=0' \
      -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"' \
      -H 'sec-ch-ua-mobile: ?0' \
      -H 'upgrade-insecure-requests: 1' \
      -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36' \
      -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
      -H 'sec-fetch-site: same-origin' \
      -H 'sec-fetch-mode: navigate' \
      -H 'sec-fetch-user: ?1' \
      -H 'sec-fetch-dest: document' \
      -H 'referer: https://redmine.synyi.com/projects/bank/issues?query_id=2364' \
      -H 'accept-language: en,zh-CN;q=0.9,zh;q=0.8,eo;q=0.7,de;q=0.6' \
      -H 'cookie: autologin=53c4177818d4edf8bb436d090ea0c37376d4c655; _ga=GA1.2.909375640.1599446152; __cfduid=dd0534999ee6df3fc374724ee1499e1e61617762675; _redmine_session=Q0wzc0REYTlyQXZRNUNjRFlHWUZVRlh5OWljWjU1dUg2TFV1STJzaG9iOWdGRXJsbGZCY0c5MUdkc0xuYlBFRnBWSy9PeHc3dndpaGRseGxOeGx5R2dTaXQ2czZrM0dGcGw1bkgwOTdVaGNyaXZWZzVpMDFzQ0cwODhET3NVcXYrZnF3UzBncHFFM3VMcTJqMFB2UEY4b1kvSnVuTzJodldTNmx3Mm5lOEo5L3hjNU1md2ZOWlptZGNPRW1aai9lRXFkSEswdkt1dVRUcEVuR0lKbVAzWEtmblExci9QeFRtNDZ5dE9XT2tWZlRLOEFLWnBuZzcyMVdOSlNoZy9FOUJ4Y2NIVE9tS3gwRnQyUW1YaENTTjJoTE95V3JvdEthUVVhWlU3Q0c5UU9BNEVZL2lOcjJVNGJyTTJueXMwVVRFUzRUaFU1RTZQSFlNR2JEaGhETmx3PT0tLVY0cjBnOFBXNE5HQWs5SFRGQ0VRa1E9PQ%3D%3D--983555d2510bae9eb8f5f313322a73d820a2af6a' \
      -H 'if-none-match: W/"8b74e9ce99aa0ff6411c1236870651bb"' \
      --compressed''')