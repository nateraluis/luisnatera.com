import os
from collections import defaultdict
import datetime

from github import Github
from rich import print


def authenticated_github():
    g = Github(os.environ['TOKEN_ISSUES'])
    return g


def get_issue(g):
    repo = g.get_repo("nateraluis/nateraluis.github.io")
    issue = repo.get_issues(state="open", labels=["weekly"])[0]
    return issue


def get_content_from_issue(issue):
    content = defaultdict(list)
    for comment in issue.get_comments():
        for word in comment.body.split():
            if "#" in word:
                content[word].append(comment.body.replace(word, ""))
    return content


def write_content_to_post(content):
    current_date = datetime.datetime.now().isoformat()[:10]
    with open(f"_posts/{current_date}-weekly.md", "w") as f:
        for key in ['about', 'twitter', 'web']:
            if key in content:
                if key != 'about':
                    f.write(f"# {key.capitalize()}\n")
                for text in content[f"#{key}"]:
                    f.write(f"{text}\n")
                f.write("\n")
    print(f"✅ {current_date}-weekly.md post written.")


def main():
    g = authenticated_github()
    issue = get_issue(g)
    content = get_content_from_issue(issue)
    write_content_to_post(content)


if __name__ == "__main__":
    main()
