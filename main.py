import RPi.GPIO as GPIO
import time
import threading

IN1_PIN = 17
IN2_PIN = 18
IN3_PIN = 27
IN4_PIN = 22

PINS = [IN1_PIN, IN2_PIN, IN3_PIN, IN4_PIN]

HALF_STEP_SEQUENCE = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1],
]

STEPS_PER_REV = 4096

stop_flag = threading.Event()


def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for pin in PINS:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)


def cleanup_gpio():
    for pin in PINS:
        GPIO.output(pin, 0)
    GPIO.cleanup()


def step_motor(step_index):
    seq = HALF_STEP_SEQUENCE[step_index % len(HALF_STEP_SEQUENCE)]
    for pin, value in zip(PINS, seq):
        GPIO.output(pin, value)


def spin(rpm):
    step_delay = 60.0 / (rpm * STEPS_PER_REV)
    step_index = 0
    while not stop_flag.is_set():
        step_motor(step_index)
        step_index = (step_index - 1) % len(HALF_STEP_SEQUENCE)
        time.sleep(step_delay)
    for pin in PINS:
        GPIO.output(pin, 0)


def main():
    setup_gpio()

    print("Press ENTER to begin calibration, when the hand reaches 12, press ENTER again to complete.")

    input()


    stop_flag.clear()
    motor_thread = threading.Thread(target=spin, args=(3.0,), daemon=True)
    motor_thread.start()

    input()


    stop_flag.set()
    motor_thread.join(timeout=2)

    print("\nCalibration complete.")
    print("\nHow fast should the clock run?")
    print("[1]  1 RPM")
    print("[2]  1 rotation per hour")
    print("[3]  12 rotations per hour")
    print("\nType 1, 2, or 3 and press ENTER: ", end="", flush=True)

    while True:
        choice = input().strip()
        if choice == "1":
            rpm = 1.0
            label = "1 RPM"
            break
        elif choice == "2":
            rpm = 1.0 / 60.0
            label = "1 rotation per hour"
            break
        elif choice == "3":
            rpm = 12.0 / 60.0
            label = "12 rotations per hour"
            break
        else:
            print("Invalid. Type 1, 2, or 3 and press ENTER: ", end="", flush=True)

    print(f"\nRunning at {label}. Press ENTER to stop.")

    stop_flag.clear()
    motor_thread = threading.Thread(target=spin, args=(rpm,), daemon=True)
    motor_thread.start()

    input()

    stop_flag.set()
    motor_thread.join(timeout=2)
    cleanup_gpio()
    print("Motor stopped.")


if __name__ == "__main__":
    main()
