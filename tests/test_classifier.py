from src.classifier import TicketClassifier

def test_classifier_predicts_known_categories():
    texts=['charged twice','application crashes','cannot login','please add feature']
    labels=['billing','bug','access','feature']
    model=TicketClassifier().fit(texts,labels)
    pred=model.predict(['cannot login'])
    assert pred[0]=='access'
