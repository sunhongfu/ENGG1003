def ball_height(v0, t):
	g = 9.81
	return v0*t - 0.5*g*t**2

v0 = 5
time = 0.6
print(ball_height(v0, time))