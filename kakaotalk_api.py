"""
https://developers.kakao.com/console/app/668813
https://blog.daum.net/geoscience/1624
https://m.blog.daum.net/geoscience/1636

네이티브 앱 키	bf4842bdf053b570669fb19f6a6c7d6d
REST API 키	239f82e410b6e6a346af715d85b81e1f
JavaScript 키	39e60bf616385a5235dd45b31a7924a9
Admin 키	758e29728ac7471833ddce5442891b90


https://kauth.kakao.com/oauth/authorize?client_id=239f82e410b6e6a346af715d85b81e1f&redirect_uri=https://0.0.0.0:3000&response_type=code&scope=talk_message

3BSVHxNabt0WHGx15JYaU8sk1DgzlQeLx7Al9QiiLI_xR3IHn19xBXQynvgjoaUJGYQP9Qo9dNsAAAF9SGOJtQ
"""
# 라이브러리 호출
import requests
import json
# 아래 코드에서 {REST API}, {코드} 부분을 위에서 복사한 내용으로 교체해 줍니다.

# 카카오톡 메시지 API
url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type" : "authorization_code",
    "client_id" : "239f82e410b6e6a346af715d85b81e1f",
    "redirect_url" : "https://0.0.0.0:3000",
    "code" : "3BSVHxNabt0WHGx15JYaU8sk1DgzlQeLx7Al9QiiLI_xR3IHn19xBXQynvgjoaUJGYQP9Qo9dNsAAAF9SGOJtQ"
}
response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# kakao_code.json 파일 저장
with open("kakao_code.json", "w") as fp:
    json.dump(tokens, fp)


url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
headers = {"Authorization": "Bearer " + f"{tokens['access_token']}"}
template = {
    "object_type" : "list",
    "header_title" : "쑤넬이 알람",
    "header_link" : {
        "web_url" : "www.naver.com",
        "mobile_web_url" : "www.naver.com"
    },
    "contents" : [
        {
            "title" : "쑤넬이는 지금?!",
            "description" : "쑤넬이는 무엇을 하고 있을까요?",
            "image_url" : "https://cdn.kado.net/news/photo/201901/948844_399953_0825.jpg",
            "image_width" : 50, "image_height" : 50,
            "link" : {
                "web_url" : "https://www.google.co.kr/search?q=national+park&source=lnms&tbm=nws",
                "mobile_web_url" : "https://www.google.co.kr/search?q=national+park&source=lnms&tbm=nws"
            }
        },
        {
            "title" : "쑤넬이가 울고있어요!", # 쑤넬이가 잠에서 깻어요 / 쑤넬이가 얼굴을 묻고 잇어요 / 쑤넬이가 ...
            "description" : "쑤넬이가 엄마아빠를 찾아요!",
            "image_url" : "https://cdn-images-1.medium.com/max/1200/1*iDQvKoz7gGHc6YXqvqWWZQ.png",
            "image_width" : 50, "image_height" : 50,
            "link" : {
                "web_url" : "https://www.google.co.kr/search?q=deep+learning&source=lnms&tbm=nws",
                "mobile_web_url" : "https://www.google.co.kr/search?q=deep+learning&source=lnms&tbm=nws"
            }
        }
        
    ],
    "buttons" : [
        {
            "title" : "네이버로 이동",
            "link" : {
                "web_url" : "www.naver.com",
                "mobile_web_url" : "www.naver.com"
            }
        }
    ]
    
}

data = {"template_object" : json.dumps(template)}

response = requests.post(url, data=data, headers=headers)

if response.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))
