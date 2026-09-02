from config.config import cols_to_drop 
from preprocessing import Drop_unnecessary_features, Read_data_file, check_data_type
cols=cols_to_drop
df=Read_data_file("data/Titanic.csv")
# 2. Check summary before dropping
print(check_data_type(df))

# 3. Drop features
cols = cols_to_drop
df = Drop_unnecessary_features(df, cols)

# 4. Check summary after dropping
print(check_data_type(df))