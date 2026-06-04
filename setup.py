import subprocess
import sys

if sys.platform == "darwin":
	req_file = "requirements-mac.txt"
elif sys.platform.startswith("linux"):
	req_file = "requirements-linux.txt"
else:
	req_file = "requirements.txt"
print(f"Installing requirements from {req_file}...")
subprocess.run([sys.executable, "-m", "pip", "install", "-r", req_file], check=True)

print("Installing Playwright browsers...")
subprocess.run([sys.executable, "-m", "playwright", "install"], check=True)

print("\n✅ Setup complete! Run 'python main.py' to start MARK XXV.")

