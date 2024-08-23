import boto3
import random
import json
from datetime import datetime
from faker import Faker
import argparse

def generate_dummy_data():
    fake = Faker()
    
    # Random data generation
    db_host = fake.domain_name()
    dns_exists = random.choice([True, False])
    created = fake.date_time_this_year().isoformat()  # ISO 8601 format
    days_unhealthy = random.randint(0, 8)  # Constrained to 8 or less
    dns_valid = random.choice([True, False])
    account_exists = random.choice([True, False])
    healthy = random.choice([True, False])
    version = random.randint(1, 10)
    
    return {
        'dbHost': {"S": db_host},
        'dnsExists': {"BOOL": dns_exists},
        'created': {"S": created},
        'daysUnhealthy': {"N": str(days_unhealthy)},
        'dnsValid': {"BOOL": dns_valid},
        'accountExists': {"BOOL": account_exists},
        'healthy': {"BOOL": healthy},
        'version': {"N": str(version)},
    }

def create_dummy_records(table_name, num_records, output_json=None, profile=None):
    items = []

    for _ in range(num_records):
        item = generate_dummy_data()
        items.append(item)

    if output_json:
        with open(output_json, 'w') as json_file:
            json.dump(items, json_file, indent=4)
        print(f"Dummy records written to {output_json}")
    else:
        session = boto3.Session(profile_name=profile) if profile else boto3.Session()
        dynamodb = session.client('dynamodb')
        for item in items:
            dynamodb.put_item(TableName=table_name, Item=item)
            print(f"Inserted item: {item}")

def load_records_from_json(table_name, input_json, profile=None):
    session = boto3.Session(profile_name=profile) if profile else boto3.Session()
    dynamodb = session.client('dynamodb')

    with open(input_json, 'r') as json_file:
        items = json.load(json_file)

    for item in items:
        dynamodb.put_item(TableName=table_name, Item=item)
        print(f"Inserted item from JSON: {item}")

def main():
    parser = argparse.ArgumentParser(description="Generate and insert dummy records into DynamoDB or from JSON.")
    parser.add_argument("--table_name", required=True, help="(Required) Name of the DynamoDB table.")
    parser.add_argument("--num_records", type=int, help="(Optional) Number of dummy records to generate.")
    parser.add_argument("--output_json", help="(Optional) File path to output the generated dummy records as JSON.")
    parser.add_argument("--input_json", help="(Optional) File path to JSON file containing records to be added to DynamoDB.")
    parser.add_argument("--profile", help="(Optional) AWS profile to use for connecting to DynamoDB.")

    args = parser.parse_args()

    if args.input_json:
        load_records_from_json(args.table_name, args.input_json, args.profile)
    elif args.num_records:
        create_dummy_records(args.table_name, args.num_records, args.output_json, args.profile)
    else:
        print("Error: Either --num_records or --input_json must be provided.")

if __name__ == "__main__":
    main()
