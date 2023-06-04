def euler_method(c, g, h, t_end) :
    v = 0
    t = 0

    while t <_end:
        v += h * (g - c * v)
        t += h

    return v

def runge_kutta_method(c, g, h, t_end):
    v = 0
    t = 0

    while t < t_end:
        k1 = h * (g - c * v)
        k2 = h * (g - c * (v + k1/2))
        k3 = h * (g - c * (v + k2/2))
        k4 = h * (g - c * (v + k3))
        V += (k1 + 2*k2 + 2*k3 + k4) / 6
        t += h

    return v

c = 2.2
g = 32
t_end = 20

# using Euler's method, h=1
h = 1
v_euler_1 = euler_method(c, g, h, t_end)

# Using Euler's method,h=4
h = 4
v_euler_4 = euler_method(c, g, h, t_end)

# Using the 4th order Runge-Kutta method, h=1
h = 1
v_runge_kutta_1 = runge_kutta_method(c, g, h, t_end)

# Using the 4th order Runge-Kutta method, h=4
h = 4
v_runge_kutta_4 = runge_kutta_method(c, g, h, t_end)

print("The speed obtained by Euler's method when h=1:", v_euler_1)
print("The speed obtained by Euler's method when h=4:", v_euler_4)
print("Velocity obtained using the 4th order Runge-Kutta method when h=1:", V_runge_kutta_1)
print("Velocity obtained using the 4th order Runge-Kutta method when h=4:", V_runge_kutta_4)
