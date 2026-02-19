from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 크롬 브라우저 실행
driver = webdriver.Chrome()   # 크롬 브라우저 객체 생성

# 접속할 페이지 URL준비
url = 'https://example.com/'

# 해당 URL로 이동 ( 페이지 열기 )
driver.get(url)

# 데이터가 로딩될 시간을 대기함 - 5초간 대기상태( pending )
time.sleep(5)

# 클래스 선택자가 tit_subject인 요소들을 찾기
# values = driver.find_elements(By.TAG_NAME, 'h1')
values = driver.find_elements(By.TAG_NAME, 'p')

# 찾아낸 제목 요소들을 꺼내서  텍스트만 출력하기
# 변수명.text: 요소 안의 화면에 보이는 텍스트 읽어오기
for title in values:
  print(title.text)


# 브라우저 종료( 크롬 + driver프로세스 종료 처리 )
driver.quit()
