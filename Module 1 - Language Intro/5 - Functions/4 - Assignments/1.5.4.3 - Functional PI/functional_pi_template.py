import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

    ### YOUR CODE HERE ###

    # initial values for the Gauss-Legendre algorithm
    a = 1.0
    b = 1.0 / math.sqrt(2)
    t = 1.0 / 4
    p = 1.0

    pi_estimate = (a + b) ** 2 / (4 * t)

    # keep iterating until successive estimates agree to within the target error.
    # the iteration cap guards against an unreachable target (e.g. below float precision)
    for _ in range(100):
        # compute the new a first, but keep the old a around since b and t need it
        a_next = (a + b) / 2
        b = math.sqrt(a * b)
        t = t - p * (a - a_next) ** 2
        p = 2 * p
        a = a_next

        new_estimate = (a + b) ** 2 / (4 * t)
        change = abs(new_estimate - pi_estimate)
        pi_estimate = new_estimate

        if change < abs(target_error):
            break

    return pi_estimate




desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
