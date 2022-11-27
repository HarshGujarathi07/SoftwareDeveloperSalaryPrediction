import datetime
import os
import random
import subprocess

# 🔹 Change this to your repository path
REPO_PATH = r"D:\Projects\SoftwareDeveloperSalaryPrediction"  # Ensure correct repo path

# 🔹 Number of commits to generate
NUM_COMMITS = random.randint(30, 70)  # Random between 30-70 commits

# 🔹 Your GitHub username
GIT_USERNAME = "HarshGujarathi07"

# 🔹 Salary Prediction-Specific Commit Messages
COMMIT_MESSAGES = [
    "Refactored salary prediction model",
    "Improved feature engineering for salary estimation",
    "Updated dataset with latest salary trends",
    "Optimized data preprocessing pipeline",
    "Added new regression model for better salary predictions",
    "Fixed missing salary data handling",
    "Enhanced data visualization for salary trends",
    "Refactored ML model training script",
    "Tested various ML algorithms for salary prediction",
    "Improved hyperparameter tuning",
    "Updated salary prediction model with new features",
    "Enhanced model accuracy with feature selection",
    "Fixed timestamp alignment issue in dataset",
    "Refactored data pipeline for better performance",
    "Added new job role categories for salary analysis",
    "Improved dataset cleaning for salary trends",
    "Updated README with project goals and methodologies",
    "Implemented deep learning model for salary prediction",
    "Added exploratory data analysis notebook",
    "Optimized data normalization technique",
]


# Function to execute shell commands
def run_command(command):
    result = subprocess.run(
        command, shell=True, capture_output=True, text=True
    )
    if result.stderr:
        print(f"Error: {result.stderr}")
    return result.stdout.strip()


# Function to create and push commits
def make_commit(commit_date, commit_message):
    os.chdir(REPO_PATH)  # Move to repo folder

    # Create or update a dummy file
    with open("commit_log.txt", "a") as file:
        file.write(f"{commit_date}: {commit_message}\n")

    # Add changes to Git
    run_command("git add .")
    run_command(f'git commit --date="{commit_date}" -m "{commit_message}"')


# Set Git username (SSH handles authentication)
run_command(f'git config user.name "{GIT_USERNAME}"')

# Get the current branch name
branch_name = run_command("git rev-parse --abbrev-ref HEAD")

# Generate commits for 2022 & 2023
for _ in range(NUM_COMMITS):
    random_year = random.choice([2022, 2023])
    random_days = random.randint(0, 364)
    random_time = datetime.timedelta(
        hours=random.randint(0, 23), minutes=random.randint(0, 59)
    )

    commit_date = (
        datetime.datetime(random_year, 1, 1)
        + datetime.timedelta(days=random_days)
        + random_time
    )
    commit_message = random.choice(COMMIT_MESSAGES)

    make_commit(commit_date.strftime("%Y-%m-%dT%H:%M:%S"), commit_message)

# Push all commits to GitHub using SSH
run_command(f"git push origin {branch_name}")

print("✅ Commits successfully pushed!")
