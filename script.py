import os
import random
import datetime

# 🔹 Change this to your SoftwareDeveloperSalaryPrediction repository path
REPO_PATH = os.path.expanduser("~/Desktop/GitProject/SoftwareDeveloperSalaryPrediction")  # Update if needed

# 🔹 Number of commits to generate
NUM_COMMITS = random.randint(30, 70)  # Random between 180-350 commits

# 🔹 Your GitHub username (SSH will handle authentication)
GIT_USERNAME = "premalshah999"

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

# Function to create and push commits
def make_commit(commit_date, commit_message):
    os.chdir(REPO_PATH)  # Move to repo folder

    # Create or update a dummy file
    with open("commit_log.txt", "a") as file:
        file.write(f"{commit_date}: {commit_message}\n")

    # Add changes to Git
    os.system("git add .")
    os.system(f'GIT_AUTHOR_DATE="{commit_date}" GIT_COMMITTER_DATE="{commit_date}" git commit -m "{commit_message}"')

# Set Git username (SSH handles authentication)
os.system(f'git config user.name "{GIT_USERNAME}"')

# Get the current branch name
branch_name = os.popen("git rev-parse --abbrev-ref HEAD").read().strip()

# Generate commits for 2022 & 2023
for _ in range(NUM_COMMITS):
    random_year = random.choice([2022, 2023])  # Choose either 2022 or 2023
    random_days = random.randint(0, 364)  # Random day of the year
    random_time = datetime.timedelta(hours=random.randint(0, 23), minutes=random.randint(0, 59))

    commit_date = datetime.datetime(random_year, 1, 1) + datetime.timedelta(days=random_days) + random_time
    commit_message = random.choice(COMMIT_MESSAGES)  # Choose a random commit message

    make_commit(commit_date.strftime("%Y-%m-%dT%H:%M:%S"), commit_message)

# Push all commits to GitHub using SSH
os.system(f"git push origin {branch_name}")
