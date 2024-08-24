# codes make you happy
import novapi
from mbuild.encoder_motor import encoder_motor_class
from mbuild import gamepad
from mbuild import power_manage_module
from mbuild.smartservo import smartservo_class
from mbuild.smart_camera import smart_camera_class
from mbuild.servo_driver import servo_driver_class
from mbuild.ranging_sensor import ranging_sensor_class
from mbuild import power_expand_board
import mbuild

# initialize variables
mode = 0
mode_change = 0
max_servo1 = 0
up_down = 0
pick = 0
time_move = 0
go_to_0_6 = 0
brushless = 0
on_off_reload = 0
Lcalibeate = 0
Rcailbrate = 0
timer_rotage = 0
auto_on_off = 0
brushless_auto = 0

# new class
encoder_motor_M1 = encoder_motor_class("M1", "INDEX1")
encoder_motor_M3 = encoder_motor_class("M3", "INDEX1")
encoder_motor_M4 = encoder_motor_class("M4", "INDEX1")
encoder_motor_M2 = encoder_motor_class("M2", "INDEX1")
smartservo_1 = smartservo_class("M6", "INDEX1")
smartservo_2 = smartservo_class("M6", "INDEX2")
smartservo_3 = smartservo_class("M6", "INDEX4")
smartservo_4 = smartservo_class("M6", "INDEX3")
smart_camera_1 = smart_camera_class("PORT5", "INDEX1")
servo_driver_1 = servo_driver_class("PORT3", "INDEX1")
ranging_sensor_3 = ranging_sensor_class("PORT3", "INDEX3")
ranging_sensor_2 = ranging_sensor_class("PORT3", "INDEX2")
ranging_sensor_1 = ranging_sensor_class("PORT3", "INDEX1")
encoder_motor_M5 = encoder_motor_class("M5", "INDEX1")

def mode_4 ():
    encoder_motor_M1.set_speed(-1 * ((speed + ((ranging_sensor_1.get_distance() - Rcailbrate)) * error)))
    encoder_motor_M3.set_speed((speed - ((ranging_sensor_1.get_distance() - Rcailbrate)) * error))
    encoder_motor_M4.set_speed((speed + ((ranging_sensor_2.get_distance() - Lcalibeate)) * error))
    encoder_motor_M2.set_speed(-1 * ((speed - ((ranging_sensor_2.get_distance() - Lcalibeate)) * error)))

def move_25_mode_2 ():
    encoder_motor_M4.set_power(-1 * ((((gamepad.get_joystick("Ry") + 100)) / 200) * ((((gamepad.get_joystick("Ly") - gamepad.get_joystick("Lx"))) + gamepad.get_joystick("Rx")))))
    encoder_motor_M3.set_power((((gamepad.get_joystick("Ry") + 100)) / 200) * ((((gamepad.get_joystick("Ly") + gamepad.get_joystick("Lx"))) - gamepad.get_joystick("Rx"))))
    encoder_motor_M2.set_power(-1 * ((((gamepad.get_joystick("Ry") + 100)) / 200) * ((((gamepad.get_joystick("Ly") + gamepad.get_joystick("Lx"))) + gamepad.get_joystick("Rx")))))
    encoder_motor_M1.set_power((((gamepad.get_joystick("Ry") + 100)) / 200) * ((((gamepad.get_joystick("Ly") - gamepad.get_joystick("Lx"))) - gamepad.get_joystick("Rx"))))

def move_25_mode__1 ():
    encoder_motor_M4.set_power((((gamepad.get_joystick("Ry") + 100)) / 200) * ((((gamepad.get_joystick("Ly") - gamepad.get_joystick("Lx"))) - gamepad.get_joystick("Rx"))))
    encoder_motor_M3.set_power(-1 * ((((gamepad.get_joystick("Ry") + 100)) / 200) * ((((gamepad.get_joystick("Ly") + gamepad.get_joystick("Lx"))) + gamepad.get_joystick("Rx")))))
    encoder_motor_M2.set_power((((gamepad.get_joystick("Ry") + 100)) / 200) * ((((gamepad.get_joystick("Ly") + gamepad.get_joystick("Lx"))) - gamepad.get_joystick("Rx"))))
    encoder_motor_M1.set_power((-1 * (((gamepad.get_joystick("Ry") + 100)) / 200)) * ((((gamepad.get_joystick("Ly") - gamepad.get_joystick("Lx"))) + gamepad.get_joystick("Rx"))))

def move_right_sensor_N_N (speed, error):
    encoder_motor_M1.set_speed(-1 * ((speed + ((ranging_sensor_1.get_distance() - Rcailbrate)) * error)))
    encoder_motor_M3.set_speed((speed - ((ranging_sensor_1.get_distance() - Rcailbrate)) * error))
    encoder_motor_M4.set_speed((speed + ((ranging_sensor_2.get_distance() - Lcalibeate)) * error))
    encoder_motor_M2.set_speed(-1 * ((speed - ((ranging_sensor_2.get_distance() - Lcalibeate)) * error)))

def calibrate ():
    smartservo_1.set_power(20)
    time.sleep(0.1)
    while not smartservo_1.get_value("speed") < 0.5:
        pass

    smartservo_1.set_power(0)
    max_servo1 = smartservo_1.get_value("angle")
    smartservo_3.set_power(-20)
    time.sleep(0.1)
    while not smartservo_3.get_value("speed") < 0.5:
        pass

    smartservo_3.set_power(0)
    smartservo_4.set_power(20)
    time.sleep(0.1)
    while not smartservo_4.get_value("speed") < 0.5:
        pass

    smartservo_4.set_power(0)

def move_left_sensor_N_N (speed, error):
    encoder_motor_M1.set_speed((speed - ((ranging_sensor_1.get_distance() - Rcailbrate)) * error))
    encoder_motor_M3.set_speed(-1 * ((speed + ((ranging_sensor_1.get_distance() - Rcailbrate)) * error)))
    encoder_motor_M4.set_speed(-1 * ((speed - ((ranging_sensor_2.get_distance() - Lcalibeate)) * error)))
    encoder_motor_M2.set_speed((speed + ((ranging_sensor_2.get_distance() - Lcalibeate)) * error))

def stop_encode ():
    encoder_motor_M1.set_speed(0)
    encoder_motor_M2.set_speed(0)
    encoder_motor_M3.set_speed(0)
    encoder_motor_M4.set_speed(0)

def go_to_up ():
    smartservo_1.move_to((max_servo1 - 110), 50)
    up_down = 0
    time.sleep(0.2)

def go_to_pick ():
    smartservo_1.move_to((max_servo1 - 300), 50)
    up_down = 1
    time.sleep(0.2)

def go_to_down ():
    smartservo_1.move_to((max_servo1 - 720), 50)
    up_down = 1
    time.sleep(0.2)

def auto_mode ():
    while not (smart_camera_1.detect_sign(1) or gamepad.is_key_pressed("N1") or not auto_on_off == 1):
        time.sleep(0.001)
        go_to_up()
        move_right_sensor_N_N(125, 7)

    encoder_motor_M1.set_speed(0)
    encoder_motor_M2.set_speed(0)
    encoder_motor_M3.set_speed(0)
    encoder_motor_M4.set_speed(0)
    while not (smart_camera_1.get_sign_x(1) > 110 and smart_camera_1.get_sign_x(1) < 190 and smart_camera_1.get_sign_y(1) > 70 or gamepad.is_key_pressed("N1") or not auto_on_off == 1):
        time.sleep(0.001)
        if not smart_camera_1.detect_sign(1):
            move_right_sensor_N_N(50, 3)

        else:
            if smart_camera_1.get_sign_x(1) < 110:
                move_left_sensor_N_N(50, 3)

            else:
                if smart_camera_1.get_sign_x(1) > 190:
                    move_right_sensor_N_N(50, 3)

                else:
                    encoder_motor_M1.set_speed(-40)
                    encoder_motor_M2.set_speed(40)
                    encoder_motor_M3.set_speed(-40)
                    encoder_motor_M4.set_speed(40)

    if not gamepad.is_key_pressed("N1") or auto_on_off == 1:
        encoder_motor_M1.set_speed(0)
        encoder_motor_M2.set_speed(0)
        encoder_motor_M3.set_speed(0)
        encoder_motor_M4.set_speed(0)
        go_to_pick()
        time.sleep(1)
        smartservo_3.set_power(8)
        smartservo_4.set_power(-8)
        time.sleep(0.5)
        go_to_up()
        time.sleep(1)
        encoder_motor_M1.move(1300, 250)
        encoder_motor_M2.move(-1300, 250)
        encoder_motor_M3.move(1300, 250)
        encoder_motor_M4.move(-1300, 250)
        time.sleep(0.2)
        timer_rotage = (novapi.timer() + 0.7)
        while not (novapi.timer() > timer_rotage or gamepad.is_key_pressed("N1") or not auto_on_off == 1):
            time.sleep(0.001)
            encoder_motor_M1.set_speed(-250)
            encoder_motor_M2.set_speed(-250)
            encoder_motor_M3.set_speed(-250)
            encoder_motor_M4.set_speed(-250)

        encoder_motor_M1.set_speed(0)
        encoder_motor_M2.set_speed(0)
        encoder_motor_M3.set_speed(0)
        encoder_motor_M4.set_speed(0)
        smartservo_3.set_power(-8)
        smartservo_4.set_power(8)
        timer_rotage = (novapi.timer() + 0.9)
        while not (novapi.timer() > timer_rotage or gamepad.is_key_pressed("N1") or not auto_on_off == 1):
            time.sleep(0.001)
            encoder_motor_M1.set_speed(250)
            encoder_motor_M2.set_speed(250)
            encoder_motor_M3.set_speed(250)
            encoder_motor_M4.set_speed(250)

        smartservo_3.set_power(0)
        smartservo_4.set_power(0)
        encoder_motor_M1.set_speed(0)
        encoder_motor_M2.set_speed(0)
        encoder_motor_M3.set_speed(0)
        encoder_motor_M4.set_speed(0)

def code_all_ma ():

    mode = 1
    mode_change = 0
    Lcalibeate = 8.4
    Rcailbrate = 11.4
    auto_on_off = 1
    calibrate()
    while True:
        time.sleep(0.001)
        if mode == 1:
            move_25_mode__1()
            mode_1()

        else:
            if mode == 2:
                mode_2()
                move_25_mode_2()

            else:
                if mode == 4:
                    encoder_motor_M1.set_power(0)
                    encoder_motor_M2.set_power(0)
                    encoder_motor_M3.set_power(0)
                    encoder_motor_M4.set_power(0)

                else:
                    if mode == 3:
                        if gamepad.is_key_pressed("N1"):
                            auto_on_off = 0

                        else:
                            if gamepad.is_key_pressed("N3"):
                                auto_on_off = 1

                            else:
                                if auto_on_off == 1:
                                    auto_mode()

                                else:
                                    encoder_motor_M1.set_speed(0)
                                    encoder_motor_M2.set_speed(0)
                                    encoder_motor_M3.set_speed(0)
                                    encoder_motor_M4.set_speed(0)

                    else:
                        pass

        if gamepad.is_key_pressed("≡"):
            mode_change = 0
            time.sleep(0.2)
            while not (not mode_change == 0):
                time.sleep(0.001)
                if gamepad.is_key_pressed("N1"):
                    mode = 1
                    mode_change = 1

                if gamepad.is_key_pressed("N2"):
                    mode = 2
                    mode_change = 1

                if gamepad.is_key_pressed("N3"):
                    mode = 3
                    mode_change = 1

                if gamepad.is_key_pressed("+"):
                    smart_camera_1.open_light()
                    Lcalibeate = ranging_sensor_2.get_distance()
                    Rcailbrate = ranging_sensor_1.get_distance()
                    time.sleep(1)
                    smart_camera_1.close_light()
                    mode_change = 1

                if gamepad.is_key_pressed("L1"):
                    smart_camera_1.learn(1, "until_button")
                    mode_change = 1

                if gamepad.is_key_pressed("L1"):
                    smart_camera_1.reset()
                    mode_change = 1

                if gamepad.is_key_pressed("R2"):
                    calibrate()
                    mode_change = 1

                if gamepad.is_key_pressed("Down"):
                    smart_camera_1.close_light()
                    mode_change = 1

                if gamepad.is_key_pressed("Up"):
                    smart_camera_1.open_light()
                    mode_change = 1

                if gamepad.is_key_pressed("N4"):
                    mode = 4
                    mode_change = 1

def code_all_auto ():
    

    encoder_motor_M5.set_power(50)
    power_expand_board.set_power("DC2", 100)
    mode = 2
    mode_change = 0
    Lcalibeate = 8.4
    Rcailbrate = 11.4
    auto_on_off = 1
    calibrate()
    test_code()
    while True:
        time.sleep(0.001)
        auto_mode()

def mode_1 ():
    
    """โหมดคีบ"""
    # คีบ,คาย
    if gamepad.is_key_pressed("N3"):
        if pick == 1:
            smartservo_3.set_power(-8)
            smartservo_4.set_power(8)
            pick = 0
            time_move = (novapi.timer() + 0.7)
            go_to_0_6 = 1
            time.sleep(0.2)

        else:
            smartservo_3.set_power(8)
            smartservo_4.set_power(-8)
            pick = 1
            go_to_0_6 = 0
            time.sleep(0.2)

    else:
        pass

    if go_to_0_6 == 1 and novapi.timer() > time_move:
        smartservo_3.set_power(0)
        smartservo_4.set_power(0)
        go_to_0_6 = 0

    else:
        pass

    # คีบกล่องที่พื้น
    if gamepad.is_key_pressed("R1"):
        if up_down == 1:
            go_to_up()

        else:
            go_to_down()

    else:
        # คีบกล่องตรงกลาง
        if gamepad.is_key_pressed("L1"):
            if up_down == 1:
                go_to_up()

            else:
                go_to_pick()

        else:
            if gamepad.is_key_pressed("Up"):
                smartservo_1.set_power(20)
                while not not gamepad.is_key_pressed("Up"):
                    pass

                smartservo_1.set_power(0)

            else:
                if gamepad.is_key_pressed("Down"):
                    smartservo_1.set_power(-20)
                    while not not gamepad.is_key_pressed("Down"):
                        pass

                    smartservo_1.set_power(0)

                else:
                    pass

    # หมุนกล่อง
    if gamepad.is_key_pressed("N1"):
        smartservo_2.set_power(-8)

    else:
        if gamepad.is_key_pressed("N2"):
            smartservo_2.set_power(8)

        else:
            smartservo_2.set_power(0)

    # เลื่อนซ้าย,ขวา
    if gamepad.is_key_pressed("R2"):
        power_expand_board.set_power("DC3", 100)

    else:
        if gamepad.is_key_pressed("L2"):
            power_expand_board.set_power("DC3", -100)

        else:
            power_expand_board.set_power("DC3", 0)

        # relaod
        if gamepad.is_key_pressed("Right"):
            if on_off_reload == 1:
                on_off_reload = 0
                time.sleep(0.2)

            else:
                on_off_reload = 1
                time.sleep(0.2)

        else:
            pass

        power_expand_board.set_power("DC2", 100 * on_off_reload)
        encoder_motor_M5.set_power(50 * on_off_reload)

def test_code ():
    
    encoder_motor_M1.set_speed(-200)
    encoder_motor_M2.set_speed(0)
    encoder_motor_M3.set_speed(0)
    encoder_motor_M4.set_speed(200)
    time.sleep(2)
    stop_encode()
    while not (ranging_sensor_2.get_distance() < (Lcalibeate + 23) and ranging_sensor_1.get_distance() < (Rcailbrate + 23)):
        time.sleep(0.001)
        encoder_motor_M1.set_speed(-150)
        encoder_motor_M2.set_speed(150)
        encoder_motor_M3.set_speed(-150)
        encoder_motor_M4.set_speed(150)

    stop_encode()
    timer_rotage = (novapi.timer() + 2)
    while not (novapi.timer() > timer_rotage):
        time.sleep(0.001)
        # left
        encoder_motor_M1.set_speed((150 - ((ranging_sensor_1.get_distance() - 20.4)) * 4))
        encoder_motor_M3.set_speed(-1 * ((150 + ((ranging_sensor_1.get_distance() - 20.4)) * 4)))
        encoder_motor_M4.set_speed(-1 * ((150 - ((ranging_sensor_2.get_distance() - 18.3)) * 4)))
        encoder_motor_M2.set_speed((150 + ((ranging_sensor_2.get_distance() - 18.3)) * 4))

    stop_encode()

def mode_2 ():
    
    """โหมดยิง"""
    # เปิด,ปิดbrushless
    if gamepad.is_key_pressed("+"):
        if brushless == 0:
            power_expand_board.set_power("BL1", 100)
            power_expand_board.set_power("BL2", 100)
            power_expand_board.set_power("DC4", 50)
            brushless = 1
            time.sleep(0.2)

        else:
            power_expand_board.set_power("BL1", 0)
            power_expand_board.set_power("BL2", 0)
            power_expand_board.set_power("DC4", 0)
            brushless = 0
            time.sleep(0.2)

    else:
        pass

    # ปรับองศา brushless ลง
    if gamepad.is_key_pressed("N2"):
        servo_driver_1.change_angle(-1)
        time.sleep(0.05)

    else:
        pass

    # ปรับองศา brushless ขึ้น
    if gamepad.is_key_pressed("N1"):
        servo_driver_1.change_angle(1)
        time.sleep(0.05)

    else:
        pass

    # ตัวยิง
    if gamepad.is_key_pressed("R_Thumb") or gamepad.is_key_pressed("R1"):
        power_expand_board.set_power("DC1", -100)

    else:
        # ตัวยิง debug
        if gamepad.is_key_pressed("L_Thumb"):
            power_expand_board.set_power("DC1", 100)

        else:
            power_expand_board.set_power("DC1", 0)

    # reload debug
    if gamepad.is_key_pressed("Left"):
        power_expand_board.set_power("DC2", -100)
        encoder_motor_M5.set_power(-100)

    else:
        # relaod
        if gamepad.is_key_pressed("Right"):
            if on_off_reload == 1:
                on_off_reload = 0
                time.sleep(0.2)

            else:
                on_off_reload = 1
                time.sleep(0.2)

        else:
            pass

        power_expand_board.set_power("DC2", 100 * on_off_reload)
        encoder_motor_M5.set_power(100 * on_off_reload)

    # ปรับองศาbrushless auto
    if gamepad.is_key_pressed("N4") and brushless_auto == 0:
        servo_driver_1.set_angle(74)
        time.sleep(0.2)
        # up
        brushless_auto = 1

    else:
        if gamepad.is_key_pressed("N4") and brushless_auto == 1:
            servo_driver_1.set_angle(83)
            time.sleep(0.2)
            # down
            brushless_auto = 0

while True:
    time.sleep(0.001)
    if power_manage_module.is_auto_mode():
        code_all_auto()

    else:
        code_all_ma()