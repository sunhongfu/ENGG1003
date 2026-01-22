def ball_height(v0, t):
    g = 9.81
    return v0*t - 0.5*g*t**2

print(ball_height(5, 0.6))
