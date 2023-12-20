import json

if __name__ == '__main__':
    with open('data.json', 'r') as file:
        file_content = file.read()
        data = json.loads(file_content)

    # print(data)

    for value in data.items():
        print(value[0], value[1]['day'], value[1]['night'])