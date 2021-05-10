
# SANGSANG_V2
**온라인 클래스 실시간 쌍방향 수업 접속 봇 sangsangbot V2**


## 목차

- [상상봇](#상상봇)
- [기능](#기능)
- [사용법](#사용법)
- [할일](#할일)
- [주의](#주의)

----

# 상상봇

>  예전 온라인클래스는 URL에 쿼리 파라미터에 유저 정보를 모두 담고있었는데  현재는
> /open-api/meeting/v1/verify 에서 API를 통해 json 형식으로 유저 정보를 받아온다.
> 
>    상상봇은 flask 모듈로 API 서버를 만들고  fiddlerscript를 이용해서
> /open-api/meeting/v1/verify 를 localhost:5000/verify 로 리다이렉트시켜  가상의 유저
> 정보를 만들어 받아오고  selenium을 통해 쌍방향 수업에 참여시킨다.

# 기능

원하는 실시간 수업에 봇을 원하는만큼 넣을 수 있습니다.

- 봇 이름 설정
- 봇 아이피 설정
- 봇 개수 설정
- 이외에 봇 로그인 관련 옵션을 설정할 수 있습니다.

### config.json
	URL =  실시간 쌍방향 수업 링크
	IP =  봇 아이피
	email =  봇 아이피
	name =  봇 이름	 
	grade =  학교 (ex. middle = 중학교)
	schoolGrade =  학년
	schoolClass =  반
	schoolNo =  번호
	count = 만들 봇 개수
  
	나머지 옵션은 온라인클래스 실시간 쌍방향 수업 사이트 구조에 대한 이해가 있으신분들이 아니라면 기본 옵션으로 두시는걸 추천합니다.
	

# 사용법

- python 3 설치 필요 https://www.python.org/downloads/
- 크롬 드라이버 필요 https://chromedriver.chromium.org/downloads/
- FiddlerClassic 필요 https://www.telerik.com/fiddler/fiddler-classic

### 필요한 모듈
	pip install selenium
	pip install configparser
	pip install random2
 	pip install json
	pip install urllib3
	pip install random2
	pip install Flask  
  
### 실행방법
	1. 자신의 크롬 버전에 맞는 크롬 드라이버 다운로드후 client.py와 같은 디렉토리에 위치
	2. 아래 FiddlerClassic 설정 방법 참고
	3. config.json에서 URL등 설정
	4. server.py 실행
	5. client.py 실행
	6. chrome://settings/content 페이지 로드
	7. 권한 - 카메라 '액세스하기 전에 확인(권장)' 클릭하여 카메라 차단
	8. 권한 - 마이크 '액세스하기 전에 확인(권장)' 클릭하여 마이크 차단
	9. Enter 입력시 실행
	10. 종료시 Ctrl+C 입력

#### FiddlerClassic 다운로드 후 위쪽 메뉴 Rules - Customize Rules - OnBeforeRequest에 스크립트 추가
![enter image description here](https://raw.githubusercontent.com/Junw00/SANGSANG_V2/main/etc/fiddlerscript.PNG)
```C#
if (oSession.PathAndQuery=="/open-api/meeting/v1/verify" && oSession.isHTTPS) {
		oSession.oRequest.headers.UriScheme = "http";
		oSession.url = "127.0.0.1:5000/verify";
}
```
> C:\Users\Username\Documents\Fiddler2\Scripts 에  [CustomRules.js](https://github.com/Junw00/SANGSANG_V2/blob/main/etc/CustomRules.js)를 덮어씌워도 됩니다.


# 할일
- [ ] 서버 수정 (급함)
- [ ] 채팅 기능추가
- [ ] 캠 기능추가

# 주의
- 재미삼아 만들어보았습니다.
- **본 코드로 인해 일어나는 불이익은 책임지지 않습니다.**
- 코드가 지저분합니다.
- (신) 중학교 EBS온라인클래스에서만 테스트 되었습니다.
- 아직 버그가 있습니다, 계속 업데이트할 예정입니다.
