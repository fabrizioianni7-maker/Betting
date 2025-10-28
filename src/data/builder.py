
import pandas as pd
from src.common.utils import stamp

def unify_calcio(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty: return df
    if 'result_1x2' not in df.columns and {'home_goals','away_goals'}<=set(df.columns):
        df['result_1x2']=df.apply(lambda r: 'H' if r.home_goals>r.away_goals else ('A' if r.away_goals>r.home_goals else 'D'), axis=1)
    if 'btts' not in df.columns and {'home_goals','away_goals'}<=set(df.columns):
        df['btts']=((df.home_goals>0)&(df.away_goals>0)).astype(int)
    if 'ou_2_5' not in df.columns and {'home_goals','away_goals'}<=set(df.columns):
        df['ou_2_5']=((df.home_goals+df.away_goals)>2).map({True:'over',False:'under'})
    return df

def unify_tennis(df: pd.DataFrame) -> pd.DataFrame:
    return df

def run(df: pd.DataFrame, sport: str) -> pd.DataFrame:
    stamp(f'Unify dataset: {sport} — {len(df)} rows')
    return unify_calcio(df) if sport=='calcio' else unify_tennis(df)
