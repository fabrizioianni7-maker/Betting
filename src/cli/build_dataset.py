
import argparse, pandas as pd
from src.data.loader import load_folder
from src.data.builder import run as unify
from src.common.io import write_table

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--sport', required=True, choices=['calcio','tennis'])
    ap.add_argument('--raw_dir', default='data/raw')
    ap.add_argument('--out', default='data/processed/dataset.csv')
    args=ap.parse_args()
    df=load_folder(args.raw_dir); df=unify(df, args.sport); write_table(df, args.out); print(f'Wrote {args.out} ({len(df)})')

if __name__=='__main__': main()
