import motors.rmd_can_v0 as motor



M = [0, 0, 0, 0]

def move(Vx, Vy, omega):
    l = 25
    a = l/1.41
    b = l/1.41

    r = 6.35
    M[0] = (Vx - Vy - (a + b) * omega) * 1/r
    M[1] = (Vx + Vy + (a + b) * omega) * 1/r
    M[2] = (Vx - Vy + (a + b) * omega) * 1/r
    M[3] = (Vx + Vy - (a + b) * omega) * 1/r

    print(M[0], M[1], M[2], M[3])
    
    motor.run_speed(1, M[0])
    motor.run_speed(2, -M[1])
    motor.run_speed(3, -M[2])
    motor.run_speed(4, M[3])
    