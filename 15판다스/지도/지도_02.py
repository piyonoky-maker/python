import folium
# marker 생성
lat = 36.763718
lng = 127.28194050

# 위도( latitude ), 경도 ( longitude ) 정보
m = folium.Map(location=[lat, lng], zoom_start=15, titles='OpenStreetMap', width=800, height=450)
# Maker클래스. 플래스 생성시에 파라미터 값을 적절히 넣어주면 클래스가 가진 기능에 대한
folium.Marker(
    [lat, lng]
    , popup="다른정보"
    , tooltip='풍선도움말'
    , icon=folium.Icon(color='red', icon='glyphicon-heart')   #  https://getbootstrap.com/docs/3.3/components
    # , icon=folium.Icon(color='red', icon='glyphicon glyphicon-ok')
  ).add_to(m)

m.save('지도_02.html')
