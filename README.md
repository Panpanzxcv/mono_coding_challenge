# Wedding Database Management
This project manages wedding-related data using a SQLite database. It allows for the insertion of user and wedding data from CSV files and provides functionality to query users based on specific wedding dates.

## Features
- **SQLite Database**: Create and manage a local SQLite database (weddings.db).
- **Data Ingestion**: Read user and wedding data from CSV files (Users_Data.csv and Weddings_Data.csv) and populate the database.
- **Data Queries**:
    
    Retrieve users with weddings scheduled for June 
    2024.
    Retrieve users with weddings scheduled in the next two weeks.
- **Results Export**: Save the query results to a text file (wedding_results.txt).


## Prerequisites
- Python 3.8
- SQLite3
- CSV files (Users_Data.csv, Weddings_Data.csv) with the following structure:

    - Users_Data.csv:
        
        user_id, user_name
    
    - Weddings_Data.csv:
        
        user_id, wedding_date


## Usage
1. Ensure the required CSV files are in the same directory as the script.
2. Run the script:
    
        python wedding_database.py

3. The results will be saved in wedding_results.txt.



