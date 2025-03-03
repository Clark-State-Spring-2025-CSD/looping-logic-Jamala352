#This simulates rolling to hit in Warhammer 40,000
#Prompt the user how many dice are being rolled, and what the hit target is
#Roll the correct number of dice, then display the results
#This is a guided practice. Either follow with the video or your instructor will
#go over this in class.
#Video Link: https://youtu.be/89G5DN0-O3k

import random
random.seed()

def roll_dice(num_dice, target):
    rolls = [random.randint(1, 6) for _ in range(num_dice)]
    hits = sum(roll >= target for roll in rolls)
    return hits, rolls

def simulate_warhammer_rolls(num_dice, hit_target, wound_target, save_target):
    hits, hit_rolls = roll_dice(num_dice, hit_target)
    wounds, wound_rolls = roll_dice(hits, wound_target)
    saves, save_rolls = roll_dice(wounds, save_target)
    
    return {
        'Hit Rolls': hit_rolls,
        'Hits': hits,
        'Wound Rolls': wound_rolls,
        'Wounds': wounds,
        'Save Rolls': save_rolls,
        'Saves': saves
    }

num_dice = int(input("Enter the number of dice being rolled: "))
hit_target = int(input("Enter the hit target: "))
wound_target = int(input("Enter the wound target: "))
save_target = int(input("Enter the save target: "))

results = simulate_warhammer_rolls(num_dice, hit_target, wound_target, save_target)

print(f"Hit Rolls: {results['Hit Rolls']} - Hits: {results['Hits']}")
print(f"Wound Rolls: {results['Wound Rolls']} - Wounds: {results['Wounds']}")
print(f"Save Rolls: {results['Save Rolls']} - Saves: {results['Saves']}")
