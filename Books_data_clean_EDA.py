#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


#Loading the cleaned dataset into Jupyter Notebook
df=pd.read_excel(r"C:\Users\deepa\OneDrive\Desktop\Resources_PythonProject\ProjectDatasets\books_data_clean.xlsx")


# In[6]:


df


# In[92]:


#Split the author column as it has multiple authors

author_name=[f"Author{i}" for i in range (1,52)]
print(author_name)

for i in range(0,51):
    df[f'Author{i}']=df[i]
    i=i+1


# In[95]:


for i in range(8,51):
    df.drop(columns=[i], axis=1, inplace=True)


# In[100]:


col_drop=[i for i in range(0,8)]
df.drop(columns=col_drop, axis=1,inplace=True)


# In[101]:


df.info()


# # Top 10 Books based on Average Rating

# In[112]:


#Sorting top books by average rating
top_books=df[['title','average_rating','language_code']].sort_values(by='average_rating', ascending=False)

#Top 10 books based on average rating and the language in which they are written
top_books.head(10)


# We observe that the average rating for all the top 10 books is 5.0. All the books are written in English, except for 1 book that is written in Welsh
# 

# # Language Composition of the Books

# In[124]:


df['language_code'].value_counts().head(5).plot(kind = 'pie', autopct='%1.1f%%', figsize=(8,8)).legend()
plt.show()


# According to the pie chart, ~97% of the books in the dataset are written in English (code: eng, en-US, en-GB). The other top languages are Spanish (code:spa) and French(code:fre)

# # Relationship between Language_Code and Average_Rating

# Objective: To check if the top 5 languges(depicted by the pie chart above) contribute to a higher rating

# In[137]:


plt.figure(figsize=(15,8))
sns.boxplot(x=df.language_code,y=df.average_rating)
plt.show()


# Although ~97% of the books in the dataset are in English, if we consider median of the average rating for each language, we dont see average rating impacted by the language of the book

# # Distribution of Average_Rating of the Books

# In[154]:


#Density Curve for Average Rating
fig,axes=plt.subplots(figsize=(3,3))
sns.kdeplot(df['average_rating'],ax=axes)
plt.title('Probability Density Curve for Average Rating of Books')
plt.xlabel('Average Rating')
plt.show()


# In[309]:


#Understand Number of observations for a Particular average rating
test=pd.DataFrame(df.groupby('average_rating')['title'].count())
test.rename(columns = {'title':'Frequency'}, 
            inplace = True)
test=test.reset_index()
test


# The maximum obseervations are between 3.75-4.27

# In[158]:


#Mean and Median
df['average_rating'].describe(percentiles=[0.5])


# The highest average rating provided by readers is 5.0, lowest is 0.0.The density curve for the average rating is negatively skewed as the tail is towards left. This means more observations are on the left and hence mean<median for negative skewness.

# Now let's check if maximum observations/books have received a rating of 4.0 as per density curve

# In[171]:


#Creating Histogram
fig,axes=plt.subplots(figsize=(10,5))
sns.histplot(df['average_rating'],ax=axes)
plt.title('Number of Books per average_rating')
plt.xlabel('Average Rating')
plt.ylabel('Number of Books')
plt.show()


# # Top 10 Books based on Ratings Count

# In[190]:


popular_books=df[['title','ratings_count']].sort_values(by='ratings_count',ascending=False).head(10).set_index('title')
sns.barplot(x=popular_books['ratings_count'],y=popular_books.index,data=popular_books)


# # Top 10 Books based on Ratings Count

# In[192]:


popular_books2=df[['title','text_reviews_count']].sort_values(by='text_reviews_count',ascending=False).head(10).set_index('title')
sns.barplot(x=popular_books2['text_reviews_count'],y=popular_books2.index,data=popular_books2)


# We see that the following books feature in both the top 10 list by Ratings count and Text reviews Count:
# Twilight,
# The Catcher in the Rye,
# Harry Potter and the Prisoner of Azkaban

# # Top Books with the Highest Number of Publishers

# In[247]:


#Plotting in a barplot
fig,axes=plt.subplots(figsize=((8,3)))
sns.barplot(x=df['title'].value_counts().index[:10], y=df['title'].value_counts()[:10], ax=axes)
plt.xlabel('Title')
plt.ylabel('Number of Publishers')
plt.title('Top 10 Books by Number of Publishers')
plt.xticks(rotation=90)
plt.show()


# In[249]:


#Checking presence of NA values in the dataset
df.isna().sum()


# # Correlation

# In[254]:


#Correlation Table
df.corr().round(2)


# According to the above correlation table, text_review_count and ratings_count have high positive correlation (87%). This means higher the ratings count, higher is the text ratings count. 

# In[270]:


#Scatter Average Rating vs Ratings Count
plt.scatter(df["average_rating"],df["ratings_count"])
plt.xlabel("average_rating")
plt.ylabel("ratings_count")
plt.title("Average Rating vs Number of Ratings")


# In[271]:


#Scatter Average Rating vs Number of Pages
plt.scatter(df["average_rating"],df["num_pages"])
plt.xlabel("Average_rating")
plt.ylabel("Number of Pages")
plt.title("Average Rating vs Number of Pages")


# In[272]:


#Scatter Average Rating vs Publication Date Delta
plt.scatter(df["average_rating"],df["publication_date"])
plt.xlabel("Average_rating")
plt.ylabel("Date of Publication Delta")
plt.title("Average Rating vs Publication Date")


# In[273]:


#Scatter Average Rating vs Publication Date Delta
plt.scatter(df["average_rating"],df["text_reviews_count"])
plt.xlabel("Average_rating")
plt.ylabel("Number of Text Reviews")
plt.title("Average Rating vs Number of Text Reviews")


# # Detecting Outliers

# In[275]:


#Finding outliers in Number of Pages using boxplot
fig,axes=plt.subplots(figsize=(3,3))
sns.boxplot(df['num_pages'], ax=axes)
plt.title("Number of Pages - Boxplot")


# In[276]:


#Finding outliers from Ratings Count using boxplot
fig,axes=plt.subplots(figsize=(3,3))
sns.boxplot(df['ratings_count'], ax=axes)
plt.title("Number of Ratings - Boxplot")


# In[277]:


#Finding outliers from text reviews count using boxplot
fig,axes=plt.subplots(figsize=(5,5))
sns.boxplot(df['text_reviews_count'], ax=axes)
plt.title("Number of Text Reviews - Boxplot")


# In[ ]:




