# class_='<strong class="tit_subject">2. 정답을 찾는 사람 vs 기준을 세우는 사람</strong>'

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 크롬 브라우저 실행
driver = webdriver.Chrome()   # 크롬 브라우저 객체 생성

# 접속할 페이지 URL준비
url = 'https://brunch.co.kr/keyword/IT_%ED%8A%B8%EB%A0%8C%EB%93%9C?q=g'

# 해당 URL로 이동 ( 페이지 열기 )
driver.get(url)

# 데이터가 로딩될 시간을 대기함 - 5초간 대기상태( pending )
time.sleep(5)

# 클래스 선택자가 tit_subject인 요소들을 찾기
# find_eleement는 한 개만 반환
# file_elements는 조건에 맞는 요소들 여러 개 찾아서 리스트로 반환함.
# searchs = driver.find_elements(By.XPATH,'//*[@id="center"]/yt-searchbox/div[1]/div/form/input')
class_elements = driver.find_elements(By.CLASS_NAME, 'tit_subject')
cnt = len(class_elements)
print(cnt)    # list의 담긴 원소의 갯수
print(type(class_elements))   # class_elements변수의 타입
# 브라우저 종료( 크롬 + driver프로세스 종료 처리 )
driver.quit()
