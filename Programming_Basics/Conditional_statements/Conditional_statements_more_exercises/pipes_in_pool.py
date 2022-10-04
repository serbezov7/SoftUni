volume_pool = int(input())
pipe_one = int(input())
pipe_two = int(input())
hours_left = float(input())

pipe_one_volume = hours_left * pipe_one
pipe_two_volume = hours_left * pipe_two
total_volume = pipe_one_volume + pipe_two_volume
pipe_one_percent = pipe_one_volume / total_volume * 100
pipe_two_percent = pipe_two_volume / total_volume * 100
volume_difference_percent = total_volume / volume_pool * 100
volume_difference_ltr = total_volume - volume_pool
if total_volume <= volume_pool:
    print(f"The pool is {volume_difference_percent:.2f}% full. Pipe 1:{pipe_one_percent:.2f}%. Pipe 2: {pipe_two_percent:.2f}%")
else:
    print(f"For {hours_left:.2f} hours the pool overflows with {volume_difference_ltr:.2f} liters.")

