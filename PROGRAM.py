# Functions's purpose: read in a file name from the user and return it once they give one that exists
# Parameters: None
# Return: file name
import os
def filename(fileGiven):
    fileGiven = input( "Please enter a file name > " )
    while not os.path.exists( fileGiven):
        fileGiven = input("Please enter a file name > ")
    return(fileGiven)
filename(fileGiven)
# Function's purpose: Process the file
# Parameters: file name of file to read from
# Return: The maximum profit
def maximum_profit (filename):
    maxProfit = 0
    filename = open(filename,"r")
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
    print("The movie with the maximum profit is", maxMovieTitle , "with $", maxProfit,)
    return(maxProfit)



# Function's purpose: Process the file
# Parameters: file name of file to read from, file name of file to write to
# Return: None




# Function's purpose: main
# Parameters: None
# Return: None
def main():

    maximum_profit(filename)
#
# print("Filename", filename,"exists")
#
# output_filename = input("Please enter the output file name > ")
