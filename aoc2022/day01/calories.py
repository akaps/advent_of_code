def main():
    lines = open('input.txt')
    calories = []

    current = 0
    for line in lines:
        line = line.strip()
        if line.isdigit():
            current += int(line)
        else:
            calories.append(current)
            current = 0

    max_calories = total = max(calories)
    print(max_calories)
    for _ in range(2):
        calories.remove(max_calories)
        max_calories = max(calories)
        total += max_calories

    print(total)

if __name__ == "__main__":
    main()
