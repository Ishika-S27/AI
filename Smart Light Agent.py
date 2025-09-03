outside_light = input("Is outside light available? (yes/no): ").strip().lower() == "yes"
human_present = input("Is human present in the room? (yes/no): ").strip().lower() == "yes"

if human_present and not outside_light:
    action = "Light ON"
else:
    action = "Light OFF"

print("Action:", action)

