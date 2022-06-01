import json

filename = 'data/eq_data_30_day_m1.json'
# 从json文件中读取数据
with open(filename) as f:
    all_eq_data = json.load(f)
all_eq_dicts = all_eq_data['features']
# 提取位置数据
mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

# 打印数据
if __name__ == '__main__':
    print(mags[:5])
    print(titles[:5])
    print(lons[:5])
    print(lats[:5])
[0.96, 1.2, 4.3, 3.6, 2.1]
['M 1.0 - 8km NE of Aguanga, CA', 'M 1.2 - 11km NNE of North Nenana, Alaska', 'M 4.3 - 69km NNW of Ayna, Peru', 'M 3.6 - 126km SSE of Cold Bay, Alaska', 'M 2.1 - 21km NNW of Tehachapi, CA']
[-116.7941667, -148.9865, -74.2343, -161.6801, -118.5316667]
[33.4863333, 64.6673, -12.1025, 54.2232, 35.3098333]
import json
import plotly.express as px
import pandas as pd


filename = 'data/eq_data_30_day_m1.json'
# 从json文件中读取数据
with open(filename) as f:
    all_eq_data = json.load(f)
all_eq_dicts = all_eq_data['features']
mags, titles, lons, lats = [], [], [], []
# 提取位置数据
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)
# 封装数据
data = pd.DataFrame(
    data=zip(lons, lats, titles, mags), columns=['经度', '纬度', '位置', '震级']
)
# 绘制震级散点图
fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title='全球地震散点图',
    size='震级',
    size_max=10,
    color='震级',
    hover_name='位置',
)
# 将数据写入html文件中并在网页中显示
fig.write_html('global_earthquakes.html')
fig.show()