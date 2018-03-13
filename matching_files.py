#!/usr/bin/env python3.6

# Version matching_files2.0.0.py

# Note: Code was Developed in the Abasht Laboratory at the University of Delaware under
# the supervision of Dr. Behnam Abasht
# website: http://canr.udel.edu/faculty/behnam-abasht/

#################################Matching Files Program####################################################
#################################Code Written by M. Joseph Tomlinson IV####################################

# Program compares two Files to see if they perfectly match. Compares the line count first and if the two files line
# counts match, continues with the more lengthy, line by line matching. Overall goal is to verify files match exactly.
# Was developed to verify two files are the same from a programs output. All user has to do is
# change the "Matching_Files_Parameter_File.txt" to their files of
# interests and run the program locally or in an HPC environment.

#Input:
#Program accepts an input parameter file (Matching_Files_Parameter_File.txt) with the
#file names of the files to be examined.

#Output:Two files
# File 1 (Report_File.txt) which contains a overview of the files and number of matching and mismatching lines of data
# File 2 (Mis-match_Report.txt) contains all lines of the files that do not match

##############################Code to Parse the Parameter File###########################
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
    mis_matching_Report.write("File"+"\t"+"Line"+"\n")

    #Opening the files to read the data (again)
    file_one = open(file_one, 'r')
    file_two = open(file_two, 'r')

    file_one_content=file_one.readlines()
    file_two_content=file_two.readlines()

    #set counter variables
    matching_line_count=0
    non_matching_line_count=0

    #Get the Mismatching Lines from Input File One
    for line_file_one in file_one_content:
        counter= 0
        for line_file_two in file_two_content:
           if line_file_one == line_file_two:
               matching_line_count+=1
               break
           else:
               counter+=1
               if counter == len(file_two_content):
                   mis_matching_Report.write("Input_File_One\t"+str(line_file_one))
               else:
                   pass

    mis_matching_Report.write("\n")

    #Get the Mismatching Lines from Input File Two
    for line_file_two in file_two_content:
        counter= 0
        for line_file_one in file_one_content:
           if line_file_one == line_file_two:
               break
           else:
               counter+=1
               if counter == len(file_one_content):
                   mis_matching_Report.write("Input_File_Two\t"+str(line_file_two))
               else:
                   pass
    
    return {'matching_line_count':matching_line_count}


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
    report_file.write("Summary Report of Analysis")
    report_file.write("\n")
    report_file.write("The number of lines of "+input_file_one+" is: "+str(file_one_count)+"\n")
    report_file.write("The number of lines of "+input_file_two+" is: "+str(file_two_count)+"\n")
    report_file.write("\n")
    report_file.write("Line counts match---checking lines"+"\n")

    line_counts=check_lines(input_file_one, input_file_two)
    matching_lines=line_counts['matching_line_count']
    report_file.write("The number of matching lines is "+str(matching_lines)+"\n")

    
main()
