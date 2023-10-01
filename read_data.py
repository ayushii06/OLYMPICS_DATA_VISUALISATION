import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


#reading the csv file
olympics=pd.read_csv("Athletes_summer_games.csv")


#defining the function to drop duplicates

oly_drop_same=olympics.drop_duplicates(subset=['Year','Team','Event','Medal'])

# maximum participation
# participation_country=oly_drop_same.Team.value_counts().sort_values(ascending=False).head(25)
# # print(participation_country)

# plt.figure(figsize=(10,6))
# plt.title("Overall Participation by Country")
# sns.barplot(x=participation_country.index,y=participation_country,palette='Set2')
# plt.xticks(rotation=20)
# plt.xlabel("Countries")
# plt.ylabel("Total Participation")
# plt.show()

# #Age distribution of the participants

# age_distribution=oly_drop_same.Age.value_counts().sort_values(ascending=False).head(30)
# print(age_distribution)

# plt.figure(figsize=(10,6))
# plt.title("Age Distribution of the Participants")
# plt.xlabel("Age")
# plt.ylabel("Number of Participants")
# plt.hist(oly_drop_same.Age,bins=np.arange(10,80,2),color='cyan',edgecolor='blue')
# plt.show()

#Male and Female participants.
# colors=['cyan','green']
# gender=oly_drop_same.Sex.value_counts()
# print(gender)
# plt.figure(figsize=(10,6))
# plt.pie(gender,colors=colors,autopct='%1.1f%%',startangle=90,shadow=True,explode=(0.1,0),labels=['Male','Female'])
# plt.legend(gender.index,loc='upper right')
# plt.title("Male and Female Participation in Olympics")
# plt.show()

#Female participants in each year
female_participants = oly_drop_same[oly_drop_same['Sex']=='F']['Year'].value_counts()
female_participants.sort_index(inplace=True)
print(female_participants)

plt.figure(figsize=(10,6))
plt.plot(female_participants.index,female_participants.values,color='green',marker='o',markerfacecolor='red')
plt.title("Female Participation in Each Year")
plt.xlabel("Year")
plt.ylabel("Participants")
plt.show()

# Geographical Analysis
# area=oly_drop_same.Medal.value_counts().sort_values(ascending=False)
# print(area)
# fig=px.choropleth(area.values,locations=area.index,locationmode='country names',color=area.values,title="Overall Participation by Country",color_continuous_scale=px.colors.sequential.Plasma)
# fig.show()