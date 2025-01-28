
# Git and GitHub: A Complete Guide

## What is Git?

Git is a distributed version control system that allows developers to track changes to files and collaborate with others on software development projects.

GitHub is a platform that hosts Git repositories in the cloud, making it easier to share and collaborate on projects.

## 1. Creating a GitHub Account

To get started with Git and GitHub, you’ll need a GitHub account:

1. **Go to GitHub**: Open your browser and navigate to [https://github.com](https://github.com).
2. **Sign Up**: Click the **Sign up** button on the homepage.
   - Provide your **username**, **email address**, and **password**.
   - Follow the prompts to complete the registration process (you may need to verify your email).
3. **Set Up Your Profile**: Once registered, you can customize your profile, add a bio, profile picture, etc.
4. **Create a New Repository**: After logging in, you can create a new repository to store your code.

   To create a repository:
   - Go to your **GitHub homepage**.
   - Click the **+** icon in the upper-right corner and select **New repository**.
   - Give it a name, choose whether it's public or private, and initialize it with a README if you want.
   - Click **Create repository**.

## 2. Installing Git

### On Windows:
- Download and install Git from [git-scm.com](https://git-scm.com/download/win).
- Open **Git Bash** after installation to start using Git.

### On macOS:
- Use Homebrew: `brew install git`
- Or download from [git-scm.com](https://git-scm.com/download/mac).

### On Linux:
- On Ubuntu/Debian: `sudo apt install git`
- On Fedora: `sudo dnf install git`

To check if Git is installed correctly:
```bash
git --version
```

## 3. Basic Configuration

Once Git is installed, set your name and email (this information will appear in your commits):
```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

You can verify your configuration:
```bash
git config --list
```

## 4. Creating a New Git Repository

### Initialize a New Repository Locally

1. Navigate to your project folder:
   ```bash
   cd path/to/your/project
   ```

2. Initialize the Git repository:
   ```bash
   git init
   ```

   This will create a `.git` directory where Git will track changes.

### Clone an Existing Repository from GitHub

If you want to clone an existing repository from GitHub, use:
```bash
git clone https://github.com/username/repository.git
```

This will create a local copy of the repository on your machine.

## 5. Staging and Committing Changes

### View Changes
To see what has changed in your repository:
```bash
git status
```

### Staging Changes
Before committing, you need to stage the changes. To stage a single file:
```bash
git add <filename>
```

To stage all changes:
```bash
git add .
```

### Committing Changes
Once your changes are staged, you can commit them:
```bash
git commit -m "Your commit message"
```

## 6. Pushing Changes to GitHub

After committing changes locally, you can push them to GitHub:

```bash
git push origin main
```

> `origin` is the default name for the remote repository, and `main` is the default branch name.

If this is your first time pushing, Git will prompt you for your GitHub credentials.

## 7. Pulling Changes from GitHub

To pull the latest changes from a GitHub repository into your local copy:
```bash
git pull origin main
```

## 8. Branching and Merging

### Creating a New Branch
To create and switch to a new branch:
```bash
git checkout -b new-branch-name
```

### Switching Between Branches
To switch to an existing branch:
```bash
git checkout branch-name
```

### Merging Branches
To merge a branch into your current branch:
```bash
git merge branch-name
```

> **Note:** If there are merge conflicts, Git will prompt you to resolve them manually.

## 9. Viewing History

To view the commit history of your repository:
```bash
git log
```

For a more compact history:
```bash
git log --oneline
```

## 10. Undoing Changes

### Undo Staged Changes
To unstage changes (but keep them in your working directory):
```bash
git reset <filename>
```

### Undo Last Commit
If you want to undo the last commit (and keep the changes in your working directory):
```bash
git reset --soft HEAD~1
```

To undo the last commit and discard changes:
```bash
git reset --hard HEAD~1
```

> **Warning:** `git reset --hard` will permanently discard changes.

## Conclusion

With these basics, you're ready to start using Git and GitHub! You'll be able to track your code changes, collaborate with others, and manage different versions of your project. Once you're comfortable with these basic commands, you can explore more advanced Git features like rebasing, stashing, and working with remotes.

Happy coding! 🚀
```
