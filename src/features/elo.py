
import pandas as pd
def simple_elo(df: pd.DataFrame, K=20, base=1500):
    if df.empty: return df
    elo={}
    def get(t): return elo.get(t, base)
    rows=[]
    for _,r in df.sort_values('date').iterrows():
        h,a=r.home_team,r.away_team; eh,ea=get(h),get(a)
        exp_h=1/(1+10**((ea-eh)/400))
        s_h=1 if r.home_goals>r.away_goals else (0 if r.home_goals<r.away_goals else .5)
        eh2=eh+K*(s_h-exp_h); ea2=ea+K*((1-s_h)-(1-exp_h)); elo[h],elo[a]=eh2,ea2
        rows.append((eh,ea,eh2,ea2))
    df[['home_elo_pre','away_elo_pre','home_elo_post','away_elo_post']]=pd.DataFrame(rows,index=df.index)
    return df
