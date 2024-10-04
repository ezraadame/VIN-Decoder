# VIN-Decoder
This is a simple VIN decoder using Python and the NHTSA website's API to return vehicle information.

To keep it simple I kept it to the basic information needed for a vehicle.
Make, Model, Year, Body Type, Engine, Trim.

The user is initially prompted to enter in a VIN. If the API call to the NHTSA website finds information on the VIN provided, it will output the information to each respective variable.

The code itself imports requests and a function called decoding_vin is primarily used.
In the decoding_vin function the function is retreieving data from the website. If the response status comes back the data is then formatted as JSON.
The 6 variables initially start off with 'None', but in a for loop inside the function the variables are updated.
With the data being retrived each varibale is assigned data that corresponds to them respectively. If nothing is returned a 'N/A' will be outputted instead.

This function also holds the main function, allowing the code to run.
