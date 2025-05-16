import requests
# 请求URLurl = "https://kzb29rda.com/prod-api/iptv/getIptvList?liveType=0&deviceType=1"
# 发送GET请求response = requests.get(url)
# 检查请求是否成功if response.status_code == 200:    # 解析JSON响应    data = response.json()
    # 检查响应中是否包含list    if "list" in data:        # 遍历list中的每个元素        result = []        for item in data["list"]:            # 获取play_source_name和play_source_code            name = item.get("play_source_name", "")            name_id = item.get("play_source_code", "")
            # 组成新的字符串并添加到结果数组中            if name and name_id:                result.append(f"{name},http://192.168.2.245:2086/kzb.php?id={name_id}")
        # 输出所有元素        for line in result:            print(line)    else:        print("响应中未找到list")else:    print(f"请求失败，状态码: {response.status_code}")