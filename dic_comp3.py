seasons1 = {
    "Summer": "夏",
    "Autumn": "秋",
    "Winter": "冬",
    "Spring": "春"
}

# Key-Valueの入れ替え
seasons2 = { j:e for (e,j) in seasons1.items()}
print(seasons2)