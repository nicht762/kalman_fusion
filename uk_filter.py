import numpy as np
import filterpy.kalman
import filterpy.common
import matplotlib.pyplot as plt
from traj_gen import traj_generation


acc_hz = 50
pos_hz = 1
dt = 1/acc_hz
k = int(acc_hz/pos_hz)

samples_count = 2000
acc_noise_sigma = 0.01
pos_noise_sigma = 0.7
model_sigma = 1e-4

acc_measured, pos_measured = traj_generation(samples_count, acc_noise_sigma, pos_noise_sigma, acc_hz, pos_hz)


# Функция наблюдения - аналог матрицы наблюдения
# Преобразует вектор состояния x в вектор измерений z
def measurement_function(x):
    return np.array([x[2], x[0]])


# Функция процесса - аналог матрицы процесса / matrix A - state transition matrix
def state_transition_function(x, dt):
    new_state = np.zeros(3)
    new_state[0] = x[0] + dt * x[1] + ((dt**2)/2) * x[2]
    new_state[1] = x[1] + dt * x[2]
    new_state[2] = x[2]
    return new_state


# unscented kalman filter
points = filterpy.kalman.JulierSigmaPoints(3, kappa=0)
filter = filterpy.kalman.UnscentedKalmanFilter(dim_x=3,
                                               dim_z=2,
                                               dt=dt,
                                               hx=measurement_function,
                                               fx=state_transition_function,
                                               points=points)

# Ковариационная матрица ошибки модели
# описывает насколько точно модель соответствует реальности
filter.Q = filterpy.common.Q_discrete_white_noise(dim=3, dt=dt, var=model_sigma)
# Ковариационная матрица ошибки измерения - диаг по кол-ву измеряемых величин
# измеряем ускорение - вписываем сигму ускорения
filter.R = np.array([[acc_noise_sigma**2, 0],
                     [0, pos_noise_sigma**2]])
# filter.R = np.array([[pos_noise_sigma**2]])
# Начальное состояние. x, x', x"
filter.x = np.array([0.0, 0.0, 0.0])
# Ковариационная матрица для начального состояния
# диагональная по размеру вектора, сама обновляется - не паримся
filter.P = np.array([[5.0,  0.0, 0.0],
                     [0.0,  5.0, 0.0],
                     [0.0,  0.0, 5.0]])

pos0 = np.array([0.0, 0.0, 0.0])
position = np.zeros((samples_count, 3))
for i in range(samples_count):
    if i % k < 0.01:
        position[i] = pos_measured[i]
    else:
        position[i] = position[i-1]

filteredState = []

# FOR UKF
for i in range(samples_count):
    z = np.array([acc_measured[i, 0], position[i, 0]])
    filter.predict()
    filter.update(z)
    filteredState.append(filter.x)

filteredState = np.array(filteredState)

# plotting
plt.title("Pose data, axis X")
plt.plot(pos_measured[:, 0], label="Measured pose full", color="#99AAFF")
plt.plot(position[:, 0], label="Measured pose 1 hz", color="#FF6633")
# plt.plot(acc_measured, label="Measured acc", color="#99AAFF")
# plt.plot(acceleration, label="True acceleration", color="#FF6633")
# plt.plot(filteredState[:, 0], label="Оценка фильтра", color="#224411")
plt.plot(filteredState[:, 0], label="Filter estimation", color="#224411")
plt.legend()
plt.show()

