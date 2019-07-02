from  matplotlib import pyplot as plt
import csv
from random import randint


filename = "StudentsPerformance.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    male, female = [], []
    num_of_males = 0
    num_of_females = 0
    for row in reader:
        if row[0] == "male":
            male.append(int(row[6]))
            num_of_males += 1
        elif row[0] == "female":
            female.append(int(row[6]))
            num_of_females += 1
        else:
            print(row[0])
    print(num_of_females)

    sub = num_of_females-num_of_males
    print(sub)
    while sub >= 1:
        numero = int(randint(0, num_of_females))
        del female[numero]
        sub -= 1
        num_of_females -= 1

    print(num_of_males)
    print(len(male))
    print(num_of_females)
    print(len(female))

    male.sort()
    female.sort()
    print(male)
    print(female)
    plt.plot(range(num_of_males), male, c="blue")
    plt.plot(range(num_of_females), female, c="red")
    plt.fill_between(range(int(num_of_males)), female, male, facecolor="blue", alpha=0.5)

    plt.title("Difference between results for women and men", fontsize = 20)
    plt.ylabel("Result in percents")
    plt.xlabel("Red line are women, blue - Men")
    plt.show()