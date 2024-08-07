import datetime
import os
from collections import defaultdict

from github import Github
from rich import print


def authenticated_github():
    g = Github(os.environ["TOKEN_ISSUES"])
    return g


def get_issue(g):
    repo = g.get_repo("nateraluis/luisnatera.com")
    issue = repo.get_issues(state="open", labels=["weekly"])[0]
    return issue


def get_content_from_issue(issue):
    content = defaultdict(list)
    for comment in issue.get_comments():
        for word in comment.body.split():
            if "#" in word:
                content[word].append(comment.body.replace(word, ""))
    if len(content) > 0:
        return content
    return None


def write_content_to_post(content):
    current_date = datetime.datetime.now().isoformat()[:10]
    with open(f"_posts/{current_date}-weekly.md", "w") as f:
        f.write(
            f"---\ntitle: 'Week in Review {current_date}'\ndate: {current_date}\n"
            f"permalink: /posts/{datetime.datetime.now().year}/{datetime.datetime.now().month}/{current_date}-review/\n"
            "tags:\n  - weekly\n  - review\n  - automated\n"
            "---\n"
        )
        tags = [k[1:] for k in content.keys()]
        tags.sort(key=str.casefold)
        for key in tags:
            print(f"✍️ Writing {key}")
            if key != "about":
                f.write(f"## {key.capitalize()}\n")
            for text in content[f"#{key}"]:
                if key != "about":
                    f.write(f"- {text}\n")
                else:
                    f.write(f"{text}\n")
            f.write("\n")
        f.write("***\n")
        f.write(
            "🤖 This post was generated automatically by the weekly script, using content curated in the "
            "[issues](https://github.com/nateraluis/nateraluis.github.io/issues) "
            "of my [repo](https://github.com/nateraluis/nateraluis.github.io/) in "
            "[GitHub](https://github.com/nateraluis)\n"
        )
    print(f"✅ {current_date}-weekly.md post written.")


def main():
    g = authenticated_github()
    issue = get_issue(g)
    content = get_content_from_issue(issue)
    if content is not None:
        write_content_to_post(content)
    else:
        print("❌ 📅 This week there is no content to write.")


if __name__ == "__main__":
    main()
