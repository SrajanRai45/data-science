🧠 Lightweight Data Science Environment (Without Anaconda)
⚡ Overview

This repository provides a lightweight, cross-platform Python environment for running Data Science and Jupyter Notebook workflows — without relying on Anaconda.
It uses the uv package manager, which is faster, simpler, and avoids dependency conflicts that often occur in heavy distributions like Anaconda.

💡 Motivation

Anaconda is a great tool for beginners, but it comes with several drawbacks:

🧱 Too Heavy: Installs hundreds of packages by default.

⚙️ Complex Configuration: Requires additional setup for environments and PATH management.

🔐 Conflicts on Linux: Keyring and cryptographic issues can occur during setup.

🧩 Slow Updates: Package management can become cumbersome with large environments.

To solve this, I created a custom environment using uv, which is minimal, clean, and portable across any system — whether Linux, Windows, or macOS.

🧰 Features

✅ Fully supports Jupyter Notebook without Anaconda
✅ Works on any OS (Linux, macOS, Windows)
✅ Uses uv for fast package installation
✅ Keeps the environment lightweight and reproducible
✅ Ideal for Data Science, ML, or AI experimentation

🪄 Setup Instructions
1️⃣ Install uv

You can install uv globally using:

curl -LsSf https://astral.sh/uv/install.sh | sh


(For Windows, follow the instructions on the official UV docs.)

2️⃣ Create a Virtual Environment

Inside your project directory:

uv venv .venv


Activate the environment:

source .venv/bin/activate   # For Linux/macOS
# or
.venv\Scripts\activate      # For Windows

3️⃣ Install Jupyter and Required Packages

Use the fast installer via uv:

uv pip install jupyter numpy pandas matplotlib scikit-learn


You can also install additional libraries later:

uv pip install seaborn plotly scipy

4️⃣ Launch Jupyter Notebook

Once all dependencies are installed:

jupyter notebook


You can now create and run notebooks directly from this environment 🎉

🧾 Example Usage

Open a new notebook and test your setup:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.random.randn(100)
plt.hist(data, bins=20)
plt.show()


If it runs without issues — congrats 🎊 you’ve got a fully working data science environment without Anaconda!

🧱 Why uv?
Feature	Anaconda	uv
🪶 Lightweight	❌ Heavy	✅ Extremely Light
⚡ Speed	❌ Slow	✅ Fast (Rust-based)
🔁 Reproducibility	⚠️ Partial	✅ Deterministic
🧩 Setup Complexity	❌ High	✅ Minimal
🔐 Linux Conflicts	❌ Common	✅ None
🌐 Cross-Platform Compatibility

This setup is designed to run smoothly on:

🐧 Linux (Tested on Arch & Ubuntu)

🪟 Windows 10/11

🍎 macOS (Intel & Apple Silicon)

💬 Notes

You don’t need to modify .bashrc or any system files.

The environment remains isolated and doesn’t interfere with system-level Python.

You can export dependencies easily:

uv pip freeze > requirements.txt


and reinstall them elsewhere:

uv pip install -r requirements.txt

🧑‍💻 Author

Srajan Rai (CreaZone/SrajanRai45) 
🎓 Computer Science (Data Science) @ Gyan Ganga Institute of Technology, Jabalpur
💡 Passionate about AI, Game Development, and Efficient Tooling
