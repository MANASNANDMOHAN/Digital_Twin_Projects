import requests
import time

# Replace with your phone's IP
PHY_IP = "http://192.168.1.10:8080"

while True:
    r = requests.get(f"{PHY_IP}/get?gyroX&gyroY&gyroZ")
    data = r.json()["buffer"]

    gx = data["gyroX"]["buffer"][-1]
    gy = data["gyroY"]["buffer"][-1]
    gz = data["gyroZ"]["buffer"][-1]

    print(f"Gyro (rad/s): gx={gx:.4f}, gy={gy:.4f}, gz={gz:.4f}")
    time.sleep(0.05)

