import datetime

def get_valid_mood():
    valid_moods = ["happy", "relaxed", "apathetic", "sad", "angry"]
    while True:
        mood = input("Please enter your current mood (happy, relaxed, apathetic, sad, angry): ").lower()
        if mood in valid_moods:
            if mood == "happy":
                return 2
            elif mood == "relaxed":
                return 1
            elif mood == "apathetic":
                return 0
            elif mood == "sad":
                return -1
            elif mood == "angry":
                return -2
        else:
            print("Invalid mood entered, please try again.")

def write_mood_to_file(mood):
    with open("data/mood_diary.txt", "a") as file:
        file.write(f"{mood} {datetime.date.today()}\n")

def has_entered_mood_today():
    today = str(datetime.date.today())
    with open("data/mood_diary.txt", "r") as file:
        return any(line.split()[1] == today for line in file)

def calculate_average_mood():
    with open("data/mood_diary.txt", "r") as file:
        entries = file.readlines()
        recent_entries = entries[-7:] if len(entries) >= 7 else entries
        moods = [int(entry.split()[0]) for entry in recent_entries]
        return sum(moods) // len(moods) if moods else 0

def diagnose_moods(average_mood):
    with open("data/mood_diary.txt", "r") as file:
        entries = file.readlines()
        recent_entries = entries[-7:]
        mood_counts = {"2": 0, "1": 0, "0": 0, "-1": 0, "-2": 0}
        for entry in recent_entries:
            mood = entry.split()[0]
            mood_counts[str(mood)] += 1

    if mood_counts["2"] >= 5:
        return "manic"
    elif mood_counts["-1"] >= 4:
        return "depressive"
    elif mood_counts["0"] >= 6:
        return "schizoid"
    else:
        return {2: "happy", 1: "relaxed", 0: "apathetic", -1: "sad", -2: "angry"}[average_mood]

def is_gt_7_days():
     with open("data/mood_diary.txt", "r") as file:
        entries = file.readlines()
        return len(entries) >= 7

def assess_mood():
    if has_entered_mood_today():
        print("Sorry, you have already entered your mood today.")
        return

    mood = get_valid_mood()
    write_mood_to_file(mood)

    if not is_gt_7_days():
        return

    average_mood = calculate_average_mood()
    diagnosis = diagnose_moods(average_mood)
    print(f"Your diagnosis: {diagnosis}!")

