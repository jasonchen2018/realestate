#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.plotting import figure, output_file, show
from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource
output_notebook()
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings 
warnings.filterwarnings("ignore") #ignore warnings from python 'warning' library


# In[11]:


def graph_function(data_frame):
    #Useful imports

    h=list(data_frame)
    print (h)
    len(h)
    feature_list = []
    print("\nIf done with selecting features, enter NA\n")
    for i in h:
        selected = input("Choose the feature you want : ")
        if selected == 'NA':
            break
        else:
            feature_list.append(selected);

    print (feature_list)
    title = input("\nEnter a title for the graphs : ")
    for i, j in enumerate(feature_list):
        fig=plt.subplots(figsize=(15,20))
        plt.subplot(4, 2, i+1)
        plt.subplots_adjust(hspace = 1.0)
        sns.countplot(x=j,data = data_frame)
        plt.title(title)


# In[ ]:





# In[ ]:




