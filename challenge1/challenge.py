def update_matrix(matrix, indexes, value):
    matrix[int(indexes[0]) - 1][int(indexes[1]) - 1][int(indexes[2]) - 1] = int(value)
    return matrix


def query_matrix(matrix, indexes):
    x = range(int(indexes[0]) - 1, int(indexes[3]))
    y = range(int(indexes[1]) - 1, int(indexes[4]))
    z = range(int(indexes[2]) - 1, int(indexes[5]))
    value = 0
    for i in x:
        for j in y:
            for k in z:
                value += matrix[i][j][k]
    return value


def generate_matrix(n):
    n = int(n)
    matrix = [[[0 for i in range(n)] for j in range(n)] for k in range(n)]
    return matrix


def run_cases():
    tests_cases = int(input())
    for test_case in range(tests_cases):
        n, m = str(input()).split(" ")
        matrix = generate_matrix(n)
        for test_case in range(int(m)):
            operation, *index, value = str(input()).split(" ")
            if operation == "UPDATE":
                matrix = update_matrix(matrix, index, value)
            elif operation == "QUERY":
                index.append(value)
                query = query_matrix(matrix, index)
                print(query)


if __name__ == "__main__":
    run_cases()
