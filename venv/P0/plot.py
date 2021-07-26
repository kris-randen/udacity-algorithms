def plot(n, t, loglog, interpolation):
    from matplotlib import pyplot as plt

    interpolated = list(map(interpolation, n))
    # ci = 1/1.2e-6
    ci = interpolated[0]/0.6
    interpolated = list(map(lambda x: x/ci, interpolated))

    ca = t[0]
    t = list(map(lambda x: x/ca, t))
    # plotting the points
    plt.plot(n, t, color='k', label='actual')
    plt.plot(n, interpolated, color='r', label='interpolated')
    plt.legend()

    if loglog:
        plt.loglog(n, t)
        plt.loglog(n, interpolated)
    # naming the x axis
    plt.xlabel('input size (n)')
    # naming the y axis
    plt.ylabel('run time')

    # giving a title to my graph
    plt.title('time complexity')

    # function to show the plot
    plt.show()
