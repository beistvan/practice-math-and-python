# sheet = "sheet1.txt"
# mean = "mean1.txt"

grades = []

with open(sheet, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split()
        if not parts:
            continue
        status = parts[-1].strip("()")
        if status in ["exam", "autograde"]:
            grade = int(parts[-2])
            grades.append(grade)

calculated_mean = sum(grades) / len(grades) if grades else 0

with open(mean, "r", encoding="utf-8") as f:
    provided_mean = float(f.read().strip())

if abs(calculated_mean - provided_mean) < 1e-6:
    print("OK")
else:
    print("ERROR")
