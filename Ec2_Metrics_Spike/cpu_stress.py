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

