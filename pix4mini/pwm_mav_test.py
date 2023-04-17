import time

import numpy as np
from pymavlink import mavutil

port = "/dev/ttyACM0"
master = mavutil.mavlink_connection(port, baud=115200)


def motor_test(conn):
    conn.mav.command_long_send(
        conn.target_system,
        conn.target_component,
        mavutil.mavlink.MAV_CMD_DO_MOTOR_TEST,
        1,              # motor instance
        1,              # throttle test type 1 - PWM
        1000,           # throttle value
        0,              # timeout
        0,              # motor count
        0,              # test order
        0               # empty
    )


# # connection.mav.send_servo_pwm(5, 1500)
# connection.mav.rc_channels_override_send(connection.target_system, connection.target_component, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500)
# connection.mav.mav_cmd_do_set_servo_send(5, 1800)


# def set_rc_channel_pwm(channel_id, pwm=1500):
#     """ Set RC channel pwm value
#     Args:
#         channel_id (TYPE): Channel ID
#         pwm (int, optional): Channel pwm value 1100-1900
#     """
#     if channel_id < 1 or channel_id > 18:
#         print("Channel does not exist.")
#         return
#
#     # Mavlink 2 supports up to 18 channels:
#     # https://mavlink.io/en/messages/common.html#RC_CHANNELS_OVERRIDE
#     rc_channel_values = [65535 for _ in range(18)]
#     rc_channel_values[channel_id - 1] = pwm
#     master.mav.rc_channels_override_send(
#         master.target_system,                # target_system
#         master.target_component,             # target_component
#         *rc_channel_values)                  # RC channel list, in microseconds.
#
#
# set_rc_channel_pwm(5, 1600)

# master.mav.manual_control_send(
#     master.target_system,
#     500,
#     350,
#     300,
#     500,
#     400,
#     300)
#
# def set_servo_pwm(servo_n, microseconds):
#     """ Sets AUX 'servo_n' output PWM pulse-width.
#
#     Uses https://mavlink.io/en/messages/common.html#MAV_CMD_DO_SET_SERVO
#
#     'servo_n' is the AUX port to set (assumes port is configured as a servo).
#         Valid values are 1-3 in a normal BlueROV2 setup, but can go up to 8
#         depending on Pixhawk type and firmware.
#     'microseconds' is the PWM pulse-width to set the output to. Commonly
#         between 1100 and 1900 microseconds.
#
#     """
#     # master.set_servo(servo_n+8, microseconds) or:
#     master.mav.command_long_send(
#         master.target_system, master.target_component,
#         mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
#         0,            # first transmission of this command
#         servo_n + 8,  # servo instance, offset by 8 MAIN outputs
#         microseconds, # PWM pulse-width
#         0,0,0,0,0     # unused parameters
#     )

#
# for us in range(1100, 1900, 50):
#     set_servo_pwm(3, us)
#     time.sleep(0.125)
