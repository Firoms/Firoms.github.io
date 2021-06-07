'''
파이썬에서 기본으로 제공하는 gtts 라이브러리를 이용해보았다.
영어 발음과 한국어 발음이 약간씩 어색하지만, 무료라는 점에서 메리트가 있다,
기능이 적은 것이 단점이지만, 그만큼 사용하는 방법은 간단하다.
tts는 텍스트를 음성으로 변환해주는 Text to Speech의 줄임말로 보통 mp3 파일로 변환할 수 있는 것 같다.
mp3 파일은 playsound 라이브러리를 이용하여 들을 수 있다.
'''

from gtts import gTTS
from playsound import playsound

text1 = "Hi, everybody. Playing with Python is fun"

tts = gTTS(text=text1, lang="en")
tts.save("helloEN.mp3")
playsound("helloEN.mp3")
text2 = "안녕하세요, 여러분. 파이썬으로 노는 것은 재미있습니다"

tts = gTTS(text=text2, lang="ko")
tts.save("helloKO.mp3")
playsound("helloKO.mp3")



'''
kakao openAPI를 이용한 tts
request로 원하는 내용을 입력하여 mp3파일을 만들 수 있다.
단 with open() as 구절을 활용하여야 받은 API를 mp3 파일로 변환 할 수 있다.
마찬가지로 playsound 라이브러리를 이용하여 mp3 파일을 들을 수 있다.
'''

import requests
from playsound import playsound

# 한국어 tts >> 나름 괜찮은 억양

url = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
body = '<speak>\
 <voice name="WOMAN_READ_CALM"> 지금은 여성 차분한 낭독체입니다.</voice>\
 <voice name="MAN_READ_CALM"> 지금은 남성 차분한 낭독체입니다.</voice>\
 <voice name="WOMAN_DIALOG_BRIGHT"> 안녕하세요. 여성 밝은 대화체예요.</voice>\
 <voice name="MAN_DIALOG_BRIGHT"> 안녕하세요. 남성 밝은 대화체예요.</voice>\
 </speak>\
'

headers = {
    "Content-Type": "application/xml",
    "Authorization": "KakaoAK c1702abfa4758f212a4f77684968eda9",
}

r = requests.post(url, data=body.encode("utf-8"), headers=headers)

with open("result1.mp3", "wb") as f:
    f.write(r.content)

playsound("result1.mp3")


# 영어 tts 테스트 >> 영어 역시 한국어 억양으로 발음하는 문제점

url = 'https://kakaoi-newtone-openapi.kakao.com/v1/synthesize'
body ='<speak>\
 <voice name="WOMAN_READ_CALM"> Hi im calm. </voice>\
 <voice name="MAN_READ_CALM"> Hi im calm. </voice>\
 <voice name="WOMAN_DIALOG_BRIGHT"> Hi im bright. </voice>\
 <voice name="MAN_DIALOG_BRIGHT"> Hi im bright. </voice>\
 </speak>\
'

headers = {
    'Content-Type': 'application/xml',
    'Authorization': 'KakaoAK c1702abfa4758f212a4f77684968eda9',
    }

r = requests.post(url, data=body, headers=headers)

with open('resul2t.mp3', 'wb') as f:
    f.write(r.content)
playsound("result2.mp3")
