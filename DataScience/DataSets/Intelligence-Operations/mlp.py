from sklearn.neural_network import MLPClassifier
import json
import csv
from sklearn.preprocessing import StandardScaler

path = "D:\Codes\DataScience\DataSets\Intelligence-Operations"
scaler = StandardScaler()

train = []
labels = []
with open(path + "train.csv", 'r', encoding='utf-8') as csvFile:
    csvReader = csv.reader(csvFile)
    head = next(csvReader)
    for row in csvReader:
        temp = []
        for i in range(105):
            if row[i + 1] != '' and row[i + 1] != "nan":
                temp.append(float(row[i + 1]))
            else:
                temp.append(0)
        train.append(temp)
        labels.append(int(row[106]))

scaler.fit(train)
train = scaler.transform(train)

clf = MLPClassifier(solver='adam', alpha=1e-4, hidden_layer_sizes=(75, 50), random_state=1, max_iter=150)
clf.fit(train, labels)
print(clf.loss_)

test = []
with open(path + "pre_contest_test1.csv", 'r', encoding='utf-8') as csvFile:
    csvReader = csv.reader(csvFile)
    head = next(csvReader)
    for row in csvReader:
        temp = []
        for i in range(105):
            if row[i] != '' and row[i] != "nan":
                temp.append(float(row[i]))
            else:
                temp.append(0)
        test.append(temp)
test = scaler.transform(test)
re = clf.predict(test)
dic = {}
for i in range(len(re)):
    print(re[i])
    dic[str(i)] = int(re[i])

f = open(path + "submit.json", 'w', encoding='utf-8')
json.dump(dic, f)
