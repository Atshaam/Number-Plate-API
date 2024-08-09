# Number Plate API

## Overview: 

This API is built using the FastAPI framework.

API has 3 functions: can generate a new number plate following the current UK format, can validate provided number plates against current UK format and can provide information on vehicles using given number plate in all valid UK formats

## How to use:

### API has 3 endpoints; '/generate', '/validate' and '/retrieve':

'/generate' has the query parameter 'type' which currently can only take the string 'new', causing generation of new UK format plate

'/validate' has the query paramter 'test' which can take strings. If the number plate follows the new UK format and is in date then '"message":"valid"' is returned else '"message":"invalid"' is returned,

'/retrieve' has the query parameter 'check' if the number plate is in any valid UK format and is currently assigned to a vehicle then many different pieces of information from that vehicle are provided such as tax info, make, year of registration etc.

## Demo:

To get API running type into terminal:

```python
uvicorn Number_Plate_API:app --reload
```

(Replace 'Number_Plate_API' with your own file name if it's different)

![image](https://github.com/user-attachments/assets/eb5983ef-7720-448e-9f9f-585c20c13b1e)

![image](https://github.com/user-attachments/assets/f7b4ed65-344b-4cdb-9d7a-f909a6b4714b)

![image](https://github.com/user-attachments/assets/c200a8ab-632d-4755-9ceb-31bc44af13fe)

## Data retrieval:

For the '/retrieve' functionality the DVLA Open Data API is used.
API keys for this DVLA API are readily available on their website.

## Before using Number Plate API:

Requires Python 3.x 
Requires installation of the following libraries: FastAPI, random, string, re and requests

## Contributing:

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please create a GitHub issue or submit a pull request.

## Acknowledgments:

DVLA for API

Swagger for Time API

