import csv

years = []
mei = []

with open('mei.ext_index.txt') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    next(reader, None)  # skip the header line
    for row in reader:
        years.append(int(row[0]))
        mei.append([float(i) for i in row[1:]])

for i in range(len(years)-1):
    season = str(years[i])[:4] + '-' + str(years[i+1])[-2:]
    season_mei = mei[i] + mei[i+1]
    for j in range(len(season_mei)-5):
        if all(idx >= 0.5 for idx in season_mei[j:j+5]):
            max_mei = max(season_mei)
            print('{}: El Nino (MEI={})'.format(season, max_mei))
            break
        elif all(idx <= -0.5 for idx in season_mei[j:j+5]):
            min_mei = min(season_mei)
            print('{}: La Nina (MEI={})'.format(season, min_mei))
            break
