import os
import subprocess
import logging
from datetime import datetime

# Configurations
SOURCE_DIR = "/path/to/your/data"
REMOTE_USER = "youruser"
REMOTE_HOST = "remote.server.com"
REMOTE_PATH = "/remote/backup/path/"
LOG_FILE = "backup_report.log"

# Set up logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def backup_directory():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = os.path.basename(SOURCE_DIR.rstrip('/')) + "_" + timestamp + ".tar.gz"
    backup_file = f"/tmp/{backup_name}"

    try:
        # Create compressed archive
        subprocess.check_call([
            "tar", "-czf", backup_file, "-C", os.path.dirname(SOURCE_DIR), os.path.basename(SOURCE_DIR)
        ])
        logging.info(f"Archive created: {backup_file}")

        # SCP to remote host
        scp_cmd = ["scp", backup_file, f"{REMOTE_USER}@{REMOTE_HOST}:{REMOTE_PATH}"]
        subprocess.check_call(scp_cmd)
        logging.info(f"Backup sent to {REMOTE_HOST}")

        print(f"[SUCCESS] Backup {backup_file} transferred to {REMOTE_HOST}:{REMOTE_PATH}")
        logging.info(f"Backup {backup_file} successfully transferred.")
        os.remove(backup_file) # Clean up temp archive
    except subprocess.CalledProcessError as e:
        print(f"[FAIL] Backup operation failed: {str(e)}")
        logging.error(f"Backup operation failed: {str(e)}")

if __name__ == "__main__":
    backup_directory()
