import psutil
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(
    filename="system_health.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80
PROCESS_COUNT_THRESHOLD = 300  # modify as needed

def check_system_health():
    alerts = []

    # CPU usage
    cpu = psutil.cpu_percent(interval=1)
    if cpu > CPU_THRESHOLD:
        alerts.append(f"High CPU usage! ({cpu}%)")

    # Memory usage
    memory = psutil.virtual_memory().percent
    if memory > MEMORY_THRESHOLD:
        alerts.append(f"High Memory usage! ({memory}%)")

    # Disk usage
    disk = psutil.disk_usage('/').percent
    if disk > DISK_THRESHOLD:
        alerts.append(f"High Disk usage! ({disk}%)")

    # Number of running processes
    process_count = len(psutil.pids())
    if process_count > PROCESS_COUNT_THRESHOLD:
        alerts.append(f"High number of processes! ({process_count})")

    if alerts:
        for alert in alerts:
            print(f"[ALERT] {alert}")
            logging.warning(alert)
    else:
        msg = f"All systems normal. CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%, Processes: {process_count}"
        print(msg)
        logging.info(msg)

if __name__ == "__main__":
    check_system_health()
