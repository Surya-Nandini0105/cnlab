
n = int(input("Enter number of frames: "))
w = int(input("Enter window size: "))

i = 0

while i < n:
    print("Sending frames:")

    for j in range(i, min(i+w, n)):
        print("Frame", j, "sent")

    lost = int(input("Enter lost frame (-1 for no loss): "))

    if lost == -1:
        print("All frames received")
    else:
        print("Retransmitting frames")

        for j in range(lost, min(i+w, n)):
            print("Frame", j, "resent")

    i = min(i+w, n)

print("Transmission completed")
