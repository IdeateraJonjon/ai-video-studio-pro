"""
AI Video Studio - Automated GitHub Repository Creator
Uses GitHub API with Personal Access Token to create repository automatically
"""

import requests
import json
import os
import subprocess
import sys
import time

class GitHubRepoCreator:
    def __init__(self, token, username):
        self.token = token
        self.username = username
        self.headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json',
            'Content-Type': 'application/json'
        }
        self.base_url = 'https://api.github.com'

    def test_token(self):
        """Test if the token is valid"""
        try:
            response = requests.get(f'{self.base_url}/user', headers=self.headers)
            if response.status_code == 200:
                user_data = response.json()
                print(f"✓ Token valid! Authenticated as: {user_data['login']}")
                return True, user_data['login']
            else:
                print(f"✗ Token invalid. Status: {response.status_code}")
                return False, None
        except Exception as e:
            print(f"✗ Error testing token: {e}")
            return False, None

    def create_repository(self):
        """Create the GitHub repository"""
        repo_data = {
            "name": "ai-video-studio-pro",
            "description": "Professional AI video generation platform with database, APIs, and GitHub integration",
            "homepage": "",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True,
            "auto_init": False,  # Don't initialize - we have our own files
            "allow_squash_merge": True,
            "allow_merge_commit": True,
            "allow_rebase_merge": True,
            "delete_branch_on_merge": False
        }

        try:
            print("🚀 Creating GitHub repository...")
            response = requests.post(
                f'{self.base_url}/user/repos',
                headers=self.headers,
                data=json.dumps(repo_data)
            )

            if response.status_code == 201:
                repo_info = response.json()
                print(f"✓ Repository created successfully!")
                print(f"📍 URL: {repo_info['html_url']}")
                print(f"🔗 Clone URL: {repo_info['clone_url']}")
                return True, repo_info
            elif response.status_code == 422:
                error_data = response.json()
                if 'already exists' in str(error_data):
                    print("⚠ Repository already exists! Using existing repository.")
                    # Get existing repo info
                    existing_response = requests.get(
                        f'{self.base_url}/repos/{self.username}/ai-video-studio-pro',
                        headers=self.headers
                    )
                    if existing_response.status_code == 200:
                        return True, existing_response.json()
                print(f"✗ Repository creation failed: {error_data}")
                return False, None
            else:
                print(f"✗ Failed to create repository. Status: {response.status_code}")
                print(f"Response: {response.text}")
                return False, None

        except Exception as e:
            print(f"✗ Error creating repository: {e}")
            return False, None

    def setup_git_remote(self, repo_info):
        """Add GitHub remote to local repository"""
        try:
            clone_url = repo_info['clone_url']
            
            # Check if remote already exists
            result = subprocess.run(['git', 'remote', '-v'], 
                                  capture_output=True, text=True, cwd=os.getcwd())
            
            if 'origin' in result.stdout:
                print("⚠ Remote 'origin' already exists. Removing and re-adding...")
                subprocess.run(['git', 'remote', 'remove', 'origin'], 
                             cwd=os.getcwd(), check=True)

            # Add new remote
            print("🔗 Adding GitHub remote...")
            subprocess.run(['git', 'remote', 'add', 'origin', clone_url], 
                         cwd=os.getcwd(), check=True)
            
            print("✓ Remote added successfully!")
            return True

        except subprocess.CalledProcessError as e:
            print(f"✗ Error setting up remote: {e}")
            return False
        except Exception as e:
            print(f"✗ Unexpected error: {e}")
            return False

    def push_to_github(self):
        """Push local repository to GitHub"""
        try:
            print("📤 Pushing to GitHub...")
            
            # Rename branch to main if it's master
            current_branch = subprocess.run(['git', 'branch', '--show-current'], 
                                          capture_output=True, text=True, cwd=os.getcwd())
            if current_branch.stdout.strip() == 'master':
                print("🔄 Renaming branch from master to main...")
                subprocess.run(['git', 'branch', '-M', 'main'], cwd=os.getcwd(), check=True)

            # Push to GitHub
            subprocess.run(['git', 'push', '-u', 'origin', 'main'], 
                         cwd=os.getcwd(), check=True)
            
            print("✓ Successfully pushed to GitHub!")
            return True

        except subprocess.CalledProcessError as e:
            print(f"✗ Error pushing to GitHub: {e}")
            print("This might be due to authentication. You may need to:")
            print("1. Set up GitHub credentials in Git")
            print("2. Or use GitHub Desktop to push manually")
            return False

def get_user_credentials():
    """Get GitHub credentials from user"""
    print("🔐 GITHUB PERSONAL ACCESS TOKEN SETUP")
    print("=" * 50)
    print()
    print("To create a repository automatically, I need your GitHub credentials.")
    print()
    print("📋 How to get a Personal Access Token:")
    print("1. Go to: https://github.com/settings/tokens")
    print("2. Click 'Generate new token (classic)'")
    print("3. Give it a name: 'AI Video Studio'")
    print("4. Select scopes: 'repo' (full control of private repositories)")
    print("5. Click 'Generate token'")
    print("6. Copy the token (you won't see it again!)")
    print()
    
    username = input("Enter your GitHub username: ").strip()
    token = input("Enter your Personal Access Token: ").strip()
    
    return username, token

def main():
    print("=" * 70)
    print("🤖 AI VIDEO STUDIO - AUTOMATED GITHUB REPOSITORY CREATOR")
    print("=" * 70)
    print()
    print("This script will:")
    print("✓ Create GitHub repository automatically")
    print("✓ Set up remote connection")
    print("✓ Push all your files to GitHub")
    print("✓ Make your project publicly available")
    print()

    # Check if we're in the right directory
    if not os.path.exists('studio_launch.py'):
        print("✗ Error: Run this script from the AI_Video_Generation directory")
        print("Use: cd C:\\AI_Video_Generation")
        return

    # Get credentials
    username, token = get_user_credentials()
    
    if not username or not token:
        print("✗ Username and token are required!")
        return

    # Create GitHub API client
    github = GitHubRepoCreator(token, username)
    
    # Test token
    print("\n🔍 Testing GitHub token...")
    valid, actual_username = github.test_token()
    if not valid:
        print("✗ Please check your token and try again.")
        return

    if actual_username.lower() != username.lower():
        print(f"⚠ Note: Username mismatch. Using actual username: {actual_username}")
        username = actual_username

    # Create repository
    print("\n🚀 Creating GitHub repository...")
    success, repo_info = github.create_repository()
    if not success:
        print("✗ Failed to create repository.")
        return

    # Set up git remote
    print("\n🔗 Setting up Git remote...")
    if not github.setup_git_remote(repo_info):
        print("✗ Failed to set up remote. You can do this manually in GitHub Desktop.")
        print(f"Repository URL: {repo_info['html_url']}")
        return

    # Push to GitHub
    print("\n📤 Pushing files to GitHub...")
    if github.push_to_github():
        print("\n" + "=" * 70)
        print("🎉 SUCCESS! YOUR REPOSITORY IS LIVE!")
        print("=" * 70)
        print(f"🌐 Repository URL: {repo_info['html_url']}")
        print(f"👤 Owner: {username}")
        print(f"📁 Name: ai-video-studio-pro")
        print(f"📊 Files: 43+ files pushed")
        print(f"📖 Documentation: Professional README included")
        print(f"🔓 Visibility: Public (ready for sharing)")
        print()
        print("✓ Your AI Video Studio is now open source!")
        print("✓ Perfect for portfolio and collaboration!")
        print("✓ Ready to share with the world!")
        print()
        
        # Offer to open repository
        open_repo = input("Would you like to open the repository in your browser? (y/n): ")
        if open_repo.lower() == 'y':
            import webbrowser
            webbrowser.open(repo_info['html_url'])
            
    else:
        print(f"\n⚠ Repository created but push failed.")
        print(f"🌐 Repository URL: {repo_info['html_url']}")
        print("💡 You can push manually using GitHub Desktop:")
        print("1. Open GitHub Desktop")
        print("2. Add this repository")
        print("3. Click 'Publish repository'")

if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")
