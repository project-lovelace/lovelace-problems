import csv

years = []
mei = []

def mei_to_intensity(mei_val):
    mei_val = abs(mei_val)
    if mei_val < 0.5:
        return "none"
    elif 0.5 <= mei_val < 1.0:
        return "weak"
    elif 1.0 <= mei_val < 1.5:
        return "moderate"
    elif 1.5 <= mei_val < 2.0:
        return "strong"
    elif 2.0 <= mei_val:
        return "very strong"

with open('mei.ext_index.txt') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    next(reader, None)  # skip the header line
    for row in reader:
        years.append(int(row[0]))
        mei.append([float(i) for i in row[1:]])

mei_dict = {}
for i in range(len(years) - 1):
    season = str(years[i])[:4] + '-' + str(years[i + 1])[-2:]
    season_mei = mei[i] + mei[i+1]
    for j in range(len(season_mei) - 5):
        if all(idx >= 0.5 for idx in season_mei[j:j + 5]):
            max_mei = max(season_mei)
            
            mei_dict[season] = ("El Nino", mei_to_intensity(max_mei), max_mei)
            break
        elif all(idx <= -0.5 for idx in season_mei[j:j + 5]):
            min_mei = min(season_mei)
            mei_dict[season] = ("La Nina", mei_to_intensity(min_mei), min_mei)
            break
        else:
            mei_dict[season] = ("Neither", "none", 0)
			
def enso_classification(season):
    return mei_dict[season]