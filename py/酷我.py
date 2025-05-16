import  requests  # 导入requests库，用于发送HTTP请求 
import  json  # 导入json库，用于处理JSON数据

def get_kw_headers():    
                """    
                   获取酷我音乐搜索所需的请求头信息。    
                   返回:       
                    dict: 包含User-Agent、Referer和Content-Type的字典    
                    """  
               return {       
                     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",      
                      "Referer": "https://www.kuwo.cn/",     
                       "Content-Type": "application/json"    }


def save_to_json(data, filename='news.json'):   
 """    
将数据保存为JSON文件。    
参数:       
 data (dict or list): 要保存的数据        
 filename (str): 保存的文件名，默认为'news.json'    
 """    
 try:       
  with open(filename, 'w', encoding='utf-8') as f:            
 # 使用json.dump将数据写入文件，ensure_ascii=False确保中文字符正常显示，indent=4使JSON格式化更美观            
 json.dump(data, f, ensure_ascii=False, indent=4)        
 print(f"数据已成功保存到 {filename}")    except IOError as e:        # 捕获文件操作中的IO错误并打印错误信息        print(f"保存文件失败: {e}")
def search_music(keyword, page=1, rn=30):    """    根据关键词搜索酷我音乐，并返回指定页码和数量的结果。    参数:        keyword (str): 搜索的关键词，如歌手名、歌曲名等        page (int): 页码，默认为第1页        rn (int): 每页返回的结果数量，默认为30条    返回:        list: 包含搜索结果的列表，如果请求失败则返回None    """    # 酷我音乐搜索音乐的API URL    url = 'https://www.kuwo.cn/search/searchMusicBykeyWord?vipver=1&client=kt&ft=music&cluster=0&strategy=2012&encoding=utf8&rformat=json&mobi=1&issubtitle=1&show_copyright_off=1'
    # 请求参数，包括搜索关键词、页码和每页结果数量    params = {        "all": keyword,  # 搜索关键词，使用'all'字段表示全字段搜索        "pn": page,  # 页码        "rn": rn  # 每页结果数量    }    # 发送GET请求，附带请求头和参数    resp = requests.get(url, headers=get_kw_headers(), params=params)    # 检查响应状态码是否为200（表示请求成功）    if resp.status_code == 200:        try:            # 解析响应的JSON数据            data = resp.json()            # 从解析后的数据中提取'abslist'字段，该字段包含搜索结果的列表            abslist = data.get("abslist", [])            MUSICRID = [item['MUSICRID'] for  item  in  abslist]            # 处理每个字符串，截取掉前面的6个字符，保存后面的全部内容            MUSICRID = [item[6:] for  item  in  MUSICRID]            return MUSICRID        except json.JSONDecodeError:            # 如果JSON解析失败，打印错误信息并返回None            print("响应数据不是有效的JSON格式")            return None    else:        # 如果请求不成功，打印状态码和错误信息        print(f"请求失败，状态码: {resp.status_code}")        return Noneif __name__ == "__main__":    """    主程序入口，执行搜索音乐并保存结果到JSON文件的操作。    """    # 调用search_music函数，搜索关键词'周杰伦'，第2页，每页10条结果    data = search_music('周杰伦', 1, 10)    url = 'https://www.kuwo.cn/openapi/v1/www/lyric/getlyric?httpsStatus=1&reqId=0a232110-17b1-11f0-a7ab-ebfff1a198dd&plat=web_www&from='    params = {"musicId": data[0]}  # 使用第一个音乐ID作为参数    resp = requests.get(url, headers=get_kw_headers(), params = params)  # 使用 requests 库发送请求    if  resp.status_code == 200:  # 如果状态码为 200，表示请求成功        json_data = resp.json()   # 返回的JSON 数据        lyrics = [item['lineLyric'] for  item  in  json_data['data']['lrclist']]   # 取出data->lrclist->lineLyric        print(lyrics)  # 打印歌词        save_to_json(lyrics)#保存成文件