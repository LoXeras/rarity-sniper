import json
URL = "https://ikzttp.mypinata.cloud/ipfs/QmeBWSnYPEnUimvpPfNHuvgcK9wFH9Sa6cZ4KDfgkfJJis/"

def getMetadata(baseURI, max):
   import requests   
   data = []
   for x  in range(max):
      r = requests.get(baseURI+str(x))
      data.append(json.loads(r.text))
   return data

def getAttributes(data):
   attributes = []
   for x in range(len(data)):
      #spec_attr = (data[x]['attributes']).keys()
      for attr in range(len(data[x]['attributes'])):
         if not ((data[x]['attributes'][attr]['trait_type']) in attributes):
           attributes.append(data[x]['attributes'][attr]['trait_type'])
   
   return attributes

def getAttributeValues(data, attributes):
   values = []
   for attr in range(len(attributes)):
      for x in range(len(data)):      
         for count in range(len(data[x]['attributes'])):
            if ((data[x]['attributes'][count]['trait_type']) == attributes[attr]):
               if not ((data[x]['attributes'][count]['value']) in values):
                  values.append(data[x]['attributes'][count]['value'])
   return values



import timeit
start = timeit.default_timer()

all_data = []
all_data = getMetadata(URL, 50) 
#for x in range(100):
  #data = getMetadata(URL, 10) 
  #all_data.append(data)
  
attributes = getAttributes(all_data)
print(getAttributeValues(all_data, ["Hair"]))


stop = timeit.default_timer()
print('Time: ', stop - start, " seconds")  

