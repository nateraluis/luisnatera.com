---
title: 'Automating blog posting with GitHub Actions'
date: 2022-09-09
permalink: /posts/2022/09/automating-post-github-actions/
tags:
  - Automation
  - GitHub
  - Python
---

## Idea
Use GitHub actions to automated blog posting.
## GitHub Actions
Describe what are GitHub actions
### Automate issue creating
Use issue per week to track the content to be published. One issue one post. Close previous issue
### Automate content creation
- Content comes from comments
- Use `#tag` to classify the content


```mermaid
graph TD;
    A -- close previous --> B
    A[GitHub Action] --creates--> B[Weekly issue];
    G[\Post comments in issue/] --> B
    C[GitHubAction] --Executes--> D[Python script];
    D --> E(For comment in issue);
    E --reads--> B;
    E --write into--> F[/Week in review file/];
```

