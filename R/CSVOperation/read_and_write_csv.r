# Read data from CSV file
data.ex <- read.csv("sample_data.csv", header=T)

# Calculate
a <- apply(data.ex[,-5], 2, max)
b <- apply(data.ex[,-5], 2, min)
A <- rbind(max=a, min=b)

# Write result to CSV file
write.csv(x=A, file="maxmin.csv")
