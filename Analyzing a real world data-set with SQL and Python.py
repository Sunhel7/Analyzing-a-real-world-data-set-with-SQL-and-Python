#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install ipython-sql')
get_ipython().system('pip install seaborn')
import seaborn as sns
get_ipython().run_line_magic('load_ext', 'sql')


# In[2]:


import csv, sqlite3

con = sqlite3.connect("socioeconomic.db")
cur = con.cursor()
get_ipython().system('pip install pandas')


# In[3]:


get_ipython().run_line_magic('sql', 'sqlite:///socioeconomic.db')


# # Store the dataset in a Table

# In[4]:


import pandas
df = pandas.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')
df.to_sql("chicago_socioeconomic_data", con, if_exists='replace', index=False,method="multi")


# In[6]:


get_ipython().system('pip install ipython-sql prettytable')
import prettytable

prettytable.DEFAULT = 'DEFAULT'


# # Problems
# 
# How many rows are in the dataset?

# In[7]:


get_ipython().run_line_magic('sql', 'SELECT COUNT(*) FROM chicago_socioeconomic_data;')


# How many community areas in Chicago have a hardship index greater than 50.0

# In[8]:


get_ipython().run_line_magic('sql', 'SELECT COUNT(*) FROM chicago_socioeconomic_data WHERE hardship_index > 50.0;')


# What is the maximum value of hardship index in this dataset?

# In[9]:


get_ipython().run_line_magic('sql', 'SELECT MAX(hardship_index) FROM chicago_socioeconomic_data;')


# Which community area which has the highest hardship index?

# In[11]:


get_ipython().run_line_magic('sql', 'SELECT community_area_name FROM chicago_socioeconomic_data ORDER BY hardship_index DESC LIMIT 1;')


# Which Chicago community areas have per-capita incomes greater than $60,000?

# In[12]:


get_ipython().run_line_magic('sql', 'SELECT community_area_name FROM chicago_socioeconomic_data WHERE per_capita_income_ > 60000;')


# Create a scatter plot using the variables per_capita_income_ and hardship_index. Explain the correlation between the two variables.

# In[13]:


get_ipython().system('pip install matplotlib seaborn')
income_vs_hardship = get_ipython().run_line_magic('sql', 'SELECT per_capita_income_, hardship_index FROM chicago_socioeconomic_data;')
plot = sns.jointplot(x='per_capita_income_',y='hardship_index', data=income_vs_hardship.DataFrame())


# In[ ]:




