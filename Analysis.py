import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from pytrends.request import TrendReq

#setup pytrend library and define keyword

pytrends = TrendReq(hl='en-US', tz=360)
keyword="AI"
#Data Request
pytrends.build_payload([keyword], cat =0, timeframe = 'today 12-m', geo='', gprop='') 
#data from today to last 12 months, from all the categories, geography is global, gprop is only google

#countrywise data
region_data = pytrends.interest_by_region()
region_data = region_data.sort_values(by =keyword, ascending=False).head(15)

plt.figure(figure=(10,6))
sns.barplot(x=region_data[keyword], y=region_data.index, palette='Blues_d')
plt.title(f"Top countries searching for '{keyword}'")
plt.xlabel("Interest")
plt.ylabel("Country")
plt.show()

#world map
region_data=region_data.reset_index()
fig=px.choropleth(region_data, locations='geoName',
                  locationmode='country names', 
                  color=keyword, 
                  title=f"Search Interest for '{keyword}' by Country", 
                  color_continuous_scale='Blues')
fig.show()
 
 #time wise interest
time_df = pytrends.interest_over_time()
plt.figure(figsize=(12,6))
plt.plot(time_df.index, time_df[keyword], marker='o', color='purple')
plt.title(f"Search interest over time '{keyword}'")
plt.xlabel('Date')
plt.ylabel('Interest')
plt.grid(True)
plt.show()

#Comparing Multiple keywords
kw_list = ["AI", "data science", "jobs"]
pytrends.build_payload(kw_list, cat =0, timeframe = 'today 12-m', geo='', gprop='') 

compare_df = pytrends.interest_over_time()
plt.figure(figsize=(12,6))
for kw in kw_list:
    plt.plot(compare_df.index, compare_df[kw], label=kw)

plt.title("Keyword Comparision over time")
plt.xlabel('Date')
plt.ylabel('Interest')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()