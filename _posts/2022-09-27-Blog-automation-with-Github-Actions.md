---
title: 'GitHub Actions for Automating Blog Posts'
date: 2022-09-27
permalink: /posts/2022/9/github-actions-for-automating-blog-posts/
image: https://luisnatera.com/assets/img/github_actions_architecture.png
tags:
  - automation
  - github
  - python
---

As I started writing the [week in review,](https://luisnatera.com/tag#weekly) I wanted to automatize the process as much as possible. Reflecting on the work I have done in one week is not automatable, yet. However, building the post with the different elements needed can be automated.

The main idea was to have a system to track links I come across along the week, add a sentence about why I find the given item interesting, and provide a placeholder where I can work on a weekly reflection.

The goal was that once the week was over, the content was formatted and published.

My research started with Notion. I wanted to get to learn more about it. Soon, I realized that although it is a powerful system and offers a lot of flexibility, working with Notion was going to add more complexity by adding a new tool on top of my blog/site already hosted on GitHub. And I was not looking to add more complexity when the idea was to simplify the process.

I decided to base everything on GitHub. Using a weekly issue, to track the content I wanted to post about in the issue's comments. This way, I could organize one comment per item and classify them using text tags.

The first step was to automatize the creation and closing of weekly issues, for this I used the [Issue Bot by John Bohanno](https://github.com/imjohnbo/issue-bot), and using GitHub Actions, I scheduled a new post to be created every Monday, and close the issue from the previous week. This is what the weekly issue looks like:

![]({{site.imgsurl}}weekly_issue_example.png)

Having automated the creation of the issues was the first step. It provides a place to store the links and ideas. The next step was automating publishing the post every week.

To automatize posting the week in review. I used a Python port of the GitHub API. This way, I can programmatically access the active issue and its comments. I built a Python script that uses the API to retrieve issue, builds a dictionary with the content using the text tags to classify similar links (E.g. Twitter, web, Youtube), and writes the content into a Markdown file, structuring it as the post.

The script is run weekly via a GitHub Action that checkouts the repo, install the Python dependencies, executes the script and commits the new content into the repository.

The diagram of the different actions looks like this:

![]({{site.imgsurl}}github_actions_architecture.png)

All the actions and the Python script are available in the repository. The actions are under `github/workflows` [`weekly_note`](https://github.com/nateraluis/luisnatera.com/blob/main/.github/workflows/weekly_note.yml) for automating the creation of issues, and [`auto_post.yml`](https://github.com/nateraluis/luisnatera.com/blob/main/.github/workflows/auto_post.yml) for creating the post and posting it. The `auto_post.yml` action uses the [`create_post.py`](https://github.com/nateraluis/luisnatera.com/blob/main/scripts/create_post.py) script under the `scripts/` directory.
