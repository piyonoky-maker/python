from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import InvalidSessionIdException
import time
# 무한 스크롤 처리 함수 구현하기 - 재사용성 고려
def scroll(driver):
  while True:
    # 이전까지 스크롤 이동한 높이값
    before_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
    # 스크롤 바 이동하기 - scrollTo(x좌표, y좌표), execute_script()
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
    
    #print('driver: ', driver)
    # 스크롤 상의 제목 출력
    #titles = scroll(driver)
    #for title in titles:
      #print('제목: {}', title.text)

#time.sleep(2)
    # 스크롤 바 이동하기를 요청한 이후에 높이값
    after_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
#time.sleep(2)
    # 이전 높이와 스크롤 이동 후 높이가 같다는 것은 스크롤 바가 움직임이 없었다 임.
    # 이 경우에는 무한 루프를 탈 출하는 코드 작성할 것
    if before_scroll_height == after_scroll_height:
      break
  time.sleep(3)
  titles = driver.find_elements(By.CLASS_NAME, 'tit_subject')
  print(type(titles)) # class list
  print("글 갯수: ", len(titles))
  return titles
  

# Chrome 옵션: 연결 안성선을 개선
options = Options()
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = None

try:
  driver = webdriver.Chrome()
  print('실행중: 브라우저 창을 닫지 마세요.')
  url = 'https://brunch.co.kr/keyword/IT_%ED%8A%B8%EB%A0%8C%EB%93%9C?q=g'
  driver.get(url)
  time.sleep(5)
  # 무한 스크롤 함수 호출
  titles = scroll(driver)
  # 반복문 통해서 리스트 자료구조의 제목 출력하기
  for title in titles:
    print(title.text)
except InvalidSessionIdException:
  print("오류: 브라우저가 중간에 닫혔거나 연결이 끊겼습니다.")
except Exception as e:
  print("오류: ", e)
finally:
  if driver:
    driver.quit()