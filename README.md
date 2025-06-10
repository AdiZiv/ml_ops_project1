# ml_ops_project1
Customer churn model deployment with batch processing, real-time REST API, monitoring, and alerts. Includes error handling and Dockerized setup. Supports daily batch runs and real-time predictions using a trained RandomForestClassifier.




step #1: Write a Batch Processing Script:
1.	Create a Python batch processing that:
•	Reads the batch data from a given input CSV file.
•	Loads the pre-trained model (provided as a pickle file).
•	Runs predictions on the batch data and adds the predictions as a new column.
•	Saves the updated batch data (with predictions) to a new CSV file (output/predictions.csv).
•	
Notes:
-	Ensure the script accepts the input file and output file as arguments when the script is executed.
-	Try to write the script as OOP as your can (split to different classes and funcs)
-	Make the script Flexible to changes  (new model, new data source) 


=====================================================

Missing Requirements:
Command-line arguments for input/output files - currently hardcoded in config.py
No explicit error handling visible in the code
No logging mechanism visible
Suggestions for Improvement:
Add command-line argument parsing to make input/output files configurable at runtime
Add proper error handling and logging
Add input validation for the dataset
Add docstrings and type hints for better code documentation
Consider adding a proper logging mechanism
Would you like me to help you implement any of these improvements to better meet the requirements?

=====================================================

step #2: Dockerize the Solution
Containerize the entire batch processing pipeline using Docker. You'll create a Dockerfile that:

-	Sets up a Python environment with all required dependencies.
-	Copies the batch processing script and necessary assets (model file, input data) into the container.
-	Runs the batch processing script automatically.

Expected Workflow inside the Docker container:
-	The input batch file (input.csv) is provided.
-	Predictions are saved to output/predictions.csv.

step #3: PostgreSQL Integration
Use a PostgreSQL database as input instead of a CSV file:
1.	Write code to load the batch data from a PostgreSQL table instead of reading from a CSV file.
2.	Store the predictions back into a new table in the PostgreSQL database.
Steps:
1.	Set up a PostgreSQL database as a Docker container.
2.	Create a table data with relevant columns 
3.	Populate the table with example data.
4.	Update your Python batch processing script to query data from this table, run predictions, and then save the output back into another table (e.g., bike_sharing_predictions).

