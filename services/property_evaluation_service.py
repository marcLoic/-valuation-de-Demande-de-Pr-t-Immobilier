import logging
logging.basicConfig(level=logging.DEBUG)
import sys
from spyne import rpc, ServiceBase, Unicode

class PropertyEvaluationService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def evaluate_property(ctx, extracted_info):
        
        response = "Évaluation de la propriété effectuée avec succès."
        return response
    
    @rpc(Unicode, _returns=Unicode)
    def analyse_marche_immobilier(ctx, propriete):

        response = ""
        return response
    
    @rpc(Unicode, _returns=Unicode)
    def inspection_propriete(ctx, propriete):

        response = ""
        return response
    
    @rpc(Unicode, _returns=Unicode)
    def conformite_legale_reglementaire(ctx, propriete):

        response = ""
        return response