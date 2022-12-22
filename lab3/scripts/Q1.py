import os

h = "04ebf0f4fe539ed72643bd01546aeaf372fdc1bd558e92afcc8c6078d4e5becd"

print(f"Looking for matches: {h}")

for file in os.listdir("./Q1files"):
    if os.path.isfile(os.path.join("./Q1files", file)):
        sha256sum = os.system("sha256sum " + os.path.join("./Q1files", file))