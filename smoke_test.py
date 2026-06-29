#!/usr/bin/env python3
"""
smoke_test.py — Module 3 (Virtual Environments)

A "smoke test" is the minimum proof that the wiring is live. This one
proves three things, in order:

  1. Which Python is actually running this script (should be your venv's).
  2. That a real third-party package (requests) is installed and importable.
  3. That requests can reach the network and do real work.

If all three pass, your isolated environment is set up correctly.

Run it from the root of your agentic-ai-ready repo, with your venv
ACTIVATED:

    python smoke_test.py

If it fails, the error almost always means one of two things:
  - your venv wasn't activated when you ran `pip install requests`, or
  - you're running a different Python than the one you installed into.
Check for the (.venv) prefix in your prompt and run `which python`.
"""

import sys


def check_1_python_path():
    """Print the interpreter actually running this script."""
    print("Check 1 — Python interpreter")
    print(f"    Running: {sys.executable}")
    if ".venv" in sys.executable or "venv" in sys.executable:
        print("    Looks like a venv Python. Good.")
    else:
        print("    WARNING: this does not look like a venv Python.")
        print("    If you expected to be in a venv, activate it and re-run.")
    print()
    return True


def check_2_requests_installed():
    """Confirm requests is importable, and report its version."""
    print("Check 2 — requests package")
    try:
        import requests
    except ModuleNotFoundError:
        print("    FAILED: requests is not installed in this environment.")
        print("    Activate your venv, then run: pip install requests")
        return False
    print(f"    requests version: {requests.__version__}")
    print("    Imported successfully.")
    print()
    return True


def check_3_network_fetch():
    """Use requests to fetch a real URL and confirm a 200 response."""
    print("Check 3 — live network fetch")
    import requests
    url = "https://api.github.com"
    headers = {"User-Agent": "module3-smoke-test"}
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
    except Exception as exc:
        print(f"    FAILED: could not fetch {url}")
        print(f"    {type(exc).__name__}: {exc}")
        print("    Check your internet connection and try again.")
        return False
    print(f"    GET {url}")
    print(f"    Status: {resp.status_code}")
    print("    Fetched a real URL successfully.")
    print()
    return True


def main():
    print("=" * 55)
    print("Module 3 smoke test — virtual environment check")
    print("=" * 55)
    print()

    results = [
        check_1_python_path(),
        check_2_requests_installed(),
    ]
    # Only attempt the network fetch if requests imported.
    if results[-1]:
        results.append(check_3_network_fetch())
    else:
        results.append(False)

    print("=" * 55)
    if all(results):
        print("All three checks passed.")
        return 0
    print("One or more checks failed — read the messages above.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
