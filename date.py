#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np


# In[7]:


#creating data range
date_range=pd.date_range(start='2024-01-01',end='4-10-2024',freq='D')
print(date_range)


# In[27]:


#assigning random data for each date in the range
data = np.random.randint(10,100,size=(len(date_range)))


# In[17]:


#creating a time series using pandas series
time_series = pd.Series(data=data, index=date_range)
print(time_series)


# In[20]:


#get the current date
current_date=pd.Timestamp.now()

#display
print("current date is: ",current_date.date())


# In[26]:


# Define two dates
date1 = pd.Timestamp('2024-10-04  10:30:00')
date2 = pd.Timestamp('2025-01-11  12:05:00')

# Calculate the difference
difference = date2 - date1

# Display the difference
print("Difference between dates:", difference)
print("Difference in days:", difference.days)
print("Difference in hours, minutes, seconds:", difference.components)


# In[30]:


# Sample data
data = {
    'timestamp': ['2024-10-04 14:35:20', '2024-12-25 09:15:10', '2023-01-01 23:59:59']
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert the 'timestamp' column to datetime format
df['timestamp'] = pd.to_datetime(df['timestamp'])

print(df)


# In[42]:


# Extract year
df['year'] = df['timestamp'].dt.year

# Extract month
df['month'] = df['timestamp'].dt.month

# Extract day of the month
df['day'] = df['timestamp'].dt.day

# Extract hour
df['hour'] = df['timestamp'].dt.hour

# Extract minute
df['minute'] = df['timestamp'].dt.minute

# Extract second
df['second'] = df['timestamp'].dt.second

# Extract day of the week (0 = Monday, 6 = Sunday)
df['day_of_week'] = df['timestamp'].dt.dayofweek

# Extract whether it's the weekend (1 = Weekend, 0 = Weekday)
df['is_weekend'] = df['day_of_week'].apply(lambda x: 1 if x >= 5 else 0)

# Display the updated DataFrame
print(df)


# ### window function

# In[45]:


# Assume a time series of sales data
data = [100,20,150,300,400,250]

# Creating a sliding window with a size of 3
window_size=3
windows=[data[i:i + window_size]for i in range(len(data)-window_size+1)]
print(windows)


# In[ ]:


df=pd.DataFrame(data)
df['rolling_mean']=df['value'].rolling(window=3).mean()
print(df)


# In[ ]:





# In[ ]:




