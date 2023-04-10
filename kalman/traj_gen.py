import numpy as np


def traj_generation(samples_count, acc_noise_sigma, pos_noise_sigma, acc_hz, pos_hz):

    dt = 1/acc_hz
    # k = int(acc_hz/pos_hz)

    # accel gen
    acceleration = np.zeros((samples_count, 3))
    acc_noise = np.random.normal(0.0, scale=acc_noise_sigma, size=(samples_count, 3))
    for i in range(samples_count):
        acceleration[i][0] = 0.05 * np.sin(i / ((samples_count / 2) / np.pi))
    acc_measured = acceleration + acc_noise

    # pose gen
    velocity = np.zeros((samples_count, 3))
    position = np.zeros((samples_count, 3))
    pos_noise = np.random.normal(0.0, scale=pos_noise_sigma, size=(samples_count, 3))
    for i in range(1, samples_count):
        velocity[i] = velocity[i - 1] + acceleration[i] * dt
        position[i] = position[i - 1] + velocity[i] * dt + (acceleration[i] * dt ** 2) / 2.0
    pos_measured = position + pos_noise

    # pos0 = np.array([0.0, 0.0, 0.0])
    # for i in range(len(pos_measured)):
    #     if i % k > 0.01:
    #         pos_measured[i] = pos0

    # pos_measured[int(len(pos_measured) / 2):int(len(pos_measured) / 2) + 20, 0] += 10

    return acc_measured, pos_measured

