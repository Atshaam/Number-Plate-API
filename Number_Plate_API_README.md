Overview: 

API has 3 functions: can generate a new number plate following the current UK format, can validate provided number plates against current UK format and can provide information on vehicles using given number plate in all valid UK formats

How to use:

API has 3 endpoints; '/generate', '/validate' and '/retrieve':

'/generate' has the query parameter 'type' which currently can only take the string 'new', causing generation of new UK format plate

'/validate' has the query paramter 'test' which can take strings. If the number plate follows the new UK format and is in date then '"message":"valid"' is returned else '"message":"invalid"' is returned,

'/retrieve' has the query parameter 'check' if the number plate is in any valid UK format and is currently assigned to a vehicle then many different pieces of information from that vehicle are provided such as tax info, make, year of registration etc.

This API was built using the FastAPI framework.

Data retrieval:

For the '/retrieve' functionality the DVLA Open Data API is used.
API keys for this DVLA API are readily available on their website.

Before using Number Plate API:

Requires Python 3.x 
Requires installation of the following libraries: FastAPI, random, string, re and requests

Here are some examples on how to use each endpoint:

'/generate': 

'http://127.0.0.1:8000/generate?type=new' yields:

{"message":"QD65 SRZ"} {as an example}


'/validate': 

'http://127.0.0.1:8000/validate?test=QD65%20SRZ' {'%20' replaces the space}, yields:

'{"result":"valid}'

'/retrieve':

'http://127.0.0.1:8000/retrieve?check=AB12CDE', yields:

'{
  "registrationNumber": "AB12CDE",
  "taxStatus": "Taxed",
  "taxDueDate": "2024-12-01",
  "motStatus": "Valid",
  "make": "VAUXHALL",
  "yearOfManufacture": 2017,
  "engineCapacity": 1399,
  "co2Emissions": 128,
  "fuelType": "PETROL",
  "markedForExport": false,
  "colour": "WHITE",
  "typeApproval": "M1",
  "dateOfLastV5CIssued": "2018-01-26",
  "motExpiryDate": "2025-06-11",
  "wheelplan": "2 AXLE RIGID BODY",
  "monthOfFirstRegistration": "2017-06"
}'










