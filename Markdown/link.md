# 링크 이동 걸기

##외부 사이트 이동 링크 걸기

    그냥 사이트 주소를 넣으면 주소에 이동 링크가 걸린다.
    ex) https://github.com/firoms
    만약 특정 문구에 링크를 걸고 싶을 때에는 [타이틀](주소)로 지정한다.
    ex) [Firoms Github](https://github.com/firoms)

## 같은 프로젝트 내의 다른 markdown 파일 이동 링크

    상대 경로를 이용하여 다른 markdown 파일을 [타이틀](상대경로)로 지정한다.
    ex) [Another Markdown](./folder/another_markdown.md)

## 같은 markdown 파일 내의 이동 링크

    각 헤더 명을 이용하여 [타이틀](헤더 명)으로 지정한다.
    ex) [Firoms 소개](# Firoms 소개)

## 이미지에 링크 걸기

    이미지 주소를 타이틀에 넣어줘서 [![오류 시 보여질 이미지 명](이미지 주소)](주소)로 지정한다.
    [![Firoms 사진](https://firoms/image)](https://github.com/firoms)

### 주의사항
링크에 띄어쓰기가 있으면 연결이 안된다.   
따라서, '-'를 이용하여 띄어쓰기를 표현해준다.   
또한, Github에서 마크다운을 볼 경우에는 '.'이나 '()'와 같은 특수 문자들이 있으면 연결이 안되는 경우가 많으므로 유의 해야 한다.   
(이상하게 다른 마크다운 뷰어에서는 작동하지만, github에서만 작동하지 않아 일일이 해보면서 확인해봐야했다.)   