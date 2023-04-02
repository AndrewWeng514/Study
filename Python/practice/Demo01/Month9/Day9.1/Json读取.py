import json

import json

fp = open('./train.json', 'r', encoding='utf-8')
content = fp.read()
content = json.loads(content)

for key1 in content:
    if key1 == 'data':
        dataValue = content[key1]
        for key2 in dataValue:
            if key2 == 'trainList':
                trainList = dataValue[key2]
                for train in trainList:
                    trainName = train['trainName']
                    startStation = train['startStationName']
                    endStation = train['endStationName']
                    i = 0
                    for seat in train['seatBookingItem']:
                        print(trainName, startStation, endStation, seat['seatName'], seat['price'])
                        i = i + 1
