
import time

print("===== STOPWATCH =====")
print("Press Ctrl + C to stop.")

start_time = time.time()

try:
    while True:
        elapsed = int(time.time() - start_time)

        hours = elapsed // 3600
        minutes = (elapsed % 3600) // 60
        seconds = elapsed % 60

        print(
            f"\rTime: {hours:02d}:{minutes:02d}:{seconds:02d}",
            end="",
            flush=True
        )

        time.sleep(1)

except KeyboardInterrupt:
    print("\nStopwatch stopped!")
