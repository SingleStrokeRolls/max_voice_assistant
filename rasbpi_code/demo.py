import requests

API_KEY = ""
SECRET_KEY = ""

def main():
        
    url = "https://tsn.baidu.com/text2audio"
    
    payload='tok='+ get_access_token() +'&cuid=S3J2DtAKRtoCqKE3uq5PHbtnNtsYlHK9&ctp=1&lan=zh&spd=5&pit=5&vol=5&per=1&aue=3'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)

def get_access_token():
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

if __name__ == '__main__':
    main()

