# GPT code repository
# This repository contains data that ChatGPT has created.
# Github: https://www.github.com/0x4248/GPT-dataset
# By: 0x4248

import random
import shutil
import os
import pandas as pd

def convert_to_csv(file):
    # Convert the Markdown table to a list of lists
    with open(file) as f:
        rows = []
        for row in f.readlines():

            # Get rid of leading and trailing '|'
            tmp = row[1:-2]
            # Split line and ignore column whitespace
            clean_line = [col.strip() for col in tmp.split('|')]
            # Append clean row data to rows variable
            rows.append(clean_line)
        # Get rid of syntactical sugar to indicate header (2nd row)
        rows = rows[:1] + rows[2:]
    print(rows)
    df = pd.DataFrame(rows)
    df.to_csv(file, index=False, header=False)

if __name__ == "__main__":
    print("Welcome to GPT dataset")
    print("Please copy the table from Chat GPT and paste it into ADD_TO_DATASET.csv")
    print("Press enter when done")
    open("ADD_TO_DATASET.csv", "w").close()
    input(">")
    id = random.randint(1000, 9999)
    os.mkdir("dataset/"+str(id))
    shutil.move("ADD_TO_DATASET.csv", "dataset/"+str(id)+"/data.csv")
    shutil.copy("dataset/"+str(id)+"/data.csv", "dataset/"+str(id)+"/data.md")
    print("What is the prompt that you entered into Chat GPT?")
    prompt = input(">")
    open("dataset/"+str(id)+"/prompt.txt", "w").write(prompt)
    print("Converting to CSV")
    convert_to_csv("dataset/"+str(id)+"/data.csv")
    print("Creating readme in dataset")
    with open("dataset/"+str(id)+"/README.md", "w") as f:
        f.write("# GPT Dataset "+str(id)+"\n")
        f.write("## Prompt\n")
        f.write("```\n")
        f.write(prompt+"\n")
        f.write("```\n")
        f.write("## Columns\n")
        with open("dataset/"+str(id)+"/data.csv", "r") as data:
            columns = data.readline()
            for column in columns.split(","):
                f.write("- "+column+"\n")   
        f.write("## Data\n")
        with open("dataset/"+str(id)+"/data.md", "r") as data:
            f.write(data.read()+"\n")
    os.remove("dataset/"+str(id)+"/data.md")
    print("Done")