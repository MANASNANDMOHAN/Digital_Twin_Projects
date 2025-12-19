import pandas as pd
import numpy as np
import time

def calculate_orientation(accX, accY, accZ):
    """
    Calculate pitch, roll, and yaw from accelerometer data
    """
    roll = np.arctan2(accY, accZ) * 180.0 / np.pi
    pitch = np.arctan2(-accX, np.sqrt(accY**2 + accZ**2)) * 180.0 / np.pi
    yaw = 0.0
    return pitch, roll, yaw
    
def print_digital_twin(digital_twin):
    """
    Pretty print the digital twin state
    """
    print("=" * 70)
    print(f"  DIGITAL TWIN STATE @ t={digital_twin['timestamp']:.3f}s")
    print("=" * 70)
    print("  Acceleration:")
    print(f"    X: {digital_twin['accX']:>8.4f} m/s²")
    print(f"    Y: {digital_twin['accY']:>8.4f} m/s²")
    print(f"    Z: {digital_twin['accZ']:>8.4f} m/s²")
    print(f"    Absolute: {digital_twin['absolute_acc']:>8.4f} m/s²")
    print("  Orientation:")
    print(f"    Pitch: {digital_twin['pitch']:>8.2f}°")
    print(f"    Roll:  {digital_twin['roll']:>8.2f}°")
    print(f"    Yaw:   {digital_twin['yaw']:>8.2f}° (N/A without gyro)")
    print("=" * 70)
    print()

def main():
    try:
        df = pd.read_csv("Accelerometer.csv")
        print(f"✓ Loaded {len(df)} data points from Accelerometer.csv\n")
    except FileNotFoundError:
        print("❌ Error: Accelerometer.csv not found!")
        return
    except Exception as e:
        print(f"❌ Error loading CSV: {e}")
        return
    
    digital_twin = {
        "accX": None,
        "accY": None,
        "accZ": None,
        "absolute_acc": None,
        "pitch": None,
        "roll": None,
        "yaw": None,
        "timestamp": None
    }
    
    print("🚀 Starting Digital Twin Simulation with Orientation Tracking...\n")
    time.sleep(1)
    
    for index, row in df.iterrows():
        try:
            accX = row["Linear Acceleration x (m/s^2)"]
            accY = row["Linear Acceleration y (m/s^2)"]
            accZ = row["Linear Acceleration z (m/s^2)"]
            abs_acc = row["Absolute acceleration (m/s^2)"]
            timestamp = row["Time (s)"]
            
            pitch, roll, yaw = calculate_orientation(accX, accY, accZ)
            
            digital_twin["accX"] = accX
            digital_twin["accY"] = accY
            digital_twin["accZ"] = accZ
            digital_twin["absolute_acc"] = abs_acc
            digital_twin["pitch"] = pitch
            digital_twin["roll"] = roll
            digital_twin["yaw"] = yaw
            digital_twin["timestamp"] = timestamp
            
            print_digital_twin(digital_twin)
            
            time.sleep(0.1)
            
        except KeyError as e:
            print(f"❌ Error: Column {e} not found in CSV")
            print("Available columns:", df.columns.tolist())
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            import traceback
            traceback.print_exc()
            break
    
    print("\n Digital Twin Simulation Completed.")
    print(f"✓ Processed {index + 1} data points")

if __name__ == "__main__":
    main()




































