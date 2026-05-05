from sklearn.ensemble import IsolationForest
import numpy as np

model = IsolationForest(contamination=0.2)

def detect_anomalies(skill_counts):
    values = np.array(list(skill_counts.values())).reshape(-1, 1)

    if len(values) < 5:
        return {}
    
    preds = model.fit_predict(values)

    result = {}
    for i, (skill, count) in enumerate(skill_counts.items()):
        result[skill] = {
            "count" : count,
            "anomaly": True if preds[i] == -1 else False
        }

    return result