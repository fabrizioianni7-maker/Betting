
import os, json, pandas as pd, pathlib

def ensure_dir(path:str):
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)

def read_table(path:str)->pd.DataFrame:
    return pd.read_parquet(path) if path.endswith(('.parquet','.pq')) else pd.read_csv(path)

def write_table(df, path:str):
    ensure_dir(os.path.dirname(path))
    (df.to_parquet(path, index=False) if path.endswith(('.parquet','.pq')) else df.to_csv(path, index=False))

def save_json(obj, path:str):
    ensure_dir(os.path.dirname(path)); open(path,'w',encoding='utf-8').write(json.dumps(obj,indent=2,ensure_ascii=False))
