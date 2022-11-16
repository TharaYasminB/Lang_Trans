import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import jwt
from flask import request

def main(params):
    
  try:

    
    token = request.headers.authentication
    
    decoded = jwt.decode(token, key='test')

    url = 'https://api.us-east.language-translator.watson.cloud.ibm.com/instances/fd50348b-6ac7-45ad-a5cc-b6319059f1d4'
    apikey = 'YXDPsbBDXb_TpsgIffjyrE9GEjgYRe-kpjOXbkNl2juf'
    print(args)

    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
    )

    language_translator.set_service_url(url)

    result = language_translator.identify(params.payload.input.text).get_result()


    language = result["languages"][0]["language"]
    #print(language)
    
    params.payload.context.skills["main skill"].user_defined["language"] = language 
    params.payload.input.text = params.payload.input.text + "(in " + language + ")"

    return params.payload
    
  except:
      return params.payload
