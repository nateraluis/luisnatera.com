---
title: 'Automation'
date: 2024-02-01
permalink: /posts/2024/2/2024-02-01-automation-posts/
tags:
  - tech
  - GitHub
  - mastodon
  - automation
---

It has been a long time since the last time that I published a non week in review issue. To be precise, it has been since [The Amsterdam Paradox](https://buttondown.email/natera/archive/the-amsterdam-paradox-when-too-much-tourism/), back in June 22. This then, should be the come back. This issue will be a more meta one, and on the tech side of things, it is about automatising my workflow while writing the newsletter and my blog.

Back when I started writing the [week in review](https://luisnatera.com/tag#weekly) series I put together a workflow that allows me to use a GitHub issue to track the contents of the week in review, and then a GitHub action runs every Monday and collects the comments that I posted into the issue and based on logic that relies on hashtags builds the document and publishes into the blog. You can [read more about it here](https://luisnatera.com/posts/2022/9/github-actions-for-automating-blog-posts/). Since then I have been thinking on different ways that I can leverage small scripts to facilitate my writing workflow. The main one -still in planning stage- is making sure that what I publishes directly into [my blog](https://luisnatera.com) goes directly into the newsletter, as at the moment I have to copy/paste between systems. But that's for another time. The new addition: automate adding the Mastodon content that I found insightful during the week into the week in review.

I started thinking about automating adding Mastodon posts into the week in review as I was copy/pasting and adding the links, it was not a difficult task, but it takes some time, and there were some times that I forgot about doing it. So I decided to do what any lazy programmer would do, automate it. The idea, have a script that every Monday, before the week in review gets build and published, retrieves my favourite Mastodon posts from the week, and populate the GitHub issue with the posts texts and links back to the original posts. The solution: a Python script that is executed every Monday by a GitHub Action.

To get more into details, I used [Mastodon.py](https://github.com/halcy/Mastodon.py) to interact with my Mastodon account using Python, then get my favourite posts, filter by the week, and post the favourited ones into the GitHub Issue.

I imported some functions from my post-building automation script (DRY 😉) to authenticate in GitHub, and retrieve the issue, then with the bellow function got my favourites posts:

```python
from mastodon import Mastodon


def get_favourites():
    mastodon = Mastodon(access_token=os.environ["MASTODON_ACCESS_TOKEN"],
                        api_base_url=os.environ["MASTODON_BASE_URL"])
    return mastodon.favourites()
```

Once that I had the favourited posts, I use a helper function to clean the HTML tags from the texts, and write the contents from the Mastodon post with their links into the GitHub Issue with the bellow functions:

```python
import datetime
import os
import re


def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


def write_favourites(issue, favourites):
    previous_date = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=7)
    previous_date = previous_date.replace(hour=0, minute=0, second=0, microsecond=0)

    for status in favourites:
        if status['created_at'] >= previous_date:
            content = remove_html_tags(status['content'])
            url = status['url'].strip()
            text = f"#Mastodon [{content}]({url})"
            issue.create_comment(text)
```

The new 39 lines of Python script allows now for a new automation of the newsletter, making sure that every week new links are populated, and integrates directly into my use of Mastodon.

While working on complex coding projects is interesting, I still find very rewarding working on this small coding pieces that allows me to automatise certain parts of my workflows. By a quick calculation this lines of code might save me 3 to 5 minutes per week, compounding to 3,9 hours per year. Might be a small impact in terms of time, but it definitely has a big impact in terms of facilitating my workflow.

I hope this small script/functions are useful to someone, or at least it inspires you to try to automatise some tasks. If you do have any workflows that have automatised, or are looking for ideas, let me know. I'll be happy to hear from you.
