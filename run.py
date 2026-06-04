import subprocess
import tempfile
import shutil
import sys

allure_dir = tempfile.mkdtemp(prefix="allure_")

marker = sys.argv[1] if len(sys.argv) > 1 else None

if marker:
    command = f"pytest -m {marker} --alluredir={allure_dir}"
    print(f"Running {marker.upper()} tests...")
else:
    command = f"pytest --alluredir={allure_dir}"
    print("Running all tests...")

subprocess.run(command, shell=True)

print("Opening Allure Report...")

subprocess.run(
    f"allure serve {allure_dir}",
    shell=True
)

shutil.rmtree(allure_dir, ignore_errors=True)