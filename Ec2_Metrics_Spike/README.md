# 🔧 AWS CloudWatch CPU Utilization Simulation

This project simulates **high CPU usage** on an EC2 Ubuntu instance so you can monitor CPU metrics using **Amazon CloudWatch**.

Useful for:
- Practicing CloudWatch monitoring
- Testing EC2 performance under load
- Validating alarms and thresholds

---

## ✅ Requirements

- An Ubuntu EC2 instance (Free Tier-friendly)
- Basic knowledge of EC2 & SSH
- Python 3 (pre-installed on most Ubuntu images)
- Internet access on the EC2 instance (for installing packages)

---

## ⚙️ Setup Instructions

### 1. Connect to Your EC2 Instance

```bash
ssh -i your-key.pem ubuntu@your-ec2-public-ip
```

> Replace `your-key.pem` with your actual private key file.

---

### 2. Install Python & Dependencies

Run the following commands to update the package manager and install Python dependencies:

```bash
sudo apt update
sudo apt install python3-pip -y
pip3 install psutil
```

> `psutil` is optional — useful if you plan to extend the script for memory or system monitoring later.

---

### 3. Create the Python Script

Create a new Python file:

```bash
nano cpu_stress.py
```

Paste the following code:

```python
import threading
import time
import argparse

def cpu_load():
    while True:
        pass  # Keeps CPU busy

def start_cpu_stress(duration=60, threads=2):
    print(f"Starting CPU load for {duration} seconds using {threads} threads...")
    thread_list = []

    for _ in range(threads):
        t = threading.Thread(target=cpu_load)
        t.daemon = True
        t.start()
        thread_list.append(t)

    time.sleep(duration)
    print("Stopping CPU load.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulate CPU usage on the system.")
    parser.add_argument("--duration", type=int, default=60, help="Duration in seconds to keep CPU busy")
    parser.add_argument("--threads", type=int, default=2, help="Number of CPU threads to utilize")
    args = parser.parse_args()
    start_cpu_stress(duration=args.duration, threads=args.threads)
```

Save and exit: `Ctrl + O`, `Enter`, then `Ctrl + X`.

---

## 🚀 Run the Script

Use the following command to run the script and simulate CPU usage:

```bash
python3 cpu_stress.py --duration 120 --threads 2
```

- `--duration`: Duration in seconds (default is 60)
- `--threads`: Number of CPU threads to use (2 for `t2.micro`)

---

## 🛑 Stop the Script Manually (If Needed)

If the script is running in the background or you need to stop it early:

```bash
pkill -f cpu_stress.py
```

---

## 📊 View Metrics in AWS CloudWatch

1. Go to the AWS Console
2. Open **CloudWatch > Metrics > EC2 > Per-Instance Metrics**
3. Select your **Instance ID**
4. Look for **CPUUtilization**

> ⏱️ It may take 2–3 minutes for updated metrics to appear in the CloudWatch dashboard.

---

## 🧹 Cleanup

To remove the script:

```bash
rm cpu_stress.py
```

Or just stop/terminate the EC2 instance to avoid further charges.

---

## ✅ Example Output

```
Starting CPU load for 120 seconds using 2 threads...
Stopping CPU load.
```

---

## 📄 License

MIT License

---

## 👨‍💻 Author

- [MD WASIM ANSARI](https://github.com/wasimm267)

