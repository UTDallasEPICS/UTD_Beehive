To clarify some things for the backend:
- index.js under the server directory is the final version of the backend code that we displayed at the final expo. However, this only utilizes weight.
- onlyWeightIndex.js under the saved-code directory is similar to the above code in that it only utilized weight.
- index-1-post-req.js under the saved-code directory uses 1 post request to get weight, temp, and humidity info from the ESP32 and store it in a database.
- index-3-post-reqs.js under the saved-code directory uses 3 post requests to separately get weight, temp, and humidity info from the ESP32 and store it in a database.

The code may be a bit hard to understand (especially if you are new to JavaScript), so please feel free to reach out to Hassan Hashemian or Benjamin Lopez for help! Contact information can be found in the Spring 2023 final report.
