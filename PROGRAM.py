# Functions's purpose: read in a file name from the user and return it once they give one that exists
# Parameters: None
# Return: file name
import os
def filename():
    fileGiven = input( "Please enter a file name > " )
    while not os.path.exists( fileGiven):
         fileGiven = input("Please enter a file name > ")
    return fileGiven
# Function's purpose: Process the file
# Parameters: file name of file to read from
# Return: The maximum profit
def maximum_profit (fileGiven):
    try:
        maxProfit = 0
        filename = open(fileGiven,"r")
        for line in filename:
            #print(line, end = "")
            movieData = line
            releaseDate, movieTitle, budget, boxOfficeGross = movieData.split(",")
            # print(releaseDate)
            # print(movieTitle)
            # print(budget)
            # print(boxOfficeGross)
            budget = float(budget)
            boxOfficeGross = float(boxOfficeGross)
            profit = boxOfficeGross - budget
            if profit > maxProfit:
                maxProfit = profit
                maxMovieTitle = movieTitle
        print("The movie with the maximum profit is", maxMovieTitle , "with $%.2f" % maxProfit,)
        return(maxProfit)
    except FileNotFoundError:
        print("ERROR: FILE NOT FOUND")



# Function's purpose: Process the file
# Parameters: file name of file to read from, file name of file to write to
# Return: None
def writeNewFile(fileInput,fileOutput):
    fileNew = open(fileOutput,"w")
    fileOld = open(fileInput,"r")
    for line in fileOld:
        #print(line, end = "")
            movieData = line
            releaseDate, movieTitle, budget, boxOfficeGross = line.split(",")
            print("Release Date:",releaseDate, file =fileNew)
            print(movieTitle , file =fileNew)
            print("Budge of Movie:", budget, file =fileNew)
            print("Total Box Office Gross:", boxOfficeGross, file =fileNew)
            budget = float(budget)
            boxOfficeGross = float(boxOfficeGross)
            profit = boxOfficeGross - budget
    return



# Function's purpose: main
# Parameters: None
# Return: None
def main():
    fileInput = filename()

    print("Filename", fileInput,"exists")
    maximum_profit(fileInput)
    fileOutput = input("Please enter the name of the file you want to output to >")
    writeNewFile(fileInput,fileOutput)
# output_filename = input("Please enter the output file name > ")
main()
