# pip install folium
# m.save('index.html')

import folium
# 위도( latitude ), 경도 ( longitude ) 정보
m = folium.Map(location=[36.763718, 127.28194050])
folium.Marker([36.763718, 127.28194050], popup="point Here").add_to(m)

m.save('지도_01.html')




