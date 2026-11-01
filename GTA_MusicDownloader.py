import requests
import csv 
import io
import subprocess

#sheetsLink = "Link Here"  
#targetDir = "Working folder here"

def requestInfo():
    response = requests.get(sheetsLink)
    response.raise_for_status() # Should raise an error, if the url is invalid

    return csv.reader(io.StringIO(response.text))

def isPlayList(input):
    return "&list=" in input # Returns a boolean. True, if contains playlist URL tag

def isInvalidLink(input):
    return "www.youtube.com" not in input and "youtu.be" not in input # Returns true, if the link is invalid

def powerShellCommand(input):
    return subprocess.run(["yt-dlp", "-x", "--match-filter", "duration < 360", "--audio-format", "mp3", "--audio-quality", "0", "--cookies-from-browser", "firefox", input], cwd=targetDir)

def main(): # This feels quite weird not defining a main or data types
    reader = requestInfo() # Fetch the result from the servers and an iterator for em
    next(reader) # Skip the first row
    print("Downloading links: ")

    for row in reader: # type() is class '_csv.reader'
        print('\n' + str(reader.line_num) + ": " + row[1] + '\n')
        if(isPlayList(row[0])):
            print("SKIPPED - Was a playlist: " + row[1])
            continue
        elif(isInvalidLink(row[0])):
            print("SKIPPED - Invalid link: " + row[1])
            continue
            
        powerOut = powerShellCommand(row[0]) # Take the first item of the row only. The reader's items seem to be like a 2D array.
        if(powerOut.returncode != 0):
            print("An Exception for: " + row[1] + " - " + row[0])


# Execute main
main()
print('\n' + "Track update complete!")

#playlist1 = "https://www.youtube.com/watch?v=ilqeDbu4E8Y&list=RDilqeDbu4E8Y&start_radio=1"
#playlist2 = "https://www.youtube.com/watch?v=TYuhD-JuNLY&list=RDOe3FG4EOgyU&index=2"
#notPlaylist = "https://youtu.be/TYuhD-JuNLY?si=de0LrCfovqhXJ149"
#isPlayList(notPlaylist)