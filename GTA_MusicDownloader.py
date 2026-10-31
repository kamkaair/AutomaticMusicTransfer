import requests
import csv 
import io

def requestInfo():
    sheetsLink = "Link Here"

    response = requests.get(sheetsLink)
    response.raise_for_status()

    return csv.reader(io.StringIO(response.text))

def main():
    # This feels quite weird not defining a main or data types
    reader = requestInfo()

    for row in reader:
        print(row)

# Execute main
main()