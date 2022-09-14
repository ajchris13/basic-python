total_seconds = int(input("Enter the number of seconds: "))
minute = int(60)
hour = int(3600)
rem_hour = total_seconds // hour
rem_seconds = total_seconds - hour * rem_hour
rem_minute = rem_seconds // minute
rem_seconds = rem_seconds - minute * rem_minute
print()
print(total_seconds, "seconds =", rem_hour, "hours,", end=' ')
print(rem_minute, "minutes, and", rem_seconds, "seconds")
