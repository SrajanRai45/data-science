🛠 Troubleshooting Guide

This document helps you identify and resolve common issues related to Python environment setup in this project. It covers conflicts between uv, MISC, and pre-installed Python, as well as common Jupyter and package issues.

1. Python Version Conflicts
Problem

You run:

python --version


and it shows a different Python version than expected.

Cause

Your terminal is using the system Python or MISC global version instead of the uv-managed project environment.

You may have multiple managers installed and their paths overlap.

Solution

Always run Python commands using uv:

uv run python --version


This ensures you are using the correct project-specific Python version.

If you accidentally mixed MISC and uv:

Verify which Python version MISC is managing:

misc python list


Use uv for project-level commands to avoid conflicts:

uv run python my_script.py

2. uv Environment Not Found
Problem

Running:

uv run python


gives an error like: “Environment not found”.

Cause

You have not installed a Python version using uv for this project.

uv environment was deleted or corrupted.

Solution

Install the desired Python version:

uv python install 3.12


Pin the version to the project:

uv python pin 3.12


Retry running commands using:

uv run python --version

3. Jupyter Lab Not Launching Correctly
Problem

uv run jupyter lab fails or Jupyter does not recognize installed packages.

Cause

Packages like numpy, pandas, or matplotlib were not installed inside uv.

You might be trying to run Jupyter using system Python.

Solution

Ensure all dependencies are installed in uv:

uv add numpy pandas matplotlib seaborn jupyterlab


Launch Jupyter with uv:

uv run jupyter lab


Check the kernel in Jupyter Lab and make sure it matches uv’s Python.

4. MISC and uv Conflicts
Problem

uv run python or misc python commands behave unpredictably.

Cause

Both uv and MISC try to manage Python versions on the same paths.

The system PATH variable may be pointing to MISC before uv.

Solution

For project-level work, rely exclusively on uv.

Keep MISC for global installs only.

Avoid running both managers simultaneously in the same terminal session unless necessary.

5. Missing Packages or Modules
Problem

You run a script:

import numpy


and get ModuleNotFoundError.

Cause

The package was installed in a different environment (system or MISC) and not in uv.

Solution

Make sure uv environment is active:

uv run python


Install missing packages in uv:

uv add numpy

6. Environment Corruption
Problem

Python environment stops working, or uv commands fail unexpectedly.

Cause

Incorrect manual changes in uv folders.

Path conflicts with system Python or MISC.

Solution

Reinstall Python in uv:

uv python reinstall 3.12


Remove old pinned versions if necessary:

uv python unpin 3.11


Always use uv run to execute project commands.

7. Best Practices to Avoid Issues

Always use uv run for Python commands in this project.

Keep MISC only for managing global installations; do not mix with uv in the same session.

Pin your Python version for reproducibility.

Install all project dependencies inside uv — never in the system Python.

Maintain separate pyproject.toml and python.version files for each project.

8. References and Documentation

Python Official Docs: https://docs.python.org/3/

uv Documentation: https://docs.astral.sh/uv/

MISC Documentation: https://github.com/misc-python/misc
 (replace with official link if needed)

This troubleshooting.md ensures that any developer joining the project can quickly resolve conflicts and avoid common pitfalls.


**ADDITIONAL**

9. Common Mistake: Misusing the uv Command
Problem

You try to check the Python version inside uv by running:

uv python version


or simply:

uv python


…and it does not give the version you expect.

Cause

uv does not execute commands by default.

Typing uv python version or just uv python only references uv itself, but it does not run Python.

This is a very common oversight for beginners using uv for the first time.

Correct Usage

To run any Python command inside the uv-managed environment, you must use:

uv run python --version


Key points:

Always use uv run before the command you want to execute.

This applies to any Python commands (scripts, Jupyter, package installation, etc.).

Summary

uv run is the gateway command — without it, uv will not execute anything in the isolated environment, and your commands will either fail or use the wrong Python version.
