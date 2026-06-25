# run.py
import subprocess
import sys
import os

def run_tests():
    """
    Unified test runner. Usage:
      python run.py              → all tests, headless
      python run.py smoke        → smoke tests only
      python run.py regression   → regression tests
      python run.py smoke --headed   → with browser visible
      python run.py all -n 4     → parallel with 4 workers
    """

    args = sys.argv[1:]
    marker = None
    extra_flags = []

    for arg in args:
        if arg in ("smoke", "regression", "e2e", "api"):
            marker = arg
        else:
            extra_flags.append(arg)

    # Base command — always generate Allure results
    cmd = ["pytest", "--alluredir=allure-results"]

    if marker:
        cmd += ["-m", marker]
        print(f"\n🎯 Running [{marker.upper()}] tests...\n")
    else:
        print("\n🚀 Running ALL tests...\n")

    # Add any extra flags (e.g. --headed, -n 4)
    cmd += extra_flags

    # Run tests
    result = subprocess.run(cmd)

    # Open Allure report
    print("\n📊 Opening Allure Report...\n")
    subprocess.run(["allure", "serve", "allure-results"])

    # Exit with pytest's exit code (important for CI)
    sys.exit(result.returncode)


if __name__ == "__main__":
    run_tests()