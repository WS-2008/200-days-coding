# Firstly, defining smart meter readings
readings = [
    "Voltage: 230V\n",
    "Current: 5A\n",
    "Power: 1150W\n",
    "Energy: 2.5kWh\n"
]

# 1. Creating the file and write readings using open(fn, 'w') and fh.writelines(S)
fh = open("smart_meter.txt", 'w')
fh.writelines(readings)
fh.close()

# 2. Open the file for reading using open(fn, 'r') and fh.read()
fh = open("smart_meter.txt", 'r')
full_content = fh.read()
print("Using fh.read():")
print(full_content)
fh.close()

# 3. Read one line using fh.readline()
fh = open("smart_meter.txt", 'r')
first_line = fh.readline()
print("Using fh.readline():", first_line.strip())
fh.close()

# 4. Read all lines into a list using fh.readlines()
fh = open("smart_meter.txt", 'r')
lines = fh.readlines()
print("Using fh.readlines():", lines)
fh.close()

# 5. Append a new reading using open(fn, 'a') and fh.write(s)
fh = open("smart_meter.txt", 'a')
fh.write("Frequency: 50Hz\n")
fh.close()

# 6. Read again to show updated content
fh = open("smart_meter.txt", 'r')
updated_content = fh.read()
print("Updated content after appending:")
print(updated_content)
fh.close()
