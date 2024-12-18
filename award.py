# 10-037 Data Types and Conditional Statements
# *********** AUTO GRATED TASK 3 **********
# Function to choose the award based on total time
def award(total_time):
    """
    total_time(0–100 minutes), award is: Honorary colours
    total_time(101–105 minutes), award is: Honorary half colours
    total_time(106–110 minutes), award is: Honorary scroll
    total_time(111+ minutes), No award
    """
    if total_time <= 100:
        return "Honorary colours"
    elif total_time <= 105:
        return "Honorary half colours"
    elif total_time <= 110:
        return "Honorary scroll"
    else:
        return "No award"

# ===== User input for the times for all three events of a triathlon ===============
event_time = {
    "Swimming": float(input("Enter the time of swimming (in minutes): ")),
    "Cycling": float(input("Enter the time of cycling (in minutes): ")),
    "Running": float(input("Enter the time of running (in minutes): "))
}
print(f"The events of a triathlon + times (in minutes): {event_time}")

# ===== The total time taken to complete the triathlon =============================
total_time = sum(event_time.values())
print(f"The total time taken to complete the triathlon is : {total_time} minutes")

# ===== The award that the participant will receive ================================
print(f"The award of participant is: {award(total_time)}")
