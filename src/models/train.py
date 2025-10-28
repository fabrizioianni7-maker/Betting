
import os, json, pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, log_loss
from xgboost import XGBClassifier
from src.common.utils import stamp

def train_classifier(df: pd.DataFrame, target: str, out_dir: str):
    stamp(f'Train target={target}, rows={len(df)}')
    y=df[target]; X=df.drop(columns=[target])
    numeric=X.select_dtypes(include='number').columns.tolist()
    categorical=[c for c in X.columns if c not in numeric]
    pre=ColumnTransformer([('cat',OneHotEncoder(handle_unknown='ignore'),categorical),('num','passthrough',numeric)])
    model=XGBClassifier(n_estimators=300,max_depth=6,learning_rate=0.05,subsample=0.9,colsample_bytree=0.9,
                        objective='multi:softprob' if y.nunique()>2 else 'binary:logistic',
                        eval_metric='mlogloss' if y.nunique()>2 else 'logloss')
    pipe=Pipeline([('pre',pre),('model',model)])
    Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=0.2,shuffle=True,stratify=y if y.nunique()>1 else None)
    pipe.fit(Xtr,ytr); preds=pipe.predict(Xte); proba=pipe.predict_proba(Xte)
    acc=accuracy_score(yte,preds); ll=log_loss(yte,proba)
    os.makedirs(out_dir, exist_ok=True)
    json.dump({"accuracy":acc,"log_loss":ll}, open(os.path.join(out_dir,'metrics.json'),'w'), indent=2)
    import joblib; joblib.dump(pipe, os.path.join(out_dir,'model.joblib'))
    stamp(f'Accuracy={acc:.3f} LogLoss={ll:.3f} -> {out_dir}')
