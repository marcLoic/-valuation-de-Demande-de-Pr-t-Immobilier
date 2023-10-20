import logging
logging.basicConfig(level=logging.DEBUG)
import sys
from spyne import rpc, ServiceBase, Unicode


class SolvencyVerificationService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def verify_solvency(ctx, extracted_info):
        
        extracted_info = extracted_info

        result_bureau_credit = SolvencyVerificationService.bureau_credit(extracted_info.name)
        if (result_bureau_credit):
            return result_bureau_credit
        else:
            response = "Pas solvable"
            return response
    
    def bureau_credit(ctx, user):
        return True
    
    def algorithme_scoring(ctx, user):

        response = ""
        return response
    
    def analyse_revenus_depenses(ctx, user):

        response = ""
        return response