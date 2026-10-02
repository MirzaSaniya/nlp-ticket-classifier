from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

class TicketClassifier:
    def __init__(self):
        self.vectorizer=TfidfVectorizer(ngram_range=(1,2),lowercase=True)
        self.model=LogisticRegression(max_iter=1000)
    def fit(self,texts,labels):
        X=self.vectorizer.fit_transform(texts); self.model.fit(X,labels); return self
    def predict(self,texts):
        return self.model.predict(self.vectorizer.transform(texts))
    def predict_with_confidence(self,texts):
        X=self.vectorizer.transform(texts); probs=self.model.predict_proba(X)
        preds=self.model.classes_[probs.argmax(axis=1)]
        conf=probs.max(axis=1)
        return list(zip(preds,conf))
