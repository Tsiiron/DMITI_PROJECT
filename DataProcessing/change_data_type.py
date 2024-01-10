import json

if __name__ == '__main__':
    with open('data.json', 'r') as file:
        file_content = file.read()
        data = json.loads(file_content)

    raw_data = {}

    for value in data.items():
        date = value[0]
        date1 = date[5:]
        day = value[1]['day']
        night = value[1]['night']
        print(date, date1, day, night)
        if date1 in raw_data:
            raw_data[date1]['day'].append(day)
            raw_data[date1]['night'].append(night)
        else:
            raw_data[date1] = {'day' : [day], 'night' : [night]}

    with open('new_data.json', 'w') as file:
        json.dump(raw_data, file, indent=2, sort_keys=True)
        