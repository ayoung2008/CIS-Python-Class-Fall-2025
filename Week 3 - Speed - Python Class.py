# Problem 1: Time Saved by Speeding

#Ask the user for inputs
avg_speed = float(input("Enter your average speed (mph): "))
speed_limit = float(input("Enter the speed limit (mph): "))
distance = float(input("Enter the distance traveled (miles): "))

#Calculate travel times (in hours)
time_with_limit = distance / speed_limit
time_with_avg = distance / avg_speed

#Calculate time saved (in minutes)
time_saved = (time_with_limit - time_with_avg) * 60

#Show the result
print(f"\nIf you drive {distance} miles:")
print(f" - At {speed_limit} mph: {time_with_limit*60:.2f} minutes")
print(f" - At {avg_speed} mph: {time_with_avg*60:.2f} minutes")
print(f" => Time saved: {time_saved:.2f} minutes") 
