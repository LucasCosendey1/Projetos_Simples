import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Carregar os dados (supondo que você tenha um arquivo CSV)
data = pd.read_csv("sentimentos.csv")

# Separar as features (texto) e o target (sentimento)
X = data['texto']
y = data['sentimento']

# Criar um vetorizador de contagem
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

# Dividir os dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Criar e treinar o modelo Naive Bayes
model = MultinomialNB()
model.fit(X_train, y_train)

# Fazer previsões
y_pred = model.predict(X_test)

# Avaliar o modelo
accuracy = accuracy_score(y_test, y_pred)
print("Acurácia:", accuracy)