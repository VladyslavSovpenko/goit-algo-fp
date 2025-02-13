import random
import matplotlib.pyplot as plt

def simulate_dice_throws(num_throws):
    result_counts = {i: 0 for i in range(2, 13)}

    for _ in range(num_throws):
        roll_sum = random.randint(1, 6) + random.randint(1, 6)
        result_counts[roll_sum] += 1

    for key in result_counts:
        result_counts[key] /= num_throws

    return result_counts

def display_probabilities(result_counts):
    sums = list(result_counts.keys())
    probabilities = list(result_counts.values())

    plt.bar(sums, probabilities, tick_label=sums)
    plt.xlabel('Sum of Two Dice')
    plt.ylabel('Probability')
    plt.title('Probability Distribution of Dice Sums')
    plt.show()

number_of_throws = 10000
dice_outcomes = simulate_dice_throws(number_of_throws)
print(dice_outcomes)
display_probabilities(dice_outcomes)