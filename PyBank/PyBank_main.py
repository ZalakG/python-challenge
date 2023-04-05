# import the os module which allows to create file path across operating system
import os

# module for reading CSV files
import csv

BgtData_csv = os.path.join("C:/Zalak-Course/Module3_Challenge/python-challenge/PyBank/Resources/budget_data.csv")
BgtData_csv_Output = os.path.join("C:/Zalak-Course/Module3_Challenge/python-challenge/PyBank/Resources/analysis_data.csv")

# Open and read budget_data CSV file
with open(BgtData_csv, newline = "")as csvfile:

    # Specifies delimiter and variables in the file that holds contents
    csvreader = csv.reader(csvfile, delimiter = ',')

    csv_header = next(csvfile)
    
    # Declare variables that holds data
    # months for the "Date" column
    # net_total for the "Profit/Losses" column
    months = []
    net_total = [] 

    # For loop to read data from each raw after header 
    for row in csvreader:
        months.append(row[0]) 
        net_total.append(int(row[1]))

    # Calculate total number of months in "Date" column
    total_months = len(months)

     # Declare variable that holds Cahanges
    PL_change = []

    # For loop to find change in Profit/Loss
    for a in range (1, len(net_total)):
        PL_change.append((int(net_total[a]) - int(net_total[a-1])))
                    
    # calculation for average change
    avg_PL_change = round(sum(PL_change) / len(PL_change),2)

    # calculate greatest increase in profits (date and amount) over the entire period
    grt_increase = max(PL_change)

    #calculate greatest decrease 
    grt_decrease = min(PL_change)

    # Print the following results to the terminal

    print("Financial Analysis")
    print("--------------------------------")
    print("Toatal Months: " + str(total_months))
    print("Total: " + "$" + str(sum(net_total)))
    print("Average Change: " + "$" + str( avg_PL_change))
    print("Greatest Increase in Profits: " + str(months[PL_change.index(max(PL_change ))+1]) + " " + "(" + "$" + str(grt_increase) + ")")
    print("Greatest Decrease in Profits: " + str(months[PL_change.index(min(PL_change ))+1]) + " " + "(" + "$" + str(grt_decrease) + ")")

    # output/write into a text file named fin_analysis.txt in Analysis folder

    output = f"Financial Analysis \n\n--------------------------------\n\nToatal Months: {str(total_months)} \nTotal: ${str(sum(net_total))} \nAverage Change: ${str( avg_PL_change)} \nGreatest Increase in Profits:  {str(months[PL_change.index(max(PL_change ))+1])}  (${str(grt_increase)})\nGreatest Decrease in Profits: {str(months[PL_change.index(min(PL_change ))+1])} (${str(grt_decrease)})\n"

    with open("C:/Zalak-Course/Module3_Challenge/python-challenge/PyBank/Analysis/fin_analysis.txt", "w")as file:
        file.write(output)
        file.close()

    

    






    

#