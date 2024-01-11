#----------------------------------------------------------------------------
# IT209_Ahmad_Hamed_A7.py FCPD Crime Statistics Class
#
#
# Author:  Ahmad Hamed  04/18/2023
# NOTES: In this code I created a custom class called “FCPDCrime”
# that extends the ‘list’ class and adds five new custom methods: load, zipCodeList,
# printCrimes, countByZip, and countByCrime. The class
# will read in a file of csv data that you download from the Fairfax County
# Police site of crimes reported by zip code for a given week.
# The load function loads the data from the csv file and appends the data
# to itself (the object)
#------------------------------------------------------------------------

file_name = "CrimeReports.csv"


class FCPDCrime(list):
    def __init__(self, name = 'Fairfax County Police Crime report'):
        self.name = name
        super().__init__()

    def load(self, file = "CrimeReports.csv"):
        fi = open(file, 'r')
        Inlist = fi.readlines()
        fi.close()
        self.clear()
        for line in Inlist:
            fields = line.strip().split(',')
            self.append(fields)

    def zipCodeList(self, zip):
        for c in self:
            if c[8] == zip:
                print(c)

    def printCrimes(self):

        print('Fairfax County Police Crime Report :')

        print('\nFCPD Police Crime Statistcs for the week 2023-4-11 through 2023-04-18')

        input(f'{len(self)} lines follow, hit "Enter" to view:\n')
        for c in self:
            print(f'{c[0]:<2} {c[1]:<15} {c[2]:<53} {c[3]:<10} {c[4]:<4} {c[5]:<58} {c[6]:<16} {c[7]:<1} {c[8]}')

    def countByZip(self):
        zip_counts = {}
        for z in self:
            z_id = z[8]
            if z_id in zip_counts:
                zip_counts[z_id] += 1
            else:
                zip_counts[z_id] = 1

        sortedZip = sorted(zip_counts.items(), key=lambda x: x[1], reverse=True)

        occurrences_sum = 0

        print('Count of number of reports by Zip Code, sorted by frequency')

        print('\nFCPD Police Crime Statistcs for the week 2023-4-11 through 2023-04-18\n')

        for z_id, occurrences in sortedZip:
            occurrences_sum += occurrences

        for z_id, occurrences in sortedZip:
            z_divide = occurrences / occurrences_sum
            z_percent = z_divide * 100
            formatted_z_percent = f"{z_percent:.2f}%"
            if z_id == '':
                z_id = 'Zip not Listed'
            print(f'{z_id}:  {occurrences}  {formatted_z_percent}')

    def countByCrime(self, select = 'all'):
        crime_counts = {}
        for crime in self:
            if select == 'all' or select == crime[8]:
                crime_code = crime[1]
                crime_name = crime[2]
                if (crime_code, crime_name) in crime_counts:
                    crime_counts[(crime_code, crime_name)] += 1
                else:
                    crime_counts[(crime_code, crime_name)] = 1

        sortedCrime = sorted(crime_counts.items(), key=lambda x: x[1], reverse=True)

        print(f'List of Crimes by code, sorted by frequency, for {select} zip code(s)')

        print('\nFCPD Police Crime Statistcs for the week 2023-4-11 through 2023-04-18\n')
        crime_sum = 0

        for crime_name, occurrences in sortedCrime:
            crime_sum += occurrences

        for crime_name, occurrences in sortedCrime:
            crime_divide = occurrences / crime_sum
            crime_percent = crime_divide * 100
            formatted_crime_percent = f"{crime_percent:.2f}%"

            print(f'{crime_name[0]:<15}{occurrences:<4}{formatted_crime_percent:<7}{crime_name[1]}')

data = FCPDCrime('CrimeReports.csv')
data.load('CrimeReports.csv')
data.countByCrime('22303')
data.countByZip()
data.zipCodeList('22303')
data.printCrimes()
