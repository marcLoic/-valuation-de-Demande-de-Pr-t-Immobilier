import logging
logging.basicConfig(level=logging.DEBUG)
import sys
from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.util.wsgi_wrapper import run_twisted
import spacy

from services.solvency_verification_service import SolvencyVerificationService

# Charger le modèle SpaCy pour le français
nlp = spacy.load("fr_core_news_sm")

# Créer l'application Spyne
application = Application([SolvencyVerificationService],
    tns='http://localhost/SolvencyVerificationService',
    in_protocol=Soap11(validator=''),
    out_protocol=Soap11()
)

if __name__ == '__main__':
    # Créer l'application WSGI
    wsgi_app = WsgiApplication(application)
    
    # Lancer le serveur
    twisted_apps = [
        (wsgi_app, b'SolvencyVerificationService'),
    ]

    sys.exit(run_twisted(twisted_apps, 8001))