# tinySA-Ultra-scan-tool
This tool is designed to work with tinySA Ultra (www.tinysa.org) CSV files captured into the SD card storage.

Download the files from the SD card into a folder on your computer. Then, execute the program.

The program executes the following operations:
1) combines all the files present in the folder of your selection;
2) divides the first-collumn value (frequency) by one million;
3) outputs a combined.csv file.
 
Conversion of the first-collumn value is necessary because Shure Wireless Workbench only accepts 2-collumn CSV files formatted in the following format:
    frequency_in_MHz,amplitude_in_dBm

tinySA Ultra CSV format is the following:
    frequency_in_Hz,amplitude_in_dBm
