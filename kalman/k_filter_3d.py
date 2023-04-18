import numpy as np
import filterpy.kalman
import filterpy.common
import matplotlib.pyplot as plt
from traj_gen import traj_generation

acc_hz = 50
pos_hz = 1
dt = 1/acc_hz
k = int(acc_hz/pos_hz)

samples_count = 5000
acc_noise_sigma = 0.01
xy_noise_sigma = 0.5
z_noise_sigma = 0.5
model_sigma = 1e-4

# acc/pos data generation
acc_measured, pos_measured = traj_generation(samples_count, acc_noise_sigma, xy_noise_sigma, acc_hz, pos_hz)

# KF for X coord
filter_x = filterpy.kalman.KalmanFilter(dim_x=3,
                                        dim_z=2)
filter_x.F = np.array([[1,   dt,     (dt**2)/2],
                       [0,   1.0,    dt],
                       [0,   0,      1.0]])
filter_x.H = np.array([[0.0, 0.0, 1.0],
                       [1.0, 0.0, 0.0]])
filter_x.Q = filterpy.common.Q_discrete_white_noise(dim=3, dt=dt, var=model_sigma)
filter_x.R = np.array([[acc_noise_sigma**2, 0],
                       [0, xy_noise_sigma**2]])
filter_x.x = np.array([0.0, 0.0, 0.0])
filter_x.P = np.array([[2.0,  0.0, 0.0],
                       [0.0,  2.0, 0.0],
                       [0.0,  0.0, 2.0]])

# KF for Y coord
filter_y = filterpy.kalman.KalmanFilter(dim_x=3,      # Размер вектора стостояния
                                        dim_z=2)      # Размер вектора измерений
filter_y.F = np.array([[1,   dt,     (dt**2)/2],
                       [0,   1.0,    dt],
                       [0,   0,      1.0]])
filter_y.H = np.array([[0.0, 0.0, 1.0],
                       [1.0, 0.0, 0.0]])
filter_y.Q = filterpy.common.Q_discrete_white_noise(dim=3, dt=dt, var=model_sigma)
filter_y.R = np.array([[acc_noise_sigma**2, 0],
                       [0, xy_noise_sigma**2]])
filter_y.x = np.array([0.0, 0.0, 0.0])
filter_y.P = np.array([[2.0,  0.0, 0.0],
                       [0.0,  2.0, 0.0],
                       [0.0,  0.0, 2.0]])

# KF for Z coord
filter_z = filterpy.kalman.KalmanFilter(dim_x=3,      # Размер вектора стостояния
                                        dim_z=2)      # Размер вектора измерений
filter_z.F = np.array([[1,   dt,     (dt**2)/2],
                       [0,   1.0,    dt],
                       [0,   0,      1.0]])
filter_z.H = np.array([[0.0, 0.0, 1.0],
                       [1.0, 0.0, 0.0]])
filter_z.Q = filterpy.common.Q_discrete_white_noise(dim=3, dt=dt, var=model_sigma)
filter_z.R = np.array([[acc_noise_sigma**2, 0],
                       [0, z_noise_sigma**2]])
filter_z.x = np.array([0.0, 0.0, 0.0])
filter_z.P = np.array([[2.0,  0.0, 0.0],
                       [0.0,  2.0, 0.0],
                       [0.0,  0.0, 2.0]])


filteredState = []

pos0 = np.array([0.0, 0.0, 0.0])
position = np.zeros((samples_count, 3))
for i in range(samples_count):
    if i % k < 0.01:
        position[i] = pos_measured[i]
    else:
        position[i] = position[i-1]

# FOR KF
for i in range(0, len(acc_measured)):
    # measuring
    z_x = np.array([acc_measured[i, 0], position[i, 0]])
    z_y = np.array([acc_measured[i, 1], position[i, 1]])
    z_z = np.array([acc_measured[i, 2], position[i, 2]])
    # prediction
    filter_x.predict()
    filter_y.predict()
    filter_z.predict()
    # correction
    filter_x.update(z_x)
    filter_y.update(z_y)
    filter_z.update(z_z)
    # linear cords
    filteredState.append([filter_x.x[0], filter_y.x[0], filter_z.x[0]])

filteredState = np.array(filteredState)


# plotting
fig, axs = plt.subplots(3, sharex=True)
fig.suptitle('Kalman filter')
axs[0].set_title('X coords')
axs[0].grid(True)
axs[0].plot(pos_measured[:, 0], label="Measured pose full", color="#99AAFF")
axs[0].plot(position[:, 0], label="Measured pose 1 hz", color="#FF6633")
axs[0].plot(filteredState[:, 0], label="Filter estimation", color="#224411")

axs[1].set_title('Y coords')
axs[1].grid(True)
axs[1].plot(pos_measured[:, 1], label="Measured pose full", color="#99AAFF")
axs[1].plot(position[:, 1], label="Measured pose 1 hz", color="#FF6633")
axs[1].plot(filteredState[:, 1], label="Filter estimation", color="#224411")

axs[2].set_title('Z coords')
axs[2].grid(True)
axs[2].plot(pos_measured[:, 2], label="Measured pose full", color="#99AAFF")
axs[2].plot(position[:, 2], label="Measured pose 1 hz", color="#FF6633")
axs[2].plot(filteredState[:, 2], label="Filter estimation", color="#224411")


# plt.title("Pose data, axis X")
# plt.plot(pos_measured[:, 0], label="Measured pose full", color="#99AAFF")
# plt.plot(position[:, 0], label="Measured pose 1 hz", color="#FF6633")
# # plt.plot(acc_measured, label="Measured acc", color="#99AAFF")
# # plt.plot(acceleration, label="True acceleration", color="#FF6633")
# # plt.plot(filteredState[:, 0], label="Оценка фильтра", color="#224411")
# plt.plot(filteredState[:, 0], label="Filter estimation", color="#224411")
# plt.legend()
plt.show()

