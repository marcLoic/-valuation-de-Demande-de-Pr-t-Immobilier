import logging
logging.basicConfig(level=logging.DEBUG)
import sys
from spyne import Application, rpc, ServiceBase, Unicode, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.util.wsgi_wrapper import run_twisted

from services.property_evaluation_service import PropertyEvaluationService
from services.solvency_verification_service import SolvencyVerificationService
from services.info_extraction_service import InfoExtractionService
from services.loan_approval_decision_service import LoanApprovalDecisionService


application = Application([InfoExtractionService, SolvencyVerificationService, PropertyEvaluationService, LoanApprovalDecisionService],
    tns='http://localhost/evaluationpretimmobilier',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

if __name__ == '__main__':
    wsgi_app = WsgiApplication(application)
    
    twisted_apps = [(wsgi_app, b'evaluationpretimmobilier')]
    sys.exit(run_twisted(twisted_apps, 8001))
