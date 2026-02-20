from selenium import webdriver
import time
'''
웹 페이지에서 스크롤을 내리면서 스크롤 전/후 문서 높이 어떻게 변하는지 확인하기
브런치 스토리 또는 유튜브 아래로 내릴 수록 글이나 추천영상이 더 로딩되는 무한 스크롤
구조이므로 스크롤을 내리면 페이지 높이가 커질 수 있다.
'''
# 크롬 브라우저 실행
driver = webdriver.Chrome()
## 페이지 접속
driver.get('https://brunch.co.kr/keyword/IT_%ED%8A%B8%EB%A0%8C%EB%93%9C?q=g')
# 현재 페이지의 전체(scrollHeight, scrollTo) 가져오기
# execute_script() -> 브라우저의 스크립트를 실행할 수 있음
# document.documentElement.scrollHeight
# 현재 HTML문서가 스크롤 가능한 전체 길이( 높이 ) 출력
h1 = driver.execute_script('return document.documentElement.scrollHeight')
print(h1)   # 스크롤을 내리기 전 페이지 높이값이 출력

# 페이지 맨 아래로 스크롤 내리기( 1번째 )
# window.scrollTo(x, y): 특정 좌표로 스크롤 이동
# y를  scrollHeight로 주면 맨 아래로 내려 감
driver.execute_script('return document.documentElement.scrollHeight')
time.sleep(3)
h2 = driver.execute_script('return document.documentElement.scrollHeight')
print(h2)       # 스크롤을 내리기 전 페이지 높이 출력됨
time.sleep(3)   # 종료 전 잠깐 대기( 확인용 )
driver.quit()