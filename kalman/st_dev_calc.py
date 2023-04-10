import numpy as np

acc_file = '../data/acc_unc_5k_dt01.txt'
rpy_file = '../data/rpy_unc_5k_dt01_2.txt'


def st_dev_calc(data):
    st_devs = data.std(axis=0)
    print(st_devs)
    return st_devs


def main():
    data = np.loadtxt(acc_file, usecols=(1, 2, 3), dtype='float')
    st_dev_calc(data)
    data = np.loadtxt(rpy_file, usecols=(1, 2, 3), dtype='float')
    st_dev_calc(data)


if __name__ == '__main__':
    main()

