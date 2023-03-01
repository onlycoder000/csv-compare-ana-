import csv

f=0
d=0
c=0
with open('import.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        eml=row[0]
        
        # print(eml)
        with open('all.csv') as csv_file:
            o=False
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row2 in csv_reader:
                # print(eml)
                # print(row2[6])
                if eml==row2[2]:
                    # print(row2[5])
                    o=True
                    break
            
        if o:
            with open('duplicate.csv', mode='a') as open_file:
                open_writer = csv.writer(open_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                open_writer.writerow(row2)
            f+=1
        else:
            with open('unique.csv', mode='a') as open_file:
                open_writer = csv.writer(open_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                open_writer.writerow(row2)
            d+=1
        c+=1
        print(' scan='+str(c)+' duplicate='+str(f)+' not matched='+str(d))
    print(row2[5])
