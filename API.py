from fastapi import FastAPI
import random
import string
import re 
import requests

app = FastAPI()

@app.get("/generate")

def index(type: str):
        if type == "new":
            while True:
                product = f"{random.choice(string.ascii_letters).upper()}{random.choice(string.ascii_letters).upper()}{random.randint(0,9)}{random.randint(0,9)} {random.choice(string.ascii_letters).upper()}{random.choice(string.ascii_letters).upper()}{random.choice(string.ascii_letters).upper()}"
                if 51 > int(product[2]+product[3]) > 24:
                    True
                elif 74 < int(product[2]+product[3]):
                     True
                else:
                    return {
                        "message": product
                    }
                    break
                    
                
        else: 
             return {
                  "message": "invalid"
             }
@app.get("/validate")
def index(test):
    if re.search(r"^[A-Z]{2}[0,1,2,5,6,7][0-9] ?[A-Z]{3}$", test.upper()):
        if 51 > int(test[2]+test[3]) > 24:
                return {
                     "result": "invalid"
                }
        elif 74 < int(test[2]+test[3]):
                return{
                     "result":"invalid"
                }
        # space = %20 in URLs
        else:
            return {
                "result": "valid"
            }
    else:
        return{
            "result": "invalid"
        }
#using government API to get car details
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
    return response.json(), check


#to launch API locally in terminal: "uvicorn API:app --reload" - API can be replaced by name of file
#/generate: Generates a random car number plate.
#/validate: Validates a given car number plate for format compliance.
#/check_registration: Checks the registration details of a car based on its number plate.