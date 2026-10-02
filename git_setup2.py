import os
import subprocess

def run_cmd(cmd, cwd="e:/repo"):
    subprocess.run(cmd, cwd=cwd, shell=True, check=True)

# 3. Back to master, setup PS4 (Commit message)
run_cmd("git checkout master")
with open("e:/repo/ORGANIZER_ONLY/PROBLEM_STATEMENTS/PS4.md", "r") as f:
    ps4_content = f.read()

# Add a dummy change to main.py
with open("e:/repo/src/main.py", "a") as f:
    f.write("\n# Debug: Classroom init\n")

run_cmd("git add src/main.py")

# Create a temporary file for the commit message
with open("e:/repo/commit_ps4.txt", "w") as f:
    f.write("Smart Classroom Attention and Engagement Monitoring System\n\n")
    f.write(ps4_content)

run_cmd("git commit -F commit_ps4.txt")
os.remove("e:/repo/commit_ps4.txt")

# 4. Setup PS9 (Branch for PR)
run_cmd("git checkout -b early-warning-pr")
with open("e:/repo/src/utils.py", "a") as f:
    f.write("\n# Ready for early warning PR integration\n")
run_cmd("git add src/utils.py")
run_cmd('git commit -m "Prepare early warning PR setup"')

# Return to master
run_cmd("git checkout master")

print("Local git setup complete.")
