nylon = int(input())
paint = int(input())
paint_thinner = int(input())
hours_for_job = int(input())

sum_nylon = (nylon + 2) * 1.50
sum_paint = paint * 1.10 * 14.50
sum_paint_thinner = paint_thinner * 5.00

total_sum = sum_nylon + sum_paint + sum_paint_thinner + 0.40
workers=total_sum*0.30*hours_for_job

total_cost=total_sum+workers
print(total_cost)
