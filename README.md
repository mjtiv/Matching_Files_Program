# Matching_Files_Program 

Written by M. Joseph Tomlinson IV

Program Compares to two files to see if they are identical line by line

Note: Code was Developed in the Abasht Laboratory at the University of Delaware under
the supervision of Dr. Behnam Abasht
website: http://canr.udel.edu/faculty/behnam-abasht/

# Program Overview
Program compares two Files to see if they perfectly match. Compares the line
count first and if the two files line counts match, continues with the more lengthy, line by
line matching. Overall goal is to verify files match exactly. Was developed to
verify two files are the same from a programs output. All user has to do is change 
the "Matching_Files_Parameter_File.txt" to their files of interests and run the program locally
or in an HPC environment. 

# Program Files:
matching_files.py (python script file)

Matching_Files_Paramter_File.txt (input paramter file to run program)



# Output:Two files
# File 1 (Report_File.txt) which contains a overview of the files and number of matching and mismatching lines of data
# File 2 (Mis-match_Report.txt) contains all lines of the files that do not match
