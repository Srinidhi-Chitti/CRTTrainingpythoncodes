def find_fastest_three(num_cars=25, max_per_race=5, cost_per_race=10):
    races = []
    cars = list(range(1, num_cars + 1))  # Cars 1 to 25

    groups = [cars[i:i+max_per_race] for i in range(0, num_cars, max_per_race)]
    for group in groups:
        races.append(group)

    winners = [group[0] for group in groups]
    races.append(winners)

    sorted_winners = winners  # We assume given order is fastest → slowest
    contenders = []

    first_group = groups[cars.index(sorted_winners[0]) // max_per_race]
    second_group = groups[cars.index(sorted_winners[1]) // max_per_race]
    third_group = groups[cars.index(sorted_winners[2]) // max_per_race]

    contenders.extend(first_group[1:3])
  
    contenders.extend(second_group[0:2])
   
    contenders.append(third_group[0])

    races.append(contenders)

    total_cost = len(races) * cost_per_race
    return races, total_cost

race_plan, money_spent = find_fastest_three()
print("Race sequence:")
for i, race in enumerate(race_plan, 1):
    print(f"Race {i}: Cars {race}")
print(f"Total money spent: ₹{money_spent}")
