import csv
with open("demo.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        x = int(row["Col1"])
        y = int(row["Col2"])
        z = int(row["Col3"])
        print(x+y+z)
