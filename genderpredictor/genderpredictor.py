import joblib
import os

class GenderPrediction:
    def __init__(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(base_path, 'model.pkl')
        vectorizer_path = os.path.join(base_path, 'vectorizer.pkl')
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)
        self.labels = {1: "Laki-Laki", 0: "Perempuan"}

    def __call__(self, name: str):
        vector = self.vectorizer.transform([name])
        result = self.model.predict(vector)[0]
        proba = self.model.predict_proba(vector).max()
        return self.labels[result], round(proba * 100, 2)
