# expert_system.py

def ask(question):
    while True:
        answer = input(f"{question} (yes/no): ").lower()
        if answer in ['yes', 'no']:
            return answer == 'yes'
        print("Please respond with 'yes' or 'no'.")

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

    if not ask("Is the computer turning on at all?"):
        score["Power Issue"] += 2
    else:
        if not ask("Is the power light ON or do you hear fans?"):
            score["Motherboard Failure"] += 2
        else:
            if not ask("Is there any display on the monitor?"):
                score["Monitor or GPU Issue"] += 2
            else:
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

                if ask("Have you checked cables and external connections?"):
                    score["No Issue"] += 1

                if ask("Have you tried restarting in safe mode?"):
                    score["No Issue"] += 1

    # Select top result
    top_issue = max(score, key=score.get)
    confidence = score[top_issue]

    print("\n🔍 Diagnosis Summary:")
    if confidence == 0:
        print("We couldn't detect any specific issue. Please perform deeper diagnostics or seek professional help.")
    else:
        print(f"Most probable issue: {top_issue} (confidence score: {confidence})")

    # Optional recommendation
    print("\n📌 Recommendations:")
    if top_issue == "Power Issue":
        print("- Check the power cable, adapter, or try another outlet.")
    elif top_issue == "Motherboard Failure":
        print("- Consider professional servicing. The motherboard may be damaged.")
    elif top_issue == "Monitor or GPU Issue":
        print("- Check monitor cables, test with another screen, or remove and re-seat the graphics card.")
    elif top_issue == "Bootloader/OS Corruption":
        print("- Boot from a recovery disk or use OS repair tools.")
    elif top_issue == "RAM/Hardware Failure":
        print("- Reseat RAM, disconnect added hardware, or check BIOS beep codes.")
    elif top_issue == "No Issue":
        print("- System appears healthy. Try restarting or performing a system scan if issues persist.")

if __name__ == "__main__":
    diagnose()