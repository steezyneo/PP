total_distance_km = 10
total_time_min = 43 + 30/60

total_distance_miles = total_distance_km / 1.61

avg_time_per_mile = total_time_min / total_distance_miles

total_time_hrs = total_time_min / 60
avg_speed_mph = total_distance_miles / total_time_hrs

print("Avg Time per Mile: ",avg_time_per_mile, "minutes")
print("Avg Speed: ",avg_speed_mph," mph")
