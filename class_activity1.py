def compute_data(a, b, c):
    return (-b + (b ** 2 - 4 * a * c) ** (1/2)) / (2 * a)

def test_data():
    # declare test data
    data = []
    data.append([22, 66, 9, -0.14319894940006364])
    data.append([9, 1, 4, -0.05555555555555551+0.6643478190611888j])

    # run tests
    for test in data:
        print(compute_data(test[0], test[1], test[2]) == test[3])

test_data()

