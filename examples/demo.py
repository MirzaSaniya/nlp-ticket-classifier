from src.classifier import TicketClassifier

texts=[
    'I was charged twice for my subscription',
    'The application crashes when I export a report',
    'I cannot log into my account',
    'Please add dark mode to the dashboard',
    'My invoice amount is incorrect',
    'Exporting the report causes an error',
    'Password reset link does not work',
    'Can you add a CSV export option?',
]
labels=['billing','bug','access','feature','billing','bug','access','feature']
model=TicketClassifier().fit(texts,labels)
queries=['The login page rejects my password','The app fails during export','Please add an API integration']
for q,(p,c) in zip(queries,model.predict_with_confidence(queries)):
    print(f'{q} -> {p} ({c:.2f})')
