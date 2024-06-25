from mood_assessor import *
import os

def main():
    if not os.path.exists("data"):
        os.makedirs("data")

    mood_diary_path = "data/mood_diary.txt"
    if not os.path.exists(mood_diary_path):
        open(mood_diary_path, "w").close()
    
    # while True:
    #     diagonose = assess_mood()
    #     if diagonose:
    #         print(diagonose)
    #         break
    assess_mood()
main()
