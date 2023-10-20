import logging
logging.basicConfig(level=logging.DEBUG)
import sys
from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.util.wsgi_wrapper import run_twisted
import spacy

# Charger le modèle SpaCy pour le français
nlp = spacy.load("fr_core_news_sm")

class ExtractService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def extract_data(ctx, text):
        # Processus d'analyse du texte
        doc = nlp(text)

        # Définir les catégories d'informations à extraire
        categories = [
            "nom du client", 
            "adresse", 
            "email", 
            "numero de telephone",
            "montant du pret",
            "duree du pret",
            "description de la propriete",
            "revenu mensuel",
            "depenses mensuelles"
        ]

        # Initialiser un dictionnaire pour stocker les informations extraites
        extracted_info = {category: "" for category in categories}

        # Parcourir les entités nommées pour extraire les informations
        for ent in doc.ents:
            for category in categories:
                if category.lower() in ent.text.lower():
                    extracted_info[category] = ent.text

        # Convertir les informations en une chaîne de texte formatée
        result = "\n".join([f"{category}: {value}" for category, value in extracted_info.items()])

        return result

    

# Créer l'application Spyne
application = Application([ExtractService],
    tns='http://localhost/ExtractService',
    in_protocol=Soap11(validator=''),
    out_protocol=Soap11()
)

if __name__ == '__main__':
    # Créer l'application WSGI
    wsgi_app = WsgiApplication(application)
    
    # Lancer le serveur
    twisted_apps = [
        (wsgi_app, b'ExtractService'),
    ]

    sys.exit(run_twisted(twisted_apps, 8000))