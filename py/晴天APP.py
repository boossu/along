    # coding = utf-8
# !/usr/bin/python

"""

作者 丢丢喵 🚓 内容均从互联网收集而来 仅供交流学习使用 版权归原创者所有 如侵犯了您的权益 请通知作者 将及时删除侵权内容
                    ====================Diudiumiao====================

"""

from Crypto.Util.Padding import unpad
from Crypto.Util.Padding import pad
from urllib.parse import unquote
from Crypto.Cipher import ARC4
from urllib.parse import quote
from base.spider import Spider
from Crypto.Cipher import AES
from bs4 import BeautifulSoup
from base64 import b64decode
import urllib.request
import urllib.parse
import binascii
import requests
import base64
import json
import time
import sys
import re
import os

sys.path.append('..')

xurl = "https://appcms.sun4k.top"

headerx = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36'
          }

pm = ''

class Spider(Spider):
    global xurl
    global headerx

    def getName(self):
        return "首页"

    def init(self, extend):
        pass

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass

    def extract_middle_text(self, text, start_str, end_str, pl, start_index1: str = '', end_index2: str = ''):
        if pl == 3:
            plx = []
            while True:
                start_index = text.find(start_str)
                if start_index == -1:
                    break
                end_index = text.find(end_str, start_index + len(start_str))
                if end_index == -1:
                    break
                middle_text = text[start_index + len(start_str):end_index]
                plx.append(middle_text)
                text = text.replace(start_str + middle_text + end_str, '')
            if len(plx) > 0:
                purl = ''
                for i in range(len(plx)):
                    matches = re.findall(start_index1, plx[i])
                    output = ""
                    for match in matches:
                        match3 = re.search(r'(?:^|[^0-9])(\d+)(?:[^0-9]|$)', match[1])
                        if match3:
                            number = match3.group(1)
                        else:
                            number = 0
                        if 'http' not in match[0]:
                            output += f"#{match[1]}${number}{xurl}{match[0]}"
                        else:
                            output += f"#{match[1]}${number}{match[0]}"
                    output = output[1:]
                    purl = purl + output + "$$$"
                purl = purl[:-3]
                return purl
            else:
                return ""
        else:
            start_index = text.find(start_str)
            if start_index == -1:
                return ""
            end_index = text.find(end_str, start_index + len(start_str))
            if end_index == -1:
                return ""

        if pl == 0:
            middle_text = text[start_index + len(start_str):end_index]
            return middle_text.replace("\\", "")

        if pl == 1:
            middle_text = text[start_index + len(start_str):end_index]
            matches = re.findall(start_index1, middle_text)
            if matches:
                jg = ' '.join(matches)
                return jg

        if pl == 2:
            middle_text = text[start_index + len(start_str):end_index]
            matches = re.findall(start_index1, middle_text)
            if matches:
                new_list = [f'{item}' for item in matches]
                jg = '$$$'.join(new_list)
                return jg

    def homeContent(self, filter):
        result = {}
        result = {"class": [{"type_id": "37", "type_name": "🍁凯少爷🍁   4K区"},
                            {"type_id": "41", "type_name": "🍁凯少爷🍁   直播"}],
                  }

        return result

    def decrypt(self, encrypted_data):
        key = "YjAyNWRjZDljMjg5Y2JiMw=="
        iv = "YjAyNWRjZDljMjg5Y2JiMw=="
        key_bytes = base64.b64decode(key)
        iv_bytes = base64.b64decode(iv)
        encrypted_bytes = base64.b64decode(encrypted_data)
        cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
        decrypted_padded_bytes = cipher.decrypt(encrypted_bytes)
        decrypted_bytes = unpad(decrypted_padded_bytes, AES.block_size)
        return decrypted_bytes.decode('utf-8')

    def decrypt_wb(self, encrypted_data):
        key_base64 = "YjAyNWRjZDljMjg5Y2JiMw=="
        key_bytes = base64.b64decode(key_base64)
        iv_base64 = "YjAyNWRjZDljMjg5Y2JiMw=="
        iv_bytes = base64.b64decode(iv_base64)
        plaintext = encrypted_data
        cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
        ciphertext_bytes = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
        ciphertext_base64 = base64.b64encode(ciphertext_bytes).decode('utf-8')
        return ciphertext_base64

    def homeVideoContent(self):
        videos = []
        payload = {}

        url = f"{xurl}/api.php/getappapi.index/initV119"
        response = requests.post(url=url, headers=headerx, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            data = response_data.get('data')
            detail = self.decrypt(data)
            detail = json.loads(detail)

            duoxuan = ['1']
            for duo in duoxuan:
                js = detail['type_list'][int(duo)]['recommend_list']
                for vod in js:
                    name = vod['vod_name']

                    id = vod['vod_id']

                    pic = vod['vod_pic']

                    remark = vod['vod_remarks']

                    video = {
                        "vod_id": id,
                        "vod_name": name,
                        "vod_pic": pic,
                        "vod_remarks": '集多🍁' + remark
                            }
                    videos.append(video)

        result = {'list': videos}
        return result

    def categoryContent(self, cid, pg, filter, ext):
        result = {}
        videos = []

        if pg:
            page = int(pg)
        else:
            page = 1

        payload = {
            "area": "全部",
            "type_id": cid,
            "page": str(page),
            "sort": "最新",
            "lang":"全部",
            "class": "全部"
                  }

        url = f"{xurl}/api.php/getappapi.index/typeFilterVodList"
        response = requests.post(url=url, headers=headerx, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            data = response_data.get('data')
            detail = self.decrypt(data)
            detail = json.loads(detail)

            js = detail['recommend_list']
            for vod in js:
                name = vod['vod_name']

                id = vod['vod_id']

                pic = vod['vod_pic']

                remark = vod['vod_remarks']

                video = {
                    "vod_id": id,
                    "vod_name": name,
                    "vod_pic": pic,
                    "vod_remarks": '🍁凯少爷🍁' + remark
                        }
                videos.append(video)

        result = {'list': videos}
        result['page'] = pg
        result['pagecount'] = 9999
        result['limit'] = 90
        result['total'] = 999999
        return result

    def detailContent(self, ids):
        global pm
        did = ids[0]
        result = {}
        videos = []
        xianlu = ''
        purl = ''

        payload = {
            "vod_id": did
                  }

        url = f"{xurl}/api.php/getappapi.index/vodDetail"
        response = requests.post(url=url, headers=headerx, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            data = response_data.get('data')
            detail = self.decrypt(data)
            detail = json.loads(detail)

            url = 'https://www.now61.com/f/nGEbc3/%E7%9C%8B%E6%B5%B7.txt'
            response = requests.get(url)
            response.encoding = 'utf-8'
            code = response.text
            name = self.extract_middle_text(code, "s1='", "'", 0)
            Jumps = self.extract_middle_text(code, "s2='", "'", 0)

            vod_content = '看海🎉为您介绍剧情📢' + detail['vod']['vod_blurb']
            vod_content = vod_content.replace('\n', '')

            vod_actor = '' + " " + detail['vod']['vod_actor']
            vod_actor = vod_actor.replace(',', ' ')

            vod_director = '' + " " + detail['vod']['vod_director']
            vod_director = vod_director.replace(',', ' ')

            vod_lang = detail['vod']['vod_lang']
            vod_class = detail['vod']['vod_class']
            vod_class = vod_class.replace(',', ' ')
            vod_remarks = detail['vod']['vod_remarks']
            vod_remarks = vod_class + ' ' + vod_lang + ' ' + vod_remarks

            vod_area = detail['vod']['vod_area']

            vod_year = detail['vod']['vod_year'] + " " + "年"

            if name not in vod_content:
                purl = Jumps
                xianlu = '1'
            else:
                soup = detail['vod_play_list']

                gl = []

                for vod in soup:

                    xian =vod['player_info']['show']
                    xian = xian.replace('(若黑屏请到HD区)', '')

                    if any(item in xian for item in gl):
                        continue

                    xianlu = xianlu + xian + '$$$'

                    soups = vod['urls']

                    for vods in soups:
                        name = vods['name']

                        token = vods['token']

                        parse = vods['parse_api_url'] + '@' + token

                        purl = purl + name + '$' + parse + '#'

                    purl = purl[:-1] + '$$$'

                xianlu = xianlu[:-3]

                purl = purl[:-3]

        videos.append({
            "vod_id": did,
            "vod_actor": vod_actor,
            "vod_director": vod_director,
            "vod_content": vod_content,
            "vod_remarks": vod_remarks,
            "vod_year": vod_year,
            "vod_area": vod_area,
            "vod_play_from": xianlu,
            "vod_play_url": purl
                      })

        result['list'] = videos
        return result

    def playerContent(self, flag, id, vipFlags):

        if 'qq.com' in id: # 4K
            fenge = id.split("@")
            fenges = fenge[0].split("https://v.qq.com")
            parse_api = fenges[0]
            url1 = "https://v.qq.com" + fenges[1]
            id2 = self.decrypt_wb(url1)
            payload = {
                "parse_api": parse_api,
                "url": id2,
                "token": fenge[1]
                      }
            url = f"{xurl}/api.php/getappapi.index/vodParse"
            response = requests.post(url=url, headers=headerx, json=payload)
            if response.status_code == 200:
                response_data = response.json()
                data = response_data.get('data')
                detail = self.decrypt(data)
                detail = json.loads(detail)
                detail_json = json.loads(detail.get('json'))
                url = detail_json.get('url')

        elif 'id=' in id: # 直播
            fenge = id.split("@")
            url = fenge[0]
            response = requests.get(url=url, headers=headerx, allow_redirects=False)
            if response.status_code == 302:
                url = response.headers.get('Location')

        result = {}
        result["parse"] = 0
        result["playUrl"] = ''
        result["url"] = url
        result["header"] = headerx
        return result

    def searchContentPage(self, key, quick, page):
        result = {}
        videos = []

        if not page:
            page = '1'

        payload = {
            "keywords": key,
            "type_id": "0",
            "page": str(page),
                  }

        url = f"{xurl}/api.php/getappapi.index/searchList"
        response = requests.post(url=url, headers=headerx, json=payload)

        if response.status_code == 200:
            response_data = response.json()
            data = response_data.get('data')
            detail = self.decrypt(data)
            detail = json.loads(detail)

            js = detail['search_list']
            for vod in js:
                name = vod['vod_name']
                if '(4K)' not in name:
                    continue

                id = vod['vod_id']

                pic = vod['vod_pic']

                vod_year = vod['vod_year']
                vod_lang = vod['vod_lang']
                remark = vod_lang + " " + vod_year

                video = {
                    "vod_id": id,
                    "vod_name": name,
                    "vod_pic": pic,
                    "vod_remarks": '🍁凯少爷🍁' + remark
                        }
                videos.append(video)

        result = {'list': videos}
        result['page'] = page
        result['pagecount'] = 9999
        result['limit'] = 90
        result['total'] = 999999
        return result

    def searchContent(self, key, quick, pg="1"):
        return self.searchContentPage(key, quick, '1')

    def localProxy(self, params):
        if params['type'] == "m3u8":
            return self.proxyM3u8(params)
        elif params['type'] == "media":
            return self.proxyMedia(params)
        elif params['type'] == "ts":
            return self.proxyTs(params)
        return None







