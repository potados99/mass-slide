
미사 PPT
==========

Mass-slide는 [python-pptx](http://python-pptx.readthedocs.io)의 응용입니다.

`template/`과 `drafts/raw/`를 이용해 .pptx 파일을 생성합니다.

`drafts/done/` 은 스크립트를 실행할 때 마다 새로 업데이트됩니다.


사용법
=====

[python 2.7](https://www.python.org/download/releases/2.7/)과 [python-pptx](http://python-pptx.readthedocs.io)가 필요합니다.

이미 파이썬이 설치되어 있다면, python-pptx를 다음 명령어로 설치할 수 있습니다:

```sh
pip install python-pptx
``` 

다음 명령어로 앱을 실행할 수 있습니다.

```sh
python app.py
```


세부 기능
========

* 템플릿 선택

	템플릿을 선택하고 매주 바뀌는 내용은 `drafts/raw/`에서 업데이트

	선택한 템플릿으로부터 만들어지는 파일 확인 / 수정 가능

* 줄바꿈 인식

	같은 챕터 내에서 한 번 이상의 줄바꿈으로 새로운 슬라이드 생성

	챕터간 줄바꿈은 1회 이상이어야 함

	챕터 시작 후 첫번째 본문 전까지 줄바꿈 횟수 무관

* 챕터 변경 인식

	'#' 기호로 새로운 챕터 생성

	'#BLANK' 챕터는 비어있는 검은 배경의 슬라이드를 생성

* 볼드체 지정

	줄 단위 '**'

	블럭 단위 '***"

* 글씨 크기 유동 조절

	새로운 챕터의 첫번째 볼드 텍스트는 115pt (big)

	챕터별 분류는 fontModule.py에 구현됨

* 장문 자동 자르기

	유니코드 한글 한 줄당 35글자

	한 페이지당 5줄

* 모듈화

	IOModule: 파일 읽기/쓰기, 챕터 리스트 생성, 타이틀 번역, 단계별 쓰기/읽기
	processModule: 파일 읽기, 챕터별 원본텍스트 가공하여 리스트 생성
	fontModule: 챕터별 폰트 사이즈 지정
	pptxModule: 파워포인트 슬라이드 생성


Mass-slide
==========

Mass-slide is an implementation of [python-pptx](http://python-pptx.readthedocs.io).

It creates a .pptx file using 'template.txt'.

The 'template.txt' gets updated everytime you run the script.


Usage
=====

This app requires [python 2.7](https://www.python.org/download/releases/2.7/) and [python-pptx](http://python-pptx.readthedocs.io).

If you already have python, you can install python-pptx easily:

```sh
pip install python-pptx
```

You can use the following commands to start:

```sh
python app.py
```


Notes
=====

More functions will be available soon.

