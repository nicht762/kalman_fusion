import numpy as np

acc_file = '../data/acc_unc_5k_dt01.txt'
rpy_file = '../data/rpy_unc_5k_dt01_2.txt'
mag_file = '../data/mag_unc_5k_dt01.txt'

# rov_imu = ['../data/static_rov/imu_data_11040x.txt',
#            '../data/static_rov/imu_data_11040y.txt',
#            '../data/static_rov/imu_data_11040z.txt',
#            '../data/static_rov/imu_data_110401.txt',
#            '../data/static_rov/imu_data_110402.txt',
#            '../data/static_rov/imu_data_110403.txt']

rov_imu = ['../data/static_rov/imu_data_ow.txt',
           '../data/static_rov/imu_data_iw1.txt',
           '../data/static_rov/imu_data_iw2.txt']


def st_dev_calc(data):
    st_devs = data.std(axis=0)
    with np.printoptions(precision=5, suppress=True):
        print(st_devs)
    return st_devs


def exp_val_calc(data):
    exp_vals = data.mean(axis=0)
    with np.printoptions(precision=5, suppress=True):
        print(exp_vals)
    return exp_vals


def g_norm_calc(data):
    g_acc = data[:, 3:6]
    # print(g_acc)
    g_norm = np.linalg.norm(g_acc, ord=2, axis=1)
    # print(g_norm)
    exp_val_calc(g_norm)


def main():
    # FROM MY IMU
    # data = np.loadtxt(acc_file, usecols=(1, 2, 3), dtype='float')
    # print('accels')
    # st_dev_calc(data)
    # data = np.loadtxt(rpy_file, usecols=(1, 2, 3), dtype='float')
    # print('rpy')
    # st_dev_calc(data)
    # data = np.loadtxt(mag_file, usecols=(1, 2, 3), dtype='float')
    # print('mag')
    # st_dev_calc(data)

    # FROM ROV
    # r, p, y, ax, ay, az
    for imu_data in rov_imu:
        data = np.loadtxt(imu_data, usecols=(0, 1, 2, 3, 4, 5), dtype='float')
        # st_dev_calc(data)
        exp_val_calc(data)
        # eucl_g = np.linalg.norm(exp_val_calc(data)[3:6], ord=2)
        # print(eucl_g)
        # g_norm_calc(data)


if __name__ == '__main__':
    main()

