
미사 PPT
==========

Mass-slide는 [python-pptx](http://python-pptx.readthedocs.io)의 응용입니다.

`templates/`와 `drafts/raw/`를 이용해 .pptx 파일을 생성합니다.

`drafts/processed/`와 `drafts/done/` 은 스크립트를 실행할 때 마다 새로 업데이트됩니다.


설치
===

[python 2.7](https://www.python.org/download/releases/2.7/)과 [python-pptx](http://python-pptx.readthedocs.io)가 필요합니다.

이미 파이썬이 설치되어 있다면, python-pptx를 다음 명령어로 설치할 수 있습니다:

```sh
pip install python-pptx
```

사용법
=====

1. 먼저, 다 영어입니다. 다음 목록을 숙지하세요.

	> cover.txt : 표지  
	pardon.txt : 입당송  
	collect.txt : 본기도  
	first_reading.txt : 제1 독서  
	second_reading.txt : 제2 독서  
	acclamation.txt : 복음환호송  
	gospel.txt : 복음  
	antiphon.txt : 영성체송

2. `templates`에서 템플릿을 선택합니다.

3. `templates/[선택한 템플릿]_updates.txt`을 열어 목록을 봐 둡니다.

4. `drafts/raw/automated`에 위치한 파일 중, 아까 본 그 목록에 있는 파일을 최신으로 업데이트합니다.

	> 예시: templates 폴더의 lent_updates.txt의 내용이
	cover.txt  
	pardon.txt  
	collect.txt  
	first_reading.txt  
	second_reading.txt  
	acclamation.txt  
	gospel.txt  
	antiphon.txt  
	위와 같을 때,  
	drafts/raw/automated 폴더에서 저 파일들을 업데이트합니다.

5. 그리고 다음 명령어를 실행합니다.

	```sh
	python app.py [선택한 템플릿]
	```

세부 기능
========

* 템플릿 선택

	템플릿을 선택하고 매주 바뀌는 내용은 `drafts/raw/`에서 업데이트

	선택한 템플릿으로부터 만들어지는 파일 확인 / 수정 가능

	템플릿에서 업데이트되는 부분은 덮어씌워지므로 기존의 내용은 결과에 영향 없음

	새로 업데이트되는 부분의 목록은 템플릿_updates.txt에 저장됨. 꼭 작성해야 함.

* 줄바꿈 인식

	같은 챕터 내에서 한 번 이상의 줄바꿈으로 새로운 슬라이드 생성

	챕터간 줄바꿈은 1회 이상이어야 함

	챕터 시작 후 첫번째 본문 전까지 줄바꿈 횟수 무관

* 챕터 변경 인식

	'#' 기호로 새로운 챕터 생성

	'#BLANK' 챕터는 비어있는 검은 배경의 슬라이드를 생성

	템플릿 파일에서 비어있는 챕터를 만들려면 내용에 //를 써주면 됨

* 볼드체 지정

	줄 단위 '**'

	블럭 단위 '***'

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
