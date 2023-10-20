from suds.client import Client

# URL du service
url = 'http://localhost:8000/ExtractService?wsdl'

# Création du client
client = Client(url)

# Texte à envoyer pour extraction
text = "Nom du Client: John Doe\nAdresse: 123 Rue de la Liberté, 75001 Paris, France\nEmail: john.doe@email.com\nNuméro de Téléphone: +33 123 456 789\nMontant du Prêt Demandé: 200000 EUR Durée du Prêt: 20 ans\nDescription de la Propriété: Maison à deux étages avec jardin, située dans un quartier résidentiel calme.\nRevenu Mensuel: 5000 EUR\nDépenses Mensuelles: 3000 EUR"

# Appel de la méthode extrat_data
result = client.service.extract_data(text=text)

# Affichage du résultat
print(result)