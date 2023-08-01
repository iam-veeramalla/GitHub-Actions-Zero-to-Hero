import subprocess
import re

def get_latest_tag():
    try:
        tags_output = subprocess.check_output(["git", "ls-remote", "--tags", "origin"])
        tags_list = tags_output.decode("utf-8").strip().split("\n")
        latest_tag = max(tags_list, key=lambda x: [int(d) for d in re.findall(r'\d+', x)])
        return latest_tag.strip()
    except subprocess.CalledProcessError:
        raise RuntimeError("Failed to get the latest GitHub tag.")

def symmetric_increment_version(version):
    match = re.match(r'^(\d+)\.(\d+)\.(\d+)$', version)
    if not match:
        raise ValueError(f"Invalid version format: {version}. Expected 'major.minor.patch'.")

    major, minor, patch = map(int, match.groups())
    new_version = f"{minor}.{major}.{patch}"
    return new_version

def create_git_tag(version):
    subprocess.run(["git", "tag", version])
    subprocess.run(["git", "push", "origin", version])

def main():
    try:
        latest_tag = get_latest_tag()
        print(f"Latest GitHub tag: {latest_tag}")

        new_version = symmetric_increment_version(latest_tag)
        print(f"New symmetric version: {new_version}")

        create_git_tag(new_version)
        print(f"Git tag '{new_version}' created and pushed.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
