# Write a program that prompts for a file name, then opens that file and reads through the file,
# looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point
# values from each of the lines and compute the average of those
# values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
# when you are testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)  # Open the file with the provided file name
except FileNotFoundError:
    print("File not found.")
    quit()

total_confidence = 0.0
count = 0

for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        colon_pos = line.find(':')  # Find the position of ':'
        confidence_str = line[colon_pos + 1:].strip()  # Extract confidence value as a string
        confidence_float = float(confidence_str)  # Convert the string to a float
        total_confidence += confidence_float  # Add the confidence value to the total
        count += 1  # Increment the count of confidence values

fh.close()  # Close the file after processing

if count > 0:
    average_confidence = total_confidence / count  # Calculate the average
    print(f"Average spam confidence: {average_confidence:}")
else:
    print("No 'X-DSPAM-Confidence' values found in the file.")


