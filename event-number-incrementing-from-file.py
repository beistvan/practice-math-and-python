import os
import re

lines = []
if os.path.exists(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        lines = f.readlines()

max_num = 0
for line in lines:
    m = re.match(r"event\s+(\d+)\s*-", line.strip())
    if m:
        max_num = max(max_num, int(m.group(1)))

new_num = max_num + 1
new_event = f"event {new_num} - '{event}'\n"

with open(file_name, "w", encoding="utf-8") as f:
    f.write(new_event)
    f.writelines(lines)
