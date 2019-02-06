#Hans Rosling data plot.
#Displaying GDP per capita income data. We clearly see that people live longer in countries with a higher GDP per capita. Still, there is a huge difference in life expectancy between countries on the same income level.

#libraries used

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set_style("white")
import pandas as pd
my_dpi=96


#Fetching data

web_url='https://python-graph-gallery.com/wp-content/uploads/gapminderData.csv'
data = pd.read_csv(web_url)

#Transform categorical column (continent) in a numerical value  group 1->1, group 2>2...
data['continent']=pd.Categorical(data['continent'])

#for each year

for i in data.year.unique():

  #initialise a figure

  fig=plt.figure(figsize=(680/my_dpi,480/my_dpi),dpi=my_dpi)

  #color_adjustment

  tmp=data[data.year==i]
  plt.scatter(tmp['lifeExp'], tmp['gdpPercap'] , s=tmp['pop']/200000 , c=tmp['continent'].cat.codes, cmap="Accent", alpha=0.6, edgecolors="white", linewidth=2)

  #adding titles and axis labels

  plt.yscale('log')
  plt.xlabel("Life Expectancy")
  plt.ylabel("GDP per Capita income")
  plt.title("Year: "+str(i))
  plt.ylim(0,100000)
  plt.xlim(30, 90)
  tick_val = [1000,10000,100000]
  tick_lab = ['1k','10k','100k']
  plt.yticks(tick_val, tick_lab)

  plt.show()

  #saving it

  filename='hans_rosling'+str(i)+'.png'
  plt.savefig(filename, dpi=96)
  plt.gca()


