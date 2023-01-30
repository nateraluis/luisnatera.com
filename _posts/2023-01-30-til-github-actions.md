---
title: 'TIL Running a GitHub Action After Another Action'
date: 2023-01-30
permalink: /posts/2023/01/running-a-github-action-after-another-action/
tags:
  - til
  - github
  - ci
---

Today I had to deal with an issue on my CI/CD workflow for automating my weekly blog post. The problem: The action for creating the blog post ran, created the post, and pushed it back to the repo, but the deployment action was not triggered after it. Although, the deployment action is supposed to be triggered with pushes to the `main` branch:

```yml
name: 🚀Deploy site

on:
  push:
    branches:
      - main
```

After reading about why the action does not run after a push from another action, found that if the action that pushes the code pushes it directly with the GitHub authentication it does not trigger another action.

The solution: create a personal access token and use it to authenticate and push the change, or change the deployment action to also be triggered after a successful run from another action. I followed the second approach, so I modified the deployment action as follows:

```yml
name: 🚀Deploy site

on:
  push:
    branches:
      - main
  workflow_run:
    workflows: ["👨‍💻 weekly post"]
    types:
      - completed
```

Now the action also runs after the workflow `👨‍💻 weekly post` has run and its status is `completed`.

With that simple change, the workflow to write and publish a new week in review is complete, and it gets deployed after creating the blog post.