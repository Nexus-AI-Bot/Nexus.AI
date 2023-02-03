funfactapi = "https://useless-facts.sameerkumar.website/api"
import requests
import json
def funfact():
  api = requests.get(funfactapi)
  funfactgetdict = json.loads(api.content)
  return(funfactgetdict["data"])
