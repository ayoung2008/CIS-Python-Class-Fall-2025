# Pizza Assignment
# Each pizza has 8 slices
SLICES_PER_PIZZA = 8

# Inputs: how many slices each of the 4 family members eat
person1 = int(input("How many slices does person 1 eat? "))
person2 = int(input("How many slices does person 2 eat? "))
person3 = int(input("How many slices does person 3 eat? "))
person4 = int(input("How many slices does person 4 eat? "))

#Processing: total slices needed
total_slices = person1 + person2 + person3 + person4

pizzas_needed = total_slices // SLICES_PER_PIZZA

#If there are leftover slices needed, add one more pizza
if total_slices % SLICES_PER_PIZZA !=0:

    pizzas_needed += 1

#Calculate leftover slices
leftover_slices = pizzas_needed *SLICES_PER_PIZZA - total_slices

#Output
print ("Total slices needed:", pizzas_needed)
print("Leftover slices:" , leftover_slices) 
    
