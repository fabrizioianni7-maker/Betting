
import argparse
from src.common.io import read_table, write_table
from src.odds.align import align_odds

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--matches', default='data/processed/dataset.csv')
    ap.add_argument('--odds', default='data/external/odds/odds.csv')
    ap.add_argument('--out', default='data/processed/dataset_with_odds.csv')
    args=ap.parse_args()
    out=align_odds(read_table(args.matches), read_table(args.odds))
    write_table(out, args.out); print(f'Wrote {args.out} ({len(out)})')

if __name__=='__main__': main()
