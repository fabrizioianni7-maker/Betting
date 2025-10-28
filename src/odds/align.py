
import pandas as pd
def align_odds(matches: pd.DataFrame, odds: pd.DataFrame, on=['date','home_team','away_team']) -> pd.DataFrame:
    return matches if matches.empty or odds.empty else matches.merge(odds,on=on,how='left',suffixes=('','_odds'))
