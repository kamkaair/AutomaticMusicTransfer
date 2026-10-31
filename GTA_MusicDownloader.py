import requests
import csv 
import io

sheetsLink = "Link Here"  

def requestInfo():
    response = requests.get(sheetsLink)
    print(type(response))
    #response.raise_for_status()

    return csv.reader(io.StringIO(response.text))

def main(): # This feels quite weird not defining a main or data types
    reader = requestInfo() # Fetch the result from the servers and an iterator for em
    #print(type(reader))
    next(reader) # Skip the first row
    print("The links: ")
    #print(reader.line_num) # Gets the index of the current line

    for row in reader: # type() is class '_csv.reader'
        print(row[0]) # Take the first item of the row only. The reader's items seem to be like a 2D array.

# Execute main
main()