import csv

csv_file = open("./short_logs.csv","r",encodin="ms932",errors="",newline="")

f = csv.reader(csv_file,delimiter=",",diublequote=True,lineterminator="\r\n",quotechar="",skipinitialspace=True)

f = csv.DictReader(csv_file,delimiter=",",diublequote=True,lineterminator="\r\n",quotechar="",skipinitialspace=True)

