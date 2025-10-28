
import pandas as pd
from src.common.utils import stamp

def rolling_form(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty: return df
    df=df.sort_values('date').copy()
    for side, gf, ga, team in [('home','home_goals','away_goals','home_team'),('away','away_goals','home_goals','away_team')]:
        for k in [3,5,10]:
            df[f'{side}_form_gd_{k}']=(df.groupby(team)[gf].rolling(k).mean().reset_index(level=0,drop=True)-
                                       df.groupby(team)[ga].rolling(k).mean().reset_index(level=0,drop=True))
    stamp('Form features added')
    return df
