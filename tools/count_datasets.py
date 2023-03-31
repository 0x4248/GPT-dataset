import os

if __name__ == "__main__":
    count = 0
    for file in os.listdir("dataset"):
        if os.path.isdir("dataset/"+file):
            count += 1
    with open("README.md", "r") as f:
        readme = f.read()
    lines = readme.split("\n")
    lines[4] = "There are `"+str(count)+"` datasets in this repository"
    with open("README.md", "w") as f:
        f.write("\n".join(lines))
