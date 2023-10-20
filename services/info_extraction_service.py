import logging
logging.basicConfig(level=logging.DEBUG)
import sys
from spyne import rpc, ServiceBase, Unicode


class InfoExtractionService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def extract_info(ctx, request_text):
        
        response = "Informations extraites avec succès."
        return response
    