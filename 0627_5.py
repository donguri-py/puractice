seconds = int(input())

hours = seconds // (60 * 60)
minutes = (seconds % (60 * 60)) // 60
remaining_seconds = (seconds % (60 * 60)) % 60

print(f"{hours}:{minutes}:{remaining_seconds}")