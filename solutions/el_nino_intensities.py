import csv

years = []
mei = []

with open('mei_index.txt') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    next(reader, None)  # skip the header line
    for row in reader:
        years.append(int(row[0]))
        mei.append([float(i) for i in row[1:]])

season = []
mei_ext = []

for i in range(len(years)-1):
    season.append(str(years[i]) + str(years[i+1]))
    mei_ext.append(mei[i] + mei[i+1])

for i in range(len(mei_ext)):
    for j in range(len(mei_ext[i])-5):
        if all(idx >= 0.5 for idx in mei_ext[i][j:j+5]):
            season_str = season[i][:4] + '-' + season[i][-2:]
            max_mei = max(mei_ext[i])
            print('{}: El Nino (MEI={})'.format(season_str, max_mei))
            break
        elif all(idx <= -0.5 for idx in mei_ext[i][j:j+5]):
            season_str = season[i][:4] + '-' + season[i][-2:]
            min_mei = min(mei_ext[i])
            print('{}: La Nina (MEI={})'.format(season_str, min_mei))
            break
