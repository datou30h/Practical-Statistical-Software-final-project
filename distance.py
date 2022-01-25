from geopy.distance import geodesic

distance = geodesic((39.995304, 116.308264), (40.003304, 116.326759)).km
print("距离：{:.3f}km".format(distance))

import pandas as pd  # 导入Pandas库
data_stations = pd.read_csv('Stations.csv')  # 读取csv数据
data_trips = pd.read_csv('Trips.csv')

import numpy as np

col_1 = data_stations["latitude"]  #获取一列，用一维数据
data_1 = np.array(col_1)
col_2 = data_stations["longitude"]  #获取一列，用一维数据
data_2 = np.array(col_2)
col_3=data_stations["id"]
data_3 = np.array(col_3)
col_4=data_trips["from_station_id"]
data_4 = np.array(col_4)
col_5=data_trips["to_station_id"]
data_5 = np.array(col_5)


import numpy
data_dis_stations = numpy.zeros(shape=(619,619))
data_dis_trips=numpy.zeros(shape=(231635,1))

from geopy.distance import geodesic

for i in range(0,534):
  for j in range(0,534):
        distance = geodesic((data_1[i], data_2[i]), (data_1[j], data_2[j])).km
        data_dis_stations[data_3[i],data_3[j]]=distance

for i in range(0,231635):
    data_dis_trips[i]=data_dis_stations[data_4[i],data_5[i]]
print(data_dis_trips)

import csv

headers = ['distance of trip']
rows = data_dis_trips
with open('distance.csv', 'w', encoding='utf8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)
