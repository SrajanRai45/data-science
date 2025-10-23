⚙️ Project Setup Guide

This document explains how to set up and manage the Python environment for this project. It provides details about the tools used — Python, MISC, and uv — and how they interact with each other.

For this specific project, we are using the uv installation method, as it offers a simple, isolated, and highly reproducible setup environment.

1. Overview

Python environments can be managed in several ways, depending on the tools available on your system. In this documentation, we discuss three key components:

Pre-installed Python – the system-level Python that ships with your operating system.

MISC – a Python version manager that handles global installations.

uv – a modern, high-performance environment manager used to isolate project dependencies.

2. Pre-installed Python

Most operating systems (Windows, Ubuntu, Arch Linux, etc.) come with Python pre-installed.

For this project, the base system is OMARCHY, a developer-focused Linux distribution based on Arch and created by DHS, the developer of Ruby on Rails.
OMARCHY includes its own Python installation, which we are not modifying.

This system-level Python is left untouched because:

It ensures that system tools and applications depending on Python remain stable.

It avoids unnecessary conflicts with our project environments.

> **Official Documentation:** [Python Documenn](https://docs.python.org/3/)


3. MISC – The Global Python Manager

MISC is a Python version manager that allows you to install, switch, and manage different Python versions globally.
It is especially useful if you work with multiple projects requiring different Python releases.

When installed, MISC overrides the system Python and manages all Python versions through configuration files such as:

python.version

project.toml

These files specify which Python version to use for the current directory or project.

In this setup, MISC handles global installs, keeping the system clean and allowing uv to handle per-project environments.

> **Official Documentation:** [MISC Documentation](https://github.com/misc-python/misc)

 (Replace this link with the actual one if you have the correct source.)

4. uv – The Isolated Project Environment Manager

For this project, we are exclusively using uv to create and manage our local environment.
uv is designed to be extremely fast and isolated — meaning it doesn’t depend on or conflict with system-wide Python installations or MISC-managed versions.

Key Advantages of uv

Complete isolation from the system environment

Fast installation and dependency resolution

Easy to reproduce and share environments

Works seamlessly with Jupyter and data science tools

Basic uv Commands
Install a specific Python version
uv python install 3.12

Pin the version for reproducibility
uv python pin 3.12

Run Python inside the uv environment
uv run python --version


Important:
Unlike normal setups, you must use uv run before your commands.
Running python directly will not use uv’s isolated environment.

Why We Prefer uv

We are using uv because it isolates everything — meaning no conflicts with other tools, Python versions, or global packages.

You can even run uv without MISC or native Python installed. uv downloads and manages its own environment internally.
However, combining MISC + uv can lead to unnecessary complexity. While it is technically possible to make them work together, it becomes harder to maintain and may require advanced troubleshooting if conflicts occur.

Keeping MISC for global control and uv for project isolation is the most practical and health-friendly setup — avoiding stress from dependency or version mismatches.

> **Official Documentation:** [uv Documentation](https://docs.astral.sh/uv/)


5. Installing Project Dependencies

After uv is set up, install the required libraries for this project:

uv add numpy pandas matplotlib seaborn jupyterlab


To launch Jupyter Lab within the same environment:

uv run jupyter lab


This ensures that all dependencies are used from the uv-managed environment, keeping your workspace consistent.

6. Project Structure

The following structure is recommended for clarity and scalability:

project-root/
│
├── src/                     # Source code and Jupyter notebooks
│   ├── notebook_1/
│   ├── notebook_2/
│   └── ...
│
├── docs/                    # Documentation files
│   ├── setup.md
│   └── troubleshooting.md
│
├── pyproject.toml           # uv project configuration
└── README.md


Each folder inside src/ can represent one notebook or mini-project, depending on your workflow.

7. Summary
Tool	Purpose	Use Case	Notes
Pre-installed Python	System-level Python	Used by OS and core applications	Keep untouched
MISC	Global Python version manager	Manages versions across projects	Optional in this setup
uv	Project environment manager	Creates isolated, fast, reproducible setups	Primary tool for this project
8. Final Notes

Keep your global setup simple. Use MISC only if you handle multiple global Python projects.

Prefer uv for project-level work — it reduces breakages, version issues, and environmental clutter.

Avoid combining multiple managers unless absolutely necessary.

This configuration ensures that your system remains clean and your projects stay reproducible and isolated.
