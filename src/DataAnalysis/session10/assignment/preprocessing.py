import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'data', 'insurance.csv')
data = pd.read_csv(csv_path)
#Read the data file

#Drob null values
print(data.isnull().sum())

#Drop duplicates
print(data.duplicated().sum())
data.drop_duplicates(inplace=True)
print(data.duplicated().sum())



print(data.info())
print(data.describe())

#checking the data types and number of unique values for each column
nunique=data.nunique()
d_types = data.dtypes
data_types = pd.DataFrame({ 'Data Type': d_types , 'Number of Unique Values': nunique })

#Checking for categorical columns and converting them to category type
categorical_cols = data.columns[data.columns.map(lambda x: data[x].nunique()) < 7]
print(categorical_cols)
data[categorical_cols] = data[categorical_cols].astype('category')
print(data[categorical_cols].dtypes)

#checking for numerical columns
num_cols = data.select_dtypes(include=['int64', 'float64']).columns
##Checking for outliers in numerical columns using boxplots
plt.figure(figsize=(9, 4))
for i, col in enumerate(num_cols):
 plt.subplot(1, 3, i+1)
 sns.boxplot(data[col], orient="h")
 plt.title(f"{col} boxplot")
 plt.xlabel(col)
plt.show()

#Handling outliers using IQR method
for i, col in enumerate(num_cols):
    q1 = data[col].quantile(0.25)
    q3 = data[col].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    print(f"{col}: Lower Bound = {lower_bound}, Upper Bound = {upper_bound}")
    data[col] = np.where(data[col] < lower_bound, lower_bound, data[col])
    data[col] = np.where(data[col] > upper_bound, upper_bound, data[col])
    
    
    
    

#Checking for outliers in numerical columns using boxplots after handling outliers

plt.figure(figsize=(9, 4))
for i, col in enumerate(num_cols):
 plt.subplot(1, 3, i+1)
 sns.boxplot(data[col], orient="h")
 plt.title(f"{col} boxplot")
 plt.xlabel(col)
plt.show()

#distribution of numerical columns using histograms
plt.figure(figsize=(9, 4))
for i, col in enumerate(num_cols):
 plt.subplot(1, 3, i+1)
 plt.hist(data[col], edgecolor="black")
 plt.title(f"{col} Distribution Graph")
plt.show()




#distribution of categorical columns using count plots
cat_cols = data.select_dtypes("category").columns
plt.figure(figsize=(9,4))
for i, col in enumerate(cat_cols):
 plt.subplot(2, 3, i+1)
 unique = data[col].value_counts()
 count = unique.values
 categories = unique.index
 plt.pie(count, labels = categories, startangle=140, autopct='%1.1d%%')
 plt.title(f"{col} Distribution Graph")
 plt.subplots_adjust(hspace =.8, wspace =.3)
plt.show()



# Heatmaps: categorical vs categorical
n_pairs = len([1 for col in cat_cols for i in cat_cols if col < i])
plt.figure(figsize=(15, 6))
pos = 1
for col in cat_cols:
    for i in cat_cols:
        if col < i:
            plt.subplot(2, (n_pairs + 1) // 2, pos)
            agg = data.pivot_table(index=col, columns=i, values="age", aggfunc=len)
            sns.heatmap(agg)
            plt.title(f"{i} vs {col}")
            pos += 1
plt.tight_layout()
plt.show()





# Scatter plots: numerical vs numerical
n_pairs = len([1 for col in num_cols for i in num_cols if col < i])
plt.figure(figsize=(15, 6))
pos = 1
for col in num_cols:
    for i in num_cols:
        if col < i:
            plt.subplot(2, (n_pairs + 1) // 2, pos)
            sns.scatterplot(x=data[col], y=data[i])
            plt.xlabel(col)
            plt.title(f"{i} vs {col}")
            pos += 1
plt.tight_layout()
plt.show()


# Bar plots: numerical vs categorical
n_pairs = len(num_cols) * len(cat_cols)
plt.figure(figsize=(15, 10))
pos = 1
for col in num_cols:
    for i in cat_cols:
        plt.subplot(len(num_cols), len(cat_cols), pos)
        sns.barplot(x=i, y=col, data=data)
        plt.xlabel(i)
        plt.title(f"{col} vs {i}")
        pos += 1
plt.tight_layout()
plt.show()


#Data Splitting
x = data.drop(columns=["charges"])
y = data["charges"]


#normalization using MinMaxScaler
num_cols = [col for col in num_cols if col != 'charges']
scaler = MinMaxScaler()
scaler.fit(x[num_cols])
x[num_cols] = scaler.transform(x[num_cols])



#one-hot encoding for categorical columns
hot_encoding_cols= [col for col in cat_cols if col != 'children']
one_hot_encoder = OneHotEncoder(sparse_output=False, drop='first')
ohe = one_hot_encoder.fit_transform(x[hot_encoding_cols])
ohe_df = pd.DataFrame(ohe, columns=one_hot_encoder.get_feature_names_out(hot_encoding_cols))
x = pd.concat([x.drop(columns=hot_encoding_cols), ohe_df], axis=1)



#binary encoding for 'children' column because 75% of the data has 2 children . So, we can convert it to binary encoding.
x['children'] = x['children'].apply(lambda x: 1 if x > 0 else 0)



#printing the final shape of the data after preprocessing
print(f"Final shape of the data after preprocessing: {x.shape}")

#printing the first 5 rows of the data after preprocessing
print(x.head())