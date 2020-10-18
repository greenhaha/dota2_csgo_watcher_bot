import requests

header = {
    "Host": "api.wmpvp.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://news.wmpvp.com",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G9750 Build/LMY49I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 EsportsApp Version=1.4.3.43",
    "Content-Type": "application/json;charset=UTF-8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,en-US;q=0.8"
}

url = "https://api.wmpvp.com/api/v1/csgo/detailStats"
payload = {
    "accessToken": "a70745395cf1984eea76414b71a990c88b348aca",
    "gameAbbr": "CSGO",
    "module": "report",
    "moduleId": "LOCAL@ce82eafff43ce369",
    "pageNum": 1,
    "pageSize": 20,
    "commentId": "0",
    "platform": "admin",
    "sort": 2,
    "type": 1
}
p = '{"gameAbbr":"CSGO","steamId":"76561198099402352","accessToken":null,"lastTimeStamp":"","dataSource":0} '
print(requests.post(url, headers=header, data=p).content)
