import sys
import re

def extract_target_user(old_content, new_content):
    """
    Extracts the GitHub username from the new content
    if it differs from the old content.
    Format expected: 'hello <github_id>' or 'hi <github_id>'
    """
    pattern = r"(hello|hi)\s+([a-zA-Z0-9_-]+)"
    old_match = re.search(pattern, old_content)
    new_match = re.search(pattern, new_content)

    if new_match and old_match:
        old_user = old_match.group(2)
        new_user = new_match.group(2)
        if new_user != old_user:
            return new_user
    elif new_match:
        return new_match.group(2)
    return None

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python test.py old.txt new.txt")
        sys.exit(1)

    with open(sys.argv[1], 'r') as f1, open(sys.argv[2], 'r') as f2:
        old_content = f1.read()
        new_content = f2.read()
        result = extract_target_user(old_content, new_content)
        if result:
            print(result)
        else:
            print("no_user_found")
