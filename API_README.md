Overview: 

API has 3 functions: can generate a new number plate following the new UK format, can validate provided number plates against current UK format and can provide information on vehicles using given number plate in all valid UK formats

How to use:

API has 3 endpoints; '/generate', '/validate' and '/retrieve'

'/generate' has the query parameter 'type' which currently can only take the string 'new', causing generation of new UK format plate

'/validate' has the query paramter 'test' which can take strings. If the number plate follows the new UK format and is in date then '"message":"valid"' is returned else '"message":"invalid"' is returned,

'/retrieve' has the query parameter 'check' if the number plate is in the UK  
