
# DynamoDB Dummy Data Generator

This Python script allows you to generate dummy records and insert them into a DynamoDB table. You can also use this script to load records from a JSON file and insert them into DynamoDB. The script supports specifying an AWS profile for connecting to DynamoDB.

## Features

- **Generate Dummy Records**: Create a specified number of dummy records with predefined attributes and insert them into a DynamoDB table.
- **Output to JSON**: Optionally output the generated dummy records to a JSON file.
- **Load from JSON**: Load records from a JSON file and insert them into a DynamoDB table.
- **AWS Profile Support**: Specify an AWS profile to use for connecting to DynamoDB.

## Prerequisites

- Python 3.x
- `boto3` library (AWS SDK for Python)
- `Faker` library (for generating random dummy data)

### Install Required Python Packages

```bash
pip install boto3 faker
```

## Usage

### Command-Line Arguments

- `--table_name` (Required): The name of the DynamoDB table where records will be inserted.
- `--num_records` (Optional): The number of dummy records to generate.
- `--output_json` (Optional): The file path to save the generated dummy records in JSON format.
- `--input_json` (Optional): The file path to a JSON file containing records to be inserted into DynamoDB.
- `--profile` (Optional): The AWS profile to use for connecting to DynamoDB.

### Running the Script

1. **Generate and Insert Dummy Records**

   Generate 100 dummy records, insert them into the specified DynamoDB table.

   ```bash
   python main.py --table_name YourDynamoDBTableName --num_records 100  --profile your_aws_profile
   ```

   If you don't specify an AWS profile, the default profile will be used.

2. **Generate and Export Dummy Records to JSON**

   Generate 100 dummy records, and output the records to a JSON file.

   ```bash
   python main.py --table_name YourDynamoDBTableName --num_records 100 --output_json dummy_records.json --profile your_aws_profile
   ```

   If you don't specify an AWS profile, the default profile will be used.

3. **Insert Records from JSON**

   Insert records from a JSON file into the specified DynamoDB table.

   ```bash
   python main.py YourDynamoDBTableName --input_json dummy_records.json --profile your_aws_profile
   ```

   This reads the records from `dummy_records.json` and inserts them into `YourDynamoDBTableName` using the specified AWS profile.

### Example Usage

1. **Generate 50 Dummy Records and Insert into DynamoDB**

   ```bash
   python script_name.py --table_name MyDynamoDBTable --num_records 50
   ```

2. **Generate 10 Dummy Records, Output to JSON, and Insert into DynamoDB**

   ```bash
   python script_name.py --table_name MyDynamoDBTable --num_records 10 --output_json my_dummy_data.json
   ```

3. **Load Records from JSON and Insert into DynamoDB**

   ```bash
   python script_name.py --table_name MyDynamoDBTable --input_json my_dummy_data.json
   ```

## Example Record Structure

Each dummy record contains the following attributes:

- `dbHost`: A random domain name (String).
- `dnsExists`: Whether DNS exists (Boolean).
- `created`: Creation date (Date, in ISO 8601 format).
- `daysUnhealthy`: Number of days the item has been unhealthy (Integer, 0 to 8).
- `dnsValid`: Whether DNS is valid (Boolean).
- `accountExists`: Whether the account exists (Boolean).
- `healthy`: Whether the item is healthy (Boolean).
- `version`: Version number (Integer).

## License

This project is licensed under the MIT License.
