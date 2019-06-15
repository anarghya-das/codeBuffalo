import csv


def get_personality():
    # aritra's code + API call
    pass


def get_text(row):
    return (int(row[0]), row[-1])


def main():
    reader = None
    content = []
    with open('Reviews.csv') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            content.append(get_text(row))
            if i == 3:
                break
    print(content)
    personalites = []
    for user in content:
        personalites.append(user[0], (get_personality(user[1])))


main()
