# src/data_cleaning.py
import pandas as pd
import numpy as np
import os
import glob

def load_data(csv_path):
    return pd.read_csv(csv_path, encoding='latin1')

def convert_size_to_mb(size_val):
    if pd.isna(size_val):
        return np.nan
    s = str(size_val).strip()
    if s == 'Varies with device':
        return np.nan
    try:
        if s.endswith('M'):
            return float(s[:-1])
        if s.endswith(('k', 'K')):
            return float(s[:-1]) / 1024
        if s.endswith('G'):
            return float(s[:-1]) * 1024
        return float(s)
    except:
        return np.nan

def clean_dataframe(df):
    df = df.copy()
    df.columns = [c.strip() for c in df.columns]

    df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')

    df['Installs'] = df['Installs'].astype(str).str.replace('[+,]', '', regex=True)
    df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')

    df['Price'] = df['Price'].astype(str).str.replace('[$]', '', regex=True)
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

    df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

    df['Size_MB'] = df['Size'].apply(convert_size_to_mb)

    df['Last Updated'] = pd.to_datetime(df['Last Updated'], errors='coerce')

    df['Current Ver'] = df['Current Ver'].astype(str).str.strip()
    df['Android Ver'] = df['Android Ver'].astype(str).str.strip()

    if 'App' in df.columns:
        df = df.drop_duplicates(subset=['App'], keep='first').reset_index(drop=True)

    return df

def main():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    data_dir = os.path.join(project_root, 'data')

    # find any CSV in data folder
    csv_files = glob.glob(os.path.join(data_dir, "*.csv"))

    if not csv_files:
        raise FileNotFoundError(f"No CSV file found in {data_dir}. Please place your dataset there.")

    raw = csv_files[0]  # take the first CSV found
    out = os.path.join(data_dir, 'googleplaystore_clean.csv')

    print(f"Loading dataset from: {raw}")
    df = load_data(raw)

    df_clean = clean_dataframe(df)
    df_clean.to_csv(out, index=False)

    print(f"✅ Cleaned dataset saved to: {out}")
    print(df_clean.info())

if __name__ == "__main__":
    main()
