import time
import datetime

def write_timestamp_to_file():
    with open("/tmp/daemon_log.txt", "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"Timestamp written: {timestamp} - this terminal will self destruct in 10 more seconds")

def run_daemon():
    while True:
        write_timestamp_to_file()
        time.sleep(10)  # Sleep for 10 seconds

if __name__ == "__main__":
    run_daemon()
