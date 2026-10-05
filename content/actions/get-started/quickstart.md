---
title: Quickstart for GitHub Actions
intro: Try out the core features of {% data variables.product.prodname_actions %} in minutes.
allowTitleToDifferFromFilename: true
redirect_from:
  - /actions/getting-started-with-github-actions/starting-with-preconfigured-workflow-templates
  - /actions/quickstart
  - /actions/getting-started-with-github-actions
  - /actions/writing-workflows/quickstart
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
shortTitle: Quickstart
contentType: get-started
category:
  - Get started with GitHub Actions
---

{% data reusables.actions.enterprise-github-hosted-runners %}

## Introduction

{% data reusables.actions.about-actions %} You can create workflows that run tests whenever you push a change to your repository, or that deploy merged pull requests to production.

This quickstart guide shows you how to build a simple workflow in minutes using practical, real-world examples.

## What you'll build

You'll create a workflow that automatically:
* Triggers every time you push code to your repository
* Runs on a GitHub-hosted runner
* Checks out your repository code
* Displays a confirmation message

This demonstrates the core concepts: **events**, **jobs**, **steps**, and **actions**.

## Prerequisites

* A repository on {% data variables.product.github %}
* Basic familiarity with Git and {% data variables.product.prodname_dotcom %}

## Step 1: Create your workflow file

1. In your repository, create the directory `.github/workflows` if it doesn't already exist.
2. In the `.github/workflows` directory, create a new file called `quickstart.yml`.
3. Copy the following YAML content into your workflow file:

```yaml
name: Quickstart Demo
run-name: {% raw %}${{ github.actor }}{% endraw %} is testing GitHub Actions 🚀

on:
  push:
    branches:
      - main

jobs:
  explore-github-actions:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository code
        uses: {% data reusables.actions.action-checkout %}

      - name: Display trigger event
        run: echo "✅ Workflow triggered by ${% raw %}{{ github.event_name }}{% endraw %} event"

      - name: Display runner environment
        run: echo "🐧 Running on ${% raw %}{{ runner.os }}{% endraw %} runner"

      - name: Display branch and repository
        run: echo "📦 Repository: ${% raw %}{{ github.repository }}{% endraw %} | Branch: ${% raw %}{{ github.ref }}{% endraw %}"

      - name: List repository contents
        run: ls -la ${% raw %}{{ github.workspace }}{% endraw %}

      - name: Completion message
        run: echo "✨ Workflow completed successfully!"
```

## Step 2: Commit and push your workflow

1. Commit the workflow file to your repository:
   ```bash
   git add .github/workflows/quickstart.yml
   git commit -m "evidence: add quickstart GitHub Actions workflow"
   git push origin main
   ```

2. Your commit will automatically trigger the workflow.

## Step 3: View your workflow results

1. On {% data variables.product.prodname_dotcom %}, navigate to your repository.
2. Click the **Actions** tab.
3. Click the workflow run (usually labeled with your commit message or username).
4. Under **Jobs**, click the **explore-github-actions** job.
5. Expand each step to see what happened when the workflow ran.

You'll see output like:
* The event that triggered the workflow (push)
* The runner operating system (Linux)
* Your repository name and branch
* The files in your repository
* A success confirmation

## Understanding the workflow

Let's break down the key components:

| Component | Description |
|-----------|-------------|
| `name` | The name of your workflow (appears in the Actions tab) |
| `on` | The event that triggers the workflow (in this case: a push to `main`) |
| `jobs` | A collection of tasks to run |
| `runs-on` | The type of machine to run the job on (e.g., `ubuntu-latest`) |
| `steps` | Individual tasks within a job |
| `uses` | A pre-built action to reuse code (like checking out your repository) |
| `run` | A shell command to execute |

## Next steps

Now that you've created your first workflow, here are some ways to expand on it:

* **Add testing**: Use a workflow to automatically test your code on every push
* **Build artifacts**: Compile and package your application
* **Deploy to production**: Automatically deploy when you merge to `main`
* **Use marketplace actions**: Leverage community-contributed actions from the {% data variables.product.prodname_marketplace %}

{% data reusables.actions.onboarding-next-steps %}
