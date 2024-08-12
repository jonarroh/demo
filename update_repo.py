import subprocess

def check_for_updates():
    try:
        # Fetch the latest changes from the remote repository
        subprocess.run(["git", "fetch"], check=True)
        
        # Check if the local branch is behind the remote branch
        result = subprocess.run(["git", "status", "-uno"], check=True, capture_output=True, text=True)
        
        # If the status message contains 'behind', it means there are updates
        if "behind" in result.stdout:
            print("There are updates available. Pulling changes...")
            subprocess.run(["git", "pull"], check=True)
            print("Updated successfully.")
        else:
            print("Already up to date.")
    
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    check_for_updates()
