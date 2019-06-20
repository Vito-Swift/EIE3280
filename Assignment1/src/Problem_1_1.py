import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

iteration_time = 10
powers = [1, 1, 1]
target_sir = [1, 1.5, 1]
current_sir = [0, 0, 0]
tmatrix = [
    [1, 0.1, 0.3],
    [0.2, 1, 0.3],
    [0.2, 0.2, 1]
]
_tmatrix = [
    [1, 0.1, 0.3, 0.1],
    [0.2, 1, 0.3, 0.1],
    [0.2, 0.2, 1, 0.1],
    [0.1, 0.1, 0.1, 1]
]
noise = 0.1


def update_sir():
    global current_sir
    for i in range(len(powers)):
        interference = 0
        for j in range(len(powers)):
            if j != i:
                interference += tmatrix[i][j] * powers[j]
        current_sir[i] = tmatrix[i][i] * powers[i] / (interference + noise)


def update_powers(l=3):
    global powers
    next_powers = [0 for i in range(l)]
    for i in range(len(powers)):
        next_powers[i] = powers[i] * target_sir[i] / current_sir[i]
    powers = next_powers


def plot(pr, sr, pr_, sr_):
    gs = gridspec.GridSpec(3, 2)
    fig = plt.figure(tight_layout=True, figsize=(15, 12))
    p1 = fig.add_subplot(gs[0, 0])
    p2 = fig.add_subplot(gs[0, 1])
    p3 = fig.add_subplot(gs[1, :])
    p4 = fig.add_subplot(gs[2, :])

    x1 = np.arange(iteration_time + 1)
    p1.plot(x1, [p[0] for p in pr], label="transmitter 1")
    p1.plot(x1, [p[1] for p in pr], label="transmitter 2")
    p1.plot(x1, [p[2] for p in pr], label="transmitter 3")
    p1.legend()
    p1.set_xlabel("Iteration Time (a)")
    p1.set_ylabel("Power (mW)")

    p2.plot(x1, [p[0] for p in sr], label="transmitter 1")
    p2.plot(x1, [p[1] for p in sr], label="transmitter 2")
    p2.plot(x1, [p[2] for p in sr], label="transmitter 3")
    p2.legend()
    p2.set_xlabel("Iteration Time (a)")
    p2.set_ylabel("SIR")

    x1_ = np.arange(2 * iteration_time + 1)
    x2_ = np.arange(10, 2 * iteration_time + 1)
    x2_s = np.arange(11, 2 * iteration_time + 1)
    p3.plot(x1_, [p[0] for p in pr_], label="transmitter 1")
    p3.plot(x1_, [p[1] for p in pr_], label="transmitter 2")
    p3.plot(x1_, [p[2] for p in pr_], label="transmitter 3")
    p3.plot(x2_, [p[3] for p in pr_[iteration_time:]], label="transmitter 4")
    p3.legend()
    p3.set_xlabel("Iteration Time (b)")
    p3.set_ylabel("Power (mW)")

    p4.plot(x1_, [p[0] for p in sr_], label="transmitter 1")
    p4.plot(x1_, [p[1] for p in sr_], label="transmitter 2")
    p4.plot(x1_, [p[2] for p in sr_], label="transmitter 3")
    p4.plot(x2_s, [p[3] for p in sr_[iteration_time + 1:]], label="transmitter 4")
    p4.legend()
    p4.set_xlabel("Iteration Time (b)")
    p4.set_ylabel("SIR")

    plt.show()


def main():
    global tmatrix

    power_result = [[p for p in powers]]
    sir_result = []
    for i in range(iteration_time):
        update_sir()
        update_powers()
        sir_result.append([s for s in current_sir])
        power_result.append([p for p in powers])
    update_sir()
    sir_result.append([s for s in current_sir])

    tmatrix = _tmatrix
    target_sir.append(1)
    _power_result = [p for p in power_result]
    _sir_result = [s for s in sir_result[:-1]]
    _power_result[-1].append(1)
    powers.append(1)
    current_sir.append(1)
    update_sir()
    _sir_result.append([s for s in current_sir])
    for i in range(iteration_time):
        update_sir()
        update_powers(l=4)
        _sir_result.append([s for s in current_sir])
        _power_result.append([p for p in powers])
    plot(power_result, sir_result, _power_result, _sir_result)


if __name__ == '__main__':
    main()
