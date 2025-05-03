import shutil

#Get Disk Usage Statistics
total, used, free = shutil.disk_usage("/")

print("Total Disk Space: %d GB" % (total // (2**30)))
print("Used Disk Space: %d GB" % (used // (2**30)))
print("Free Disk Space: %d GB" % (free // (2**30)))
print("Percentage of Disk Space Used: %d %%" % ((used / total) * 100))

##show percentage Used

percentage_used = (used / total) * 100
print(f"Percentage of Disk Space Used: {percentage_used:.2f}%")