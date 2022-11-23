days = int(input())
doctors = 7
examinated = 0
none_examinated = 0

for day in range(1,days + 1):
    patient = int(input())
    if day % 3 == 0 and none_examinated > examinated:
        doctors += 1
    if patient <= doctors:
        examinated += patient
    if patient > doctors:
        diff = patient - doctors
        examinated += patient - diff
        none_examinated += diff

print(f"Treated patients: {examinated}.")
print(f"Untreated patients: {none_examinated}.")