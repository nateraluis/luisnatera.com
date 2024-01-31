from mastodon import Mastodon
import datetime
import os
import re
from create_post import authenticated_github, get_issue


def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


def get_favourites():
    mastodon = Mastodon(access_token=os.environ["MASTODON_ACCESS_TOKEN"],
                        api_base_url=os.environ["MASTODON_BASE_URL"])
    return mastodon.favourites()


def write_favourites(issue, favourites):
    previous_date = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=7)
    previous_date = previous_date.replace(hour=0, minute=0, second=0, microsecond=0)

    for status in favourites:
        if status['created_at'] >= previous_date:
            content = remove_html_tags(status['content'])
            url = status['url'].strip()
            text = f"#Mastodon [{content}]({url})"
            issue.create_comment(text)


def main():
    g = authenticated_github()
    issue = get_issue(g)
    favourites = get_favourites()
    write_favourites(issue, favourites)


if __name__ == "__main__":
    main()
