series_name = input()
count_seasons = int(input())
count_episodes = int(input())
time_for_one_episode = float(input())
time_for_one_episode *= 1.20
special_episode = count_seasons * 10
total_time = time_for_one_episode * count_seasons * count_episodes + special_episode
print(f"Total time needed to watch the {series_name} series is {int(total_time)} minutes.")