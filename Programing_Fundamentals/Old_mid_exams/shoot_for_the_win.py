def shoot_func(targets_):
    shot_targets = 0
    command = input()
    while command != "End":
        current_index = int(command)
        if current_index in range(len(targets_)):
            shotted_target = targets[current_index]
            targets_[current_index] = -1
            shot_targets += 1
            for index, target in enumerate(targets_):
                if target == -1:
                    continue
                if target <= shotted_target:
                    targets_[index] += shotted_target
                else:
                    targets_[index] -= shotted_target
        command = input()

    return f"Shot targets: {shot_targets} -> {' '.join(str(x) for x in targets_)}"


targets = list(map(int, input().split()))
print(shoot_func(targets))
