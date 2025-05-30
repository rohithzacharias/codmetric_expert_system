# expert_system.py

from datetime import datetime

def ask(question):
    while True:
        answer = input(f"{question} (yes/no): ").lower()
        if answer in ['yes', 'no']:
            return answer == 'yes'
        print("Please respond with 'yes' or 'no'.")

def get_category():
    print("\n📋 Choose a category to diagnose:")
    print("1. Power issues")
    print("2. Boot issues")
    print("3. Display issues")
    print("4. Full system check")

    while True:
        choice = input("Enter your choice (1-4): ")
        if choice in ['1', '2', '3', '4']:
            return int(choice)
        print("Invalid input. Please choose 1 to 4.")

def diagnose():
    print("🔧 Expert System: Diagnosing Computer Boot Issues\n")

    score = {
        "Power Issue": 0,
        "Motherboard Failure": 0,
        "Monitor or GPU Issue": 0,
        "Bootloader/OS Corruption": 0,
        "RAM/Hardware Failure": 0,
        "No Issue": 0
    }

    category = get_category()

    if category == 1 or category == 4:
        if not ask("Is the computer turning on at all?"):
            score["Power Issue"] += 2
        if ask("Does the power button do nothing when pressed?"):
            score["Power Issue"] += 2
        if not ask("Is the power light ON or do you hear fans?"):
            score["Motherboard Failure"] += 2

    if category == 2 or category == 4:
        if ask("Does the computer freeze on the manufacturer's logo?"):
            score["Bootloader/OS Corruption"] += 2
        if ask("Does it restart repeatedly after turning on?"):
            score["RAM/Hardware Failure"] += 2
        if ask("Do you see a 'No bootable device' or similar message?"):
            score["Bootloader/OS Corruption"] += 1
        if ask("Did you recently install a new OS or update drivers?"):
            score["Bootloader/OS Corruption"] += 1
        if ask("Did you recently change any hardware (RAM, SSD, GPU)?"):
            score["RAM/Hardware Failure"] += 1
        if ask("Do you hear continuous beeps when turning on?"):
            score["RAM/Hardware Failure"] += 2
        if ask("Does the screen go blue or crash unexpectedly?"):
            score["RAM/Hardware Failure"] += 2

    if category == 3 or category == 4:
        if not ask("Is there any display on the monitor?"):
            score["Monitor or GPU Issue"] += 2
        if ask("Is the screen completely black or says 'No signal'?"):
            score["Monitor or GPU Issue"] += 2
        if ask("Does the system beep once and then stop?"):
            score["No Issue"] += 1

    if category == 4:
        if ask("Have you checked cables and external connections?"):
            score["No Issue"] += 1
        if ask("Have you tried restarting in safe mode?"):
            score["No Issue"] += 1

    # Sort by score
    sorted_issues = sorted(score.items(), key=lambda x: x[1], reverse=True)
    top_issue, confidence = sorted_issues[0]

    print("\n🔍 Diagnosis Summary:")
    if confidence == 0:
        print("We couldn't detect any specific issue. Please perform deeper diagnostics or seek professional help.")
    else:
        print(f"Most probable issue: {top_issue} (confidence score: {confidence})")

    print("\n📊 All Issues Ranked:")
    for issue, pts in sorted_issues:
        if pts > 0:
            print(f"- {issue}: {pts}")

    # Recommendations
    recommendations = {
        "Power Issue": "- Check the power cable, adapter, or try another outlet.",
        "Motherboard Failure": "- Consider professional servicing. The motherboard may be damaged.",
        "Monitor or GPU Issue": "- Check monitor cables, test with another screen, or re-seat the graphics card.",
        "Bootloader/OS Corruption": "- Boot from a recovery disk or use OS repair tools.",
        "RAM/Hardware Failure": "- Reseat RAM, disconnect added hardware, or check BIOS beep codes.",
        "No Issue": "- System appears healthy. Try restarting or performing a system scan if issues persist."
    }

    print("\n📌 Recommendations:")
    if confidence > 0:
        print(recommendations[top_issue])

    # Save report
    with open("diagnosis_report.txt", "w") as file:
        file.write("Computer Boot Diagnosis Report\n")
        file.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        file.write(f"Most Probable Issue: {top_issue} (Score: {confidence})\n\n")
        file.write("All Scores:\n")
        for issue, pts in sorted_issues:
            file.write(f"- {issue}: {pts}\n")
        file.write("\nRecommendation:\n")
        file.write(recommendations.get(top_issue, "No recommendation found."))

    print("\n📝 Report saved to 'diagnosis_report.txt'.")

if __name__ == "__main__":
    diagnose()