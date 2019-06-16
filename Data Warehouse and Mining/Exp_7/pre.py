import pandas as pd
df=pd.read_csv("wh.csv")
print("Initial height-weight dataset")
print(df,"\n")
print("Dataframe after dropping missing values is:")
print(df.dropna())
print("Mean values of each column:")
print(df.mean())
print("Median values of each column:")
print(df.median())
print("Dataset after filling missing values with mean values:")
print(df.fillna(df.mean()))
print("Dataset after filling missing values with median values:")
print(df.fillna(df.median()))
print("Using median filled dataset")
df=df.fillna(df.median())
lh=df["Height"].mean()-2*df["Height"].std()
mh=df["Height"].mean()+2*df["Height"].std()
lw=df["Weight"].mean()-2*df["Weight"].std()
mw=df["Weight"].mean()+2*df["Weight"].std()
print("The outliers (data points less than mean-2*sd and greater than mean+2*sd) are:")
print(df[((df["Height"]<lh)|(df["Height"]>mh))|((df["Weight"]<lw)|(df["Weight"]>mw))])
print("Corrected dataset is:")
print(df[((df["Height"]>=lh)&(df["Height"]<=mh))&((df["Weight"]>=lw)&(df["Weight"]<=mw))])
"""
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/DWM/AQID_DWM/Exp_7$ python3 pre.py
Initial height-weight dataset
       Height      Weight
0   73.847017  141.893563
1   74.110105         NaN
2   71.730978  220.042470
3         NaN  206.349801
4   68.348516         NaN
5   63.456494  156.399676
6   71.195382         NaN
7         NaN  189.446181
8   29.243732  186.434168
9         NaN  172.883470
10        NaN  185.983958
11  75.205974         NaN
12        NaN  192.343977
13  72.800844  506.828189
14  27.421242         NaN 

Dataframe after dropping missing values is:
       Height      Weight
0   73.847017  141.893563
2   71.730978  220.042470
5   63.456494  156.399676
8   29.243732  186.434168
13  72.800844  506.828189
Mean values of each column:
Height     62.736028
Weight    215.860545
dtype: float64
Median values of each column:
Height     71.463180
Weight    187.940175
dtype: float64
Dataset after filling missing values with mean values:
       Height      Weight
0   73.847017  141.893563
1   74.110105  215.860545
2   71.730978  220.042470
3   62.736028  206.349801
4   68.348516  215.860545
5   63.456494  156.399676
6   71.195382  215.860545
7   62.736028  189.446181
8   29.243732  186.434168
9   62.736028  172.883470
10  62.736028  185.983958
11  75.205974  215.860545
12  62.736028  192.343977
13  72.800844  506.828189
14  27.421242  215.860545
Dataset after filling missing values with median values:
       Height      Weight
0   73.847017  141.893563
1   74.110105  187.940175
2   71.730978  220.042470
3   71.463180  206.349801
4   68.348516  187.940175
5   63.456494  156.399676
6   71.195382  187.940175
7   71.463180  189.446181
8   29.243732  186.434168
9   71.463180  172.883470
10  71.463180  185.983958
11  75.205974  187.940175
12  71.463180  192.343977
13  72.800844  506.828189
14  27.421242  187.940175
Using median filled dataset
The outliers (data points less than mean-2*sd and greater than mean+2*sd) are:
       Height      Weight
8   29.243732  186.434168
13  72.800844  506.828189
14  27.421242  187.940175
Corrected dataset is:
       Height      Weight
0   73.847017  141.893563
1   74.110105  187.940175
2   71.730978  220.042470
3   71.463180  206.349801
4   68.348516  187.940175
5   63.456494  156.399676
6   71.195382  187.940175
7   71.463180  189.446181
9   71.463180  172.883470
10  71.463180  185.983958
11  75.205974  187.940175
12  71.463180  192.343977

"""








