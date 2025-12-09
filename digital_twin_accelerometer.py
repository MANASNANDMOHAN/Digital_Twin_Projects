import pandas as pd
import time

# Load the exported accelerometer CSV
df = pd.read_csv("Accelerometer.csv")

# Digital Twin object
digital_twin = {
    "accX": None,
    "accY": None,
    "accZ": None,
    "absolute_acc": None,
    "timestamp": None
}

print("Starting Digital Twin Simulation...\n")

# Loop through the file row by row to simulate live sensor data
for index, row in df.iterrows():
    try:
        # Extract sensor values from columns
        accX = row["Linear Acceleration x (m/s^2)"]
        accY = row["Linear Acceleration y (m/s^2)"]
        accZ = row["Linear Acceleration z (m/s^2)"]
        abs_acc = row["Absolute acceleration (m/s^2)"]
        timestamp = row["Time (s)"]

        # Update Digital Twin
        digital_twin["accX"] = accX
        digital_twin["accY"] = accY
        digital_twin["accZ"] = accZ
        digital_twin["absolute_acc"] = abs_acc
        digital_twin["timestamp"] = timestamp

        # Print Digital Twin State
        print(f"Digital Twin Updated ({timestamp}s): {digital_twin}")

        # Add delay to simulate live stream
        time.sleep(0.1)   # you can increase or decrease

    except Exception as e:
        print("Error:", e)
        break

print("\nSimulation Complete!")

