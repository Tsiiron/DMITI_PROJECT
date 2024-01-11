import json

confidence = 0.95                # betta
significance = 1 - confidence    # alpha
t_distribution = 2.29

def create_interval(data : list) -> list:
    n = len(data)
    average = sum(data) / n
    sm1 = sum(list(map(lambda x : x**2, data))) / n
    sm2 = (sum(data) / n)**2
    dispersion = sm1 - sm2
    delta = dispersion ** 0.5 / n ** 0.5 * t_distribution
    interval = [round(average - delta), round(average + delta)]
    return interval


if __name__ == '__main__':

    with open('new_data.json', 'r') as file:
        file_content = file.read()
        data = json.loads(file_content)

    data_interval = {}

    for value in data.items():
        print(value)
        date = value[0]
        day = value[1]['day']
        night = value[1]['night']
        day_interval = create_interval(day)
        night_interval = create_interval(night)
        print(f"day = {day_interval}\nnight = {night_interval}")
        data_interval[date] = {'day' : day_interval, 'night' : night_interval}
    
    with open('interval.json', 'w') as file:
        json.dump(data_interval, file, indent=2, sort_keys=True)