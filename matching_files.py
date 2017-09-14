#!/usr/bin/env python3.6

# Note: Code was Developed in the Abasht Laboratory at the University of Delaware under
# the supervision of Dr. Behnam Abasht
# website: http://canr.udel.edu/faculty/behnam-abasht/

#################################Comparing Files to See if they Match (Identical Matches)#######################
#################################Code Written by M. Joseph Tomlinson IV#########################################

#Program compares two Files to see if they perfectly match. Compares the line
#count first and if the two file match, continues with the more lengthy, line by
#line matching. Overall goal is to verify files match exactly. Was developed to
#verify two files are the same from a programs output

#Input:
#Program accepts an input parameter file (Matching_Files_Parameter_File.txt) with the
#file names of the files to be examined.

#Output:Two files
# File 1 (Report_File.txt) which contains a overview of the files and number of matching and mismatching lines of data
# File 2 (Mis-match_Report.txt) contains all lines of the files that do not match

####################################################Code to Parse the Parameter File################################################
#Definition splits up a line based on tab
#to return the input value from that line
def split_variable (line):
    key,value = line.split("\t")
    return (value)

def read_parameter_file (input_file):
    file_parameters=[line.strip() for line in input_file]

    #Retrieve all the various lines of input (keys and values)---need to get just input parameters
    input_line_1=file_parameters[1]
    input_line_2=file_parameters[2]
    
    #Split the key, value pairs of information from the parameter file
    input_file_one = split_variable(input_line_1)
    input_file_two = split_variable(input_line_2)

    #return file names as dictionaries
    return{'input_file_one_name':input_file_one, 'input_file_two_name':input_file_two}

####################Functions to Run Actual Program###########################################################

#definition opens a file and returns the line count of the files
#to compare between the two files
def line_counter(file):
    data = open(file, 'r') #Open the file in python
    #gets the data as a list and then retrieve its length
    file_data=data.readlines()
    count=len(file_data)
    return (count)


#function check_lines goes through and checks lines (assuming same order) to
#see if the lines are perfect matches
def check_lines(file_one, file_two):
    mis_matching_Report=open("Mis-match_Report.txt","w")
    mis_matching_Report.write("The following lines below do not match"+"\n")
    mis_matching_Report.write("File_1"+"\t"+"File_2"+"\n")

    #Opening the files to read the data (again)
    file_one = open(file_one, 'r')
    file_two = open(file_two, 'r')

    file_one_content=file_one.readlines()
    file_two_content=file_two.readlines()

    #set counter variables
    matching_line_count=0
    non_matching_line_count=0

    #Begin examining lines of files for matches (found suggestion to use this style of zipping
    #and overall style of code for file matching from  
    #https://stackoverflow.com/questions/11253667/compare-files-line-by-line-to-see-if-they-are-the-same-if-so-output-them 
    #extremely fast and efficienty way to parse through all the data in both files (VERY fast)

    zipped_data=zip(file_one_content,file_two_content)

    for x, y in zipped_data:
       if x == y:
           matching_line_count+=1
       else:
           mis_matching_Report.write(x+"\t"+y)
           non_matching_line_count+=1
    return {'matching_count':matching_line_count, 'non_matching_count':non_matching_line_count}


def main():

    #Opens the parameter file to get all the required inputs for the rest of the code
    input_file = open('Matching_Files_Parameter_File.txt', 'r') #Open the file in python
    parameters=read_parameter_file(input_file) #Definition to parse through a file for parameters
    input_file.close() ####Close the intial file

    #Files that you would like to compare and see if they are the same
    input_file_one=parameters['input_file_one_name']
    input_file_two=parameters['input_file_two_name']

    #Initially count the lines of each file (if different, might want to rethink
    #code)
    file_one_count=line_counter(input_file_one)
    file_two_count=line_counter(input_file_two)

    #Create report files for if the data matches or not
    report_file=open("Report_File.txt","w")
    report_file.write("The number of lines of "+input_file_one+" is: "+str(file_one_count)+"\n")
    report_file.write("The number of lines of "+input_file_two+" is: "+str(file_two_count)+"\n")

    #Actual  running of the program to compare lines of the file
    #if the line counts match, will continue to run the program
    if file_one_count==file_two_count:
        report_file.write("Line counts match---checking lines"+"\n")
        line_counts=check_lines(input_file_one, input_file_two)

        matching_lines=line_counts['matching_count']
        non_matching_lines=line_counts['non_matching_count']

        report_file.write("The number of matching lines is "+str(matching_lines)+"\n")
        report_file.write("The number of lines NOT matching "+str(non_matching_lines))

    #If line count is not the same program ends  
    else:
        report_file.write("Line counts DO NOT match---killing program")
    
main()










