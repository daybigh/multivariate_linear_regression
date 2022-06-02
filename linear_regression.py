def parseData(data):
    Y = []
    X = [[1] for _ in range(len(data))]
    for i, point in enumerate(data):
        X[i] += data[i][:-1]
        Y.append(data[i][-1])
    return (X, Y)


def lm(x, beta):
    """multivariate linear model with beta coefficients"""
    n = len(x)
    yhat = 0
    for i in range(n):
        yhat += x[i] * beta[i]
    return yhat


def mse(X, Y, beta):
    """mean squared error loss function"""
    n = len(X)
    error = 0
    for i in range(n):
        error += (Y[i] - lm(X[i], beta)) ** 2
    return error / n


def mseprime(X, Y, beta, j):
    """partial derivative of mse function with respect to beta[j]"""
    n = len(X)
    errorp = 0

    for i in range(n):
        errorp += (Y[i] - lm(X[i], beta)) * X[i][j]

    return (2 / n) * errorp


def gd(X, Y, epoc, alpha):
    """gradient descent algorithm"""
    n = len(X[0])
    temp = [0 for _ in range(n)]
    b = [0 for _ in range(n)]

    for i in range(epoc):
        for j in range(n):
            temp[j] = b[j] + alpha * mseprime(X, Y, b, j)
        for k in range(n):
            b[k] = temp[k]
    return b


data = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

X = parseData(data)[0]
Y = parseData(data)[1]


print(gd(X, Y, 1000, 0.01))
