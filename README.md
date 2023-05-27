# tinySA-Ultra-scan-tool
Tool for combining multiple tinySA Ultra CSV files into a single Shure Wireless Workbench (WWB) compatible CSV file

This tool is designed to work with tinySA Ultra (www.tinysa.org) CSV files stored in the SD card.

The program executes the following operations:
1) combines all the files present in a folder of your selection
2) divides the first value (frequency) by one million, effectively transforming the value from Hz to MHz. 
 
This conversion is necessary because Shure Wireless Workbench only accepts 2-collumn CSV files formatted in this format:
    frequency_in_MHz,amplitude_in_dBm
