weekday1 = ["Sun", "Mon", "Tue"]
weekday2 = ["月", "火", "水", "木", "金", "土"]

for (eng, jap) in zip(weekday1,weekday2):
    print(eng + ":" + jap)