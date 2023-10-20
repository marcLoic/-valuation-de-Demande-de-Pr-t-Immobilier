import requests

# URL du service Web Composite
url = 'http://adresse_du_serveur:8000/evaluationpretimmobilier'

# Enveloppe SOAP pour l'extraction d'informations
extraction_request_envelope = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="evaluationpretimmobilier">
   <soapenv:Header/>
   <soapenv:Body>
      <web:extract_info>
         <!--Optional:-->
         <web:request_text>Texte de la demande de prêt</web:request_text>
      </web:extract_info>
   </soapenv:Body>
</soapenv:Envelope>
'''

# Enveloppe SOAP pour la vérification de solvabilité
solvency_request_envelope = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="evaluationpretimmobilier">
   <soapenv:Header/>
   <soapenv:Body>
      <web:verify_solvency>
         <!--Optional:-->
         <web:extracted_info>Informations extraites</web:extracted_info>
      </web:verify_solvency>
   </soapenv:Body>
</soapenv:Envelope>
'''

# Enveloppe SOAP pour l'évaluation de la propriété
property_evaluation_request_envelope = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="evaluationpretimmobilier">
   <soapenv:Header/>
   <soapenv:Body>
      <web:evaluate_property>
         <!--Optional:-->
         <web:extracted_info>Informations extraites</web:extracted_info>
      </web:evaluate_property>
   </soapenv:Body>
</soapenv:Envelope>
'''

# Enveloppe SOAP pour la décision d'approbation
approval_decision_request_envelope = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="evaluationpretimmobilier">
   <soapenv:Header/>
   <soapenv:Body>
      <web:make_approval_decision>
         <!--Optional:-->
         <web:solvency_result>Résultat de la solvabilité</web:solvency_result>
         <!--Optional:-->
         <web:property_evaluation_result>Résultat de l'évaluation de la propriété</web:property_evaluation_result>
      </web:make_approval_decision>
   </soapenv:Body>
</soapenv:Envelope>
'''

# Envoi de la demande d'extraction d'informations au service Web Composite
response = requests.post(url, data=extraction_request_envelope, headers={'content-type': 'text/xml'})
print("Réponse de l'extraction d'informations:", response.text)

# Envoi de la demande de vérification de solvabilité au service Web Composite
response = requests.post(url, data=solvency_request_envelope, headers={'content-type': 'text/xml'})
print("Réponse de la vérification de solvabilité:", response.text)

# Envoi de la demande d'évaluation de la propriété au service Web Composite
response = requests.post(url, data=property_evaluation_request_envelope, headers={'content-type': 'text/xml'})
print("Réponse de l'évaluation de la propriété:", response.text)

# Envoi de la demande de décision d'approbation au service Web Composite
response = requests.post(url, data=approval_decision_request_envelope, headers={'content-type': 'text/xml'})
print("Réponse de la décision d'approbation:", response.text)
