
import argparse, pandas as pd, os
from src.common.io import read_table
from src.models.train import train_classifier

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--data', default='data/processed/dataset_with_odds.csv')
    ap.add_argument('--target', required=True)
    ap.add_argument('--sport', required=True, choices=['calcio','tennis'])
    ap.add_argument('--out', default='reports/experiment_1')
    args=ap.parse_args()
    df=read_table(args.data)
    drop_cols=[c for c in ['match_id','date','league','season','home_team','away_team','tournament','player1','player2'] if c in df.columns]
    df=df.drop(columns=drop_cols, errors='ignore')
    train_classifier(df, args.target, args.out)

if __name__=='__main__': main()
