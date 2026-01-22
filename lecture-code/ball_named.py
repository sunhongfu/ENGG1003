def ball_height(v0, t):
    g = 9.81
    return v0*t - 0.5*g*t**2

v0 = 5
print(ball_height(v0, t=0.6))   # works fine
# positional before named

print(ball_height(t=0.6, v0))   # syntax error!
# named before positional