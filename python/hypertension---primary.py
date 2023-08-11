# Siobhan Reilly, Ivan Olier, Claire Planner, Tim Doran, David Reeves, Darren M Ashcroft, Linda Gask, Evangelos Kontopantelis, 2023.

import sys, csv, re

codes = [{"code":"G202.00","system":"readv2"},{"code":"G20z.11","system":"readv2"},{"code":"G2z..00","system":"readv2"},{"code":"3053HT","system":"oxmis"},{"code":"4000","system":"oxmis"},{"code":"4003","system":"oxmis"},{"code":"401 A","system":"oxmis"},{"code":"401 AC","system":"oxmis"},{"code":"401 AR","system":"oxmis"},{"code":"401 AT","system":"oxmis"},{"code":"401 BM","system":"oxmis"},{"code":"401 C","system":"oxmis"},{"code":"401 DC","system":"oxmis"},{"code":"401 LB","system":"oxmis"},{"code":"401 S","system":"oxmis"},{"code":"402 VH","system":"oxmis"},{"code":"403 AH","system":"oxmis"},{"code":"403 NG","system":"oxmis"},{"code":"4120BD","system":"oxmis"},{"code":"4360B","system":"oxmis"},{"code":"4360D","system":"oxmis"},{"code":"4380HP","system":"oxmis"},{"code":"4419H","system":"oxmis"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('hypertension-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["hypertension---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["hypertension---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["hypertension---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
