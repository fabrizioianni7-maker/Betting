
import argparse, pandas as pd, joblib
from src.common.io import read_table

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--data', default='data/processed/dataset_with_odds.csv')
    ap.add_argument('--model', default='reports/experiment_1/model.joblib')
    ap.add_argument('--target', required=True)
    args=ap.parse_args()
    df=read_table(args.data); y=df[args.target]; X=df.drop(columns=[args.target])
    pipe=joblib.load(args.model); preds=pipe.predict(X); acc=(preds==y).mean(); print(f'Quick in-sample accuracy: {acc:.3f}')

if __name__=='__main__': main()
