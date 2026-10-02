# GitHub Setup Guide

This guide contains instructions for setting up the GitHub features required to complete the treasure hunt for DecodeX. Since some problem statements are hidden within GitHub metadata (Issues, PRs, Commits, Branches, Releases) rather than files, you MUST perform these steps manually on the GitHub repository.

## Step 1: Create the 'experimental-sorting' branch (For PS 7)
1. In your local repository, create a new branch: `git checkout -b experimental-sorting`
2. Create the file `src/plugins/waste_sorter.md`.
3. Copy the content of `ORGANIZER_ONLY/PROBLEM_STATEMENTS/PS7.md` into this new file.
4. Commit the changes: `git add src/plugins/waste_sorter.md && git commit -m "Add waste sorter spec"`
5. Push the branch to GitHub: `git push origin experimental-sorting`
6. Switch back to the main branch: `git checkout main`

## Step 2: Create a dummy commit for Classroom Monitoring (For PS 4)
1. On the `main` branch, make a small dummy change to any file (e.g., add a newline to `src/main.py`).
2. Stage the change: `git add src/main.py`
3. Commit with the PS4 content in the body. You can do this by running `git commit`, which opens your editor, and then pasting the title as the commit message and the content of `ORGANIZER_ONLY/PROBLEM_STATEMENTS/PS4.md` as the commit body.
4. Push to GitHub.
*(Note: `src/main.py` mentions "Revert the classroom monitoring experiment (Commit message holds the details)". This commit is what participants will look for in the `git log`).*

## Step 3: Create GitHub Issue #4 (For PS 5)
1. Go to your repository on GitHub.
2. Navigate to the **Issues** tab and click **New Issue**.
3. Title the issue: `Feature Request: Silo Blueprint V2`.
4. In the description, paste the content of `ORGANIZER_ONLY/PROBLEM_STATEMENTS/PS5.md`.
5. Submit the issue.
*(Note: If you have created other issues first, ensure this one is specifically #4 as referenced in `config/settings.ini`)*.

## Step 4: Create a Closed Pull Request #12 (For PS 9)
1. Create a new branch: `git checkout -b early-warning-pr`
2. Make a dummy change (e.g., add a comment to `src/utils.py`).
3. Commit and push the branch.
4. Go to GitHub and open a Pull Request for this branch against `main`.
5. In the PR description, paste the content of `ORGANIZER_ONLY/PROBLEM_STATEMENTS/PS9.md`.
6. Once created, **Close** the PR without merging it.
*(Note: This creates the PR #12 referenced in `src/utils.py`. Make sure the PR number matches. Create dummy issues/PRs if needed to reach #12).*

## Step 5: Create a GitHub Release (For PS 10)
1. Go to your repository on GitHub.
2. Navigate to **Releases** and click **Draft a new release**.
3. Create a tag named `v0.9.0-cyclone-beta`.
4. Title the release `Beta Release: Cyclone Module`.
5. In the release notes description, paste the content of `ORGANIZER_ONLY/PROBLEM_STATEMENTS/PS10.md`.
6. Publish the release.

## Final Review
After completing these steps, the clues in the main repository files will point correctly to these GitHub-specific locations.
