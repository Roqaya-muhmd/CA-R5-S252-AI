import pandas as pd


def Read_data_file(file_path:str) :
    try:
      df = pd.read_csv(file_path)
      return df
    except ValueError:
        print("Error occurred while reading the data file.")
        return pd.DataFrame({})
    except FileNotFoundError:
        print("File not found.")
        return pd.DataFrame({})
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return pd.DataFrame({})


def Drop_unnecessary_features(df, cols_to_drop):
    return df.drop(columns=cols_to_drop)



# Drop_unnecessary_features(df, cols_to_drop)
# • Column name  
# • Datatype 
# • Number of unique values
def check_data_type(df):
    data = []
    for col in df.columns:
        data.append({
            "Column": col,
            "Datatype": df[col].dtype,
            "Number of unique values": df[col].nunique()
        })
    return pd.DataFrame(data)