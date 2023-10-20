import logging
logging.basicConfig(level=logging.DEBUG)
import sys
from spyne import rpc, ServiceBase, Unicode


class SolvencyVerificationService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def verify_solvency(ctx, extracted_info):
        
        response = "Solvabilité vérifiée avec succès."
        return response
    
    @rpc(Unicode, _returns=Unicode)
    def bureau_credit(ctx, user):

        response = ""
        return response
    
    @rpc(Unicode, _returns=Unicode)
    def algorithme_scoring(ctx, user):

        response = ""
        return response
    
    @rpc(Unicode, _returns=Unicode)
    def analyse_revenus_depenses(ctx, user):

        response = ""
        return response