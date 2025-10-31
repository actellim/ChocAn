# Git Cheatsheet

## **Inspection & Status**

*   **See your local branches:**
    ```bash
    git branch
    ```

*   **See all local and remote-tracking branches:**
    ```bash
    git branch -a
    ```

*   **Check the status of your changes (untracked, modified, staged):**
    ```bash
    git status
    ```

*   **View commit history for your current branch:**
    ```bash
    git log
    ```

*   **Clean up stale remote-tracking branches that were deleted on the remote:**
    ```bash
    git fetch origin --prune
    ```

---

## Semantic Versioning Tags

* Create an annotated tag
    ```bash
    git tag -a v1.2.3 -m "Release v1.2.3"
    ```

* Push the tag (explicit)
    ```bash
    git push origin v1.2.3
    ```

* Push all tags (batch)
    ```bash
    git push origin --tags
    ```

* Push tags that are reachable by the commits you just pushed
    ```bash
    git push --follow-tags
    ```

* List all tags
    ```bash
    git tag
    ```

* Show tag details
    ```bash
    git show v1.2.3
    ```

* Delete a tag locally and remotely
    ```bash
    git tag -d v1.2.3
    git push --delete origin v1.2.3
    ```

---

## **Local Workflow (The Day-to-Day Loop)**

*   **Create a new branch and immediately switch to it:**
    ```bash
    git checkout -b <branch-name>
    ```

*   **Switch between existing branches (without a custom script):**
    ```bash
    git checkout <branch-name>
    ```

*   **Switch between your existing branches (using your custom script):**
    ```bash
    ./switch.sh <branch-name>
    ```

*   **Stage all changes in the current directory for the next commit:**
    ```bash
    git add .
    ```

*   **Commit your staged changes to the branch's history:**
    ```bash
    git commit -m "Your clear and concise commit message"
    ```

*   **Revert your changes to the remote branch:**
    ```bash
    git checkout -- <filename>
    ```

---

## **Remote Repository Setup & Tracking**

- **Add a remote (SSH)**  
  ```bash
  git remote add origin git@gogs.example.com:username/repo.git
  ```
  *(Replace `username/repo` with your repo’s path.)*

- **Add a remote (HTTPS)**  
  ```bash
  git remote add origin https://gogs.example.com/username/repo.git
  ```

- **Change the URL of an existing remote**
	```bash
	# Replace <remote> with the remote name (e.g., origin)
	# Replace <new‑url> with the new repository URL
	git remote set-url <remote> <new‑url>
	```

- **Verify the remote URL**  
  ```bash
  git remote -v
  ```

- **Change the remote URL** (e.g., switch from HTTPS to SSH)  
  ```bash
  git remote set-url origin git@gogs.example.com:username/repo.git
  ```

- **Clone a repository from Gogs**  
  ```bash
  git clone git@gogs.example.com:username/repo.git
  ```

- **Generate and add an SSH key for Gogs**  
  ```bash
  # Generate a key pair (if you don’t already have one)
  ssh-keygen -t ed25519 -C "you@example.com"

  # Copy the public key to your clipboard
  cat ~/.ssh/id_ed25519.pub | pbcopy   # macOS
  cat ~/.ssh/id_ed25519.pub | xclip -selection clipboard  # Linux

  # In Gogs → Settings → SSH Keys, paste the key.
  ```

- **Set the upstream tracking for a local branch**  
  ```bash
  # If the branch already exists locally
  git branch --set-upstream-to=origin/<branch> <branch>

  # Or, push a new branch and set tracking in one step
  git push -u origin <branch>
  ```

- **Pull the latest changes from the upstream**  
  ```bash
  git pull
  ```

- **Fetch all branches from the remote without merging**  
  ```bash
  git fetch origin
  ```

- **Show all remote‑tracking branches**  
  ```bash
  git branch -r
  ```

- **Prune stale remote‑tracking branches**  
  ```bash
  git remote prune origin
  ```

- **Delete a remote branch**  
  ```bash
  git push origin --delete <branch>
  ```

- **Delete a local branch**  
  ```bash
  git branch -d <branch>
  ```

- **Get detailed info about the remote**  
  ```bash
  git remote show origin
  ```

> **Tip** – If you’ve already cloned a repo, you can add or change the remote instead of re‑cloning:

```bash
git init
git remote add origin git@gogs.example.com:username/repo.git
```

> **Tip** – After the first push of a branch, the `-u` flag tells Git to record the upstream so subsequent `git pull`/`git push` calls work without arguments.

---

## **Remote Workflow (Collaboration & Multi-Computer)**

*   **Get the latest changes from the remote branch and merge them into your local branch:**
    ```bash
    git pull
    ```

*   **Push your new branch to the remote for the first time (sets up tracking):**
    ```bash
    git push -u origin <branch-name>
    ```

*   **Push your latest commits to the already-pushed remote branch:**
    ```bash
    git push
    ```

*   **Fetch a branch from the remote that you don't have locally:**
    ```bash
    git fetch origin
    git checkout <branch-name>
    ```

---

## **Cleanup (After Your Pull Request is Merged)**

*   **Safely delete the local branch (will warn if not merged):**
    ```bash
    # First, switch back to main
    ./switch.sh main
    # Then delete the feature branch
    git branch -d <branch-name>
    ```

*   **Delete the branch from the remote repository:**
    ```bash
    git push origin --delete <branch-name>
    ```

---

## Removing Tracked Files That Are Now Ignored

- **Commit any pending .gitignore changes**.
	```bash
	git add .gitignore
	git commit -m "Update .gitignore – add new ignored patterns"
	```
	
- **Un‑track all files that match the new ignore rules.**
	– This keeps the files locally, but removes them from the repo.
	```bash
	git rm -r --cached $(git ls-files -i -c --exclude-standard)
	```
	- If you only want to remove a single file:
	```bash
	git rm --cached path/to/file
	```

- **Verify what got staged for removal**
	```bash
	git status  # you should see the files marked for deletion
	```
	
- **Commit the removal**.
	```bash
	git commit -m "Remove ignored files from repository"
	```

- **Push the changes to the remote**.
	```bash
	git push
	```

### Quick sanity check

```bash
git log --oneline -n 3      # see your recent commit
git status --ignored        # view the list of ignored files
```

### Cleaning up your local working tree (optional)

If you also want to delete the ignored files from *your* disk, run:

```bash
git clean -fdx  # removes all untracked and ignored files/folders
```

> **Tip** – `git ls-files -i --exclude-standard` lists *all* ignored files that are currently tracked.  
> It’s handy for bulk operations, but you can also target individual paths with `git rm --cached`.

