import csv

def solution():
    years = []
    mei = []

    with open('mei.ext_index.txt') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        next(reader, None)  # skip the header line
        for row in reader:
            years.append(int(row[0]))
            mei.append([float(i) for i in row[1:]])

    classification_str = ''
    for i in range(len(years) - 1):
        season = str(years[i])[:4] + '-' + str(years[i + 1])[-2:]
        season_mei = mei[i] + mei[i + 1]
        for j in range(len(season_mei) - 5):
            if all(idx >= 0.5 for idx in season_mei[j:j + 5]):
                max_mei = max(season_mei)
                classification_str = classification_str + '{}: El Nino (MEI={})'.format(season, max_mei) + '\n'
                break
            elif all(idx <= -0.5 for idx in season_mei[j:j + 5]):
                min_mei = min(season_mei)
                classification_str = classification_str + '{}: La Nina (MEI={})'.format(season, min_mei) + '\n'
                break
                
    return classification_str