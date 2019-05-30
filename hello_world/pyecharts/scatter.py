from pyecharts import Scatter
import pandas as pd

dfboy = pd.DataFrame()
dfboy['weight'] = [56,67,65,70,57,60,80,85,76,64]
dfboy['height'] = [162,170,168,172,168,172,180,176,178,170]

dfgirl = pd.DataFrame()
dfgirl['weight'] = [50,62,60,70,57,45,62,65,70,56]
dfgirl['height'] = [155,162,165,170,166,158,160,170,172,165]

scatter = Scatter(title = "体格数据",width = 600,height = 420)
scatter.add(name = "boy", x_axis = dfboy['weight'], y_axis = dfboy['height'])
scatter.add(name = "girl", x_axis = dfgirl['weight'], y_axis = dfgirl['height'],
           yaxis_min = 130,yaxis_max = 200,xaxis_min = 30,xaxis_max = 100)

scatter.render("散点图示范.html")

scatter