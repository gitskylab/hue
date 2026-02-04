import ota
import machine

ota = ota.ota(
  user="gitskylab",
  repo="hue",
  branch="main",
  working_dir="blue",
  files = ["boot.py", "main.py"]
)

try:
    # Code that might raise an exception
    ota.wificonnect()
    if ota.update():
        print("update complete.. rebooting...")
        machine.reset()
except OSError as e:
    # Code to handle the error
    print(f"error encountered: {e}")
