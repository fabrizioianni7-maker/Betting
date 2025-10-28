
import os, glob, pandas as pd
from src.common.io import read_table
from src.common.utils import stamp

def load_folder(folder:str)->pd.DataFrame:
    files = sorted(glob.glob(os.path.join(folder,'*.*')))
    frames=[]
    for f in files:
        try: frames.append(read_table(f))
        except Exception as e: stamp(f"Skip {f}: {e}")
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()
