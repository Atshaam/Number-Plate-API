from fastapi import FastAPI
import random
import string
import re 
import requests

app = FastAPI()

response_ = requests.get('https://timeapi.io/api/Time/current/zone?timeZone=Europe/Amsterdam')
current_year = int(str(response_.json()['year'])[2:])
current_month = int(response_.json()['month'])     

@app.get("/generate")
def index(type: str):
        if type == 'new':
          product = f"{random.choice(string.ascii_letters).upper()}{random.choice(string.ascii_letters).upper()}{random.randint(0,9)}{random.randint(0,9)} {random.choice(string.ascii_letters).upper()}{random.choice(string.ascii_letters).upper()}{random.choice(string.ascii_letters).upper()}"
          reg_year = int(product[2:4])
          while True:
                    if reg_year > current_year:
                         if current_month >= 9 and 50 < reg_year <= current_year + 50:
                              return {
                                   'message':product
                              }
                         elif 50 < reg_year <= current_year + 49:
                              return {
                                   'message':product
                              }
                         else:
                              True
                    else:
                         return {
                                   'message':product
                              }
                
                              
        else: 
             return {
                    "message": "invalid plate format"
                         }
@app.get("/validate")
def index(test):
    if re.search(r"^[A-Z]{2}[0,1,2,5,6,7][0-9] ?[A-Z]{3}$", test.upper()):
        test_year = int(test[2]+test[3])
        if current_month > 9:
             if 51 <= test_year <= current_year + 50:
                  return {
                     "result": "valid"
                     }
             elif 2 <= test_year <= current_year:
                  return {
                       "result":"valid"
                  }
        else:
          if 2 <= test_year <= current_year:
               return {
                    "result":"valid"
               }
          elif 51 <= test_year <= current_year+49:
               return {
                    "result": "valid"
               }
          
          else:
               return {
                    "result": "invalid"
               }
        
    else:
        return{
            "result": "invalid"
        }
@app.get("/retrieve")
def index(check: str):
    headers = {
         "x-api-key": "0TN3ptrgL54LnZFQ2kRoS1tNoKQqr3Tv3eYJ0l7b"
         }
    url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"
    payload = {
         "registrationNumber": check
    }
    response = requests.request(
        "POST", url, headers = headers, json = payload
    )

    return response.json()
