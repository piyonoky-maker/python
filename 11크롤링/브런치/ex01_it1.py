from selenium import webdriver
import time

# 크롬 브라우저 실행
driver = webdriver.Chrome()   # 크롬 브라우저 객체 생성

# 접속할 페이지 URL준비
url = 'https://brunch.co.kr/keyword/IT_%ED%8A%B8%EB%A0%8C%EB%93%9C?q=g'

# 해당 URL로 이동 ( 페이지 열기 )
driver.get(url)

# 데이터가 로딩될 시간을 대기함 - 5초간 대기상태( pending )
time.sleep(5)

# 브라우저 종료( 크롬 + driver프로세스 종료 처리 )
driver.quit()
