import random
import time

def random_story():
    subjects = ["Ali", "Sara", "Ahmed", "Zara", "Usman"]
    actions = ["found", "lost", "created", "destroyed", "discovered"]
    objects = ["a secret file", "a hidden treasure", "a strange bug", "a new app", "a mystery"]

    subject = random.choice(subjects)
    action = random.choice(actions)
    obj = random.choice(objects)

    return f"{subject} {action} {obj}."

def loading_animation():
    for i in range(5):
        print("Loading" + "." * i)
        time.sleep(0.5)

def main():
    print("Welcome to Random Story Generator 🎲\n")
    loading_animation()
    
    for _ in range(3):
        print(random_story())

if __name__ == "__main__":
    main()
