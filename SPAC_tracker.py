#!/usr/bin/env python
# coding: utf-8

# In[116]:


#import all relevant libraries

import pandas as pd
import warnings
import numpy as np
from scipy.stats import chi2_contingency
import statsmodels.formula.api as smf

import seaborn as sb
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

warnings.simplefilter(action='ignore', category=FutureWarning)

#read in SPAC dataset

df = pd.read_csv(r'C:\Users\Christopher\Desktop\SPACLIST.csv', encoding='latin1', index_col=0)

print(df.columns)

df.info()

df.describe()


# In[117]:


#create a contingency table w/ frequencies of relevant categories

contingency1 = pd.crosstab(df['Status'], df['Target_Focus'])

#contingency percentages

contigency_pct = pd.crosstab(df['Status'], df['Target_Focus'], normalize='all')
contigency_pct


# In[118]:


#create heatmap of contingency table

plt.figure(figsize=(12,8)) 
sns.heatmap(contingency1, annot=True, cmap="YlGnBu")


# In[120]:


#Since heatmap indicates abundance of other, remove from analysis

df2 = df.loc[df['Target_Focus'] != 'NoFocus']

#df2.describe()


# In[121]:


#create a contingency table w/ frequencies of relevant categories (minus NoFocus)

contingency2 = pd.crosstab(df2['Status'], df2['Target_Focus'])

#contingency percentages

contingency_pct2 = pd.crosstab(df2['Status'], df2['Target_Focus'], normalize='all')
contingency2


# In[122]:


#create heatmap of contingency table

plt.figure(figsize=(12,8)) 
sns.heatmap(contingency2, annot=True, cmap="YlGnBu")


# In[123]:


# Chi-square test of independence. 
c, p, dof, expected = chi2_contingency(contingency2) 
#print p value
print(p)


# In[124]:


#create a contingency table w/ frequencies of relevant categories

contingency3 = pd.crosstab(df['Status'], df['Lead_UW'])

contingency3


# In[125]:


#create heatmap of contingency table

plt.figure(figsize=(12,8)) 
sns.heatmap(contingency3, annot=True, cmap="YlGnBu")


# In[126]:


# Chi-square test of independence. 
c, p, dof, expected = chi2_contingency(contingency3) 
#print p value
print(p)


# In[127]:


#create a contingency table w/ frequencies of relevant categories

contingency4 = pd.crosstab(df['Status'], df['Filer'])

contingency4


# In[128]:


#create heatmap of contingency table

plt.figure(figsize=(12,8)) 
sns.heatmap(contingency4, annot=True, cmap="YlGnBu")


# In[129]:


# Chi-square test of independence. 
c, p, dof, expected = chi2_contingency(contingency4) 
#print p value
print(p)


# In[130]:


pearsoncorr = df.corr(method='pearson')
pearsoncorr


# In[131]:


sb.heatmap(pearsoncorr, 
            xticklabels=pearsoncorr.columns,
            yticklabels=pearsoncorr.columns,
            cmap='RdBu_r',
            annot=True,
            linewidth=0.5)


# In[ ]:




