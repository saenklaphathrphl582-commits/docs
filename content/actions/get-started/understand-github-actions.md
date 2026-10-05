---
title: Understanding GitHub Actions
shortTitle: Understand GitHub Actions
intro: Learn the basics of core concepts and essential terminology in {% data variables.product.prodname_actions %}.
redirect_from:
  - /github/automating-your-workflow-with-github-actions/core-concepts-for-github-actions
  - /actions/automating-your-workflow-with-github-actions/core-concepts-for-github-actions
  - /actions/getting-started-with-github-actions/core-concepts-for-github-actions
  - /actions/learn-github-actions/introduction-to-github-actions
  - /actions/learn-github-actions/understanding-github-actions
  - /actions/learn-github-actions/essential-features-of-github-actions
  - /articles/getting-started-with-github-actions
  - /actions/about-github-actions/understanding-github-actions
  - /actions/get-started/understanding-github-actions
  - /enterprise-onboarding/github-actions-for-your-enterprise/actions-components
  - /enterprise-onboarding/github-actions-for-your-enterprise/understanding-github-actions
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
contentType: get-started
category:
  - Get started with GitHub Actions
---

{% data reusables.actions.enterprise-github-hosted-runners %}

## Overview

{% data reusables.actions.about-actions %} You can create workflows that build and test every pull request to your repository, or deploy merged pull requests to production.

{% data variables.product.prodname_actions %} goes beyond just DevOps and lets you run workflows when other events happen in your repository. For example, you can run a workflow to automatically add the appropriate labels whenever someone creates a new issue in your repository.

{% ifversion fpt or ghec %}

{% data variables.product.prodname_dotcom %} provides Linux, Windows, and macOS virtual machines to run your workflows, or you can host your own self-hosted runners in your own data center or cloud environment.

{% elsif ghes %}

You must host your own Linux, Windows, or macOS virtual machines to run workflows for {% data variables.location.product_location %}.

{% endif %}

{% ifversion ghec or ghes %}

For more information about introducing {% data variables.product.prodname_actions %} to your enterprise, see [AUTOTITLE](/admin/managing-github-actions-for-your-enterprise/getting-started-with-github-actions-for-your-enterprise).

{% endif %}

## The components of {% data variables.product.prodname_actions %}

You can configure a {% data variables.product.prodname_actions %} **workflow** to be triggered when an **event** occurs in your repository, such as a pull request being opened or an issue being created. Your workflow contains one or more **jobs** which can run in sequential order or in parallel. Each job will run inside its own virtual machine **runner**, or inside a container, and has one or more **steps** that either run a script that you define or run an **action**, which is a reusable extension that can simplify your workflow.

![Diagram of an event triggering Runner 1 to run Job 1, which triggers Runner 2 to run Job 2. Each of the jobs is broken into multiple steps.](/assets/images/help/actions/overview-actions-simple.png)

### Workflows

{% data reusables.actions.about-workflows-long %}

A workflow is reusable automation that you store in your repository and can be referenced from another workflow. For more information, see [AUTOTITLE](/actions/how-tos/reuse-automations/reuse-workflows).

For more information, see [AUTOTITLE](/actions/how-tos/write-workflows).

### Events

An **event** is a specific activity in a repository that triggers a workflow run. For example, an activity can originate from {% data variables.product.prodname_dotcom %} when someone creates a pull request, opens an issue, or pushes a commit to a repository. You can also trigger a workflow on a schedule, by posting to a REST API, or manually.

For a complete list of events that can be used to trigger workflows, see [Events that trigger workflows](/actions/reference/workflows-and-actions/events-that-trigger-workflows).

### Jobs

A **job** is a set of **steps** in a workflow that executes on the same **runner**. Each step is either a shell script that will be executed, or an **action** that will be run. Steps are executed in order and are dependent on each other—since each step executes on the same runner, you can share data from one step to another.

{% ifversion actions-nga %}

Steps run in order by default, but you can also run selected steps concurrently when your workflow benefits from parallel execution, such as starting a long-running service while later steps continue testing your application.

{% endif %}

You can configure a job's dependencies with other jobs; by default, jobs have no dependencies and run in parallel. When a job takes a dependency on another job, it waits for the dependent job to complete before it can proceed. For example, you might have multiple build jobs for different architectures that have no dependencies, and a packaging job that depends on those jobs. The build jobs will run in parallel, and when they have all completed successfully, the packaging job will run.

For more information, see [AUTOTITLE](/actions/how-tos/write-workflows/choose-what-workflows-do).

### Actions

An **action** is a custom application for the {% data variables.product.prodname_actions %} platform that performs a complex but frequently repeated task. Use an action to help reduce the amount of repetitive code that you write in your workflow files. An action can pull your Git repository from {% data variables.product.prodname_dotcom %}, set up the correct toolchain for your build environment, or set up the authentication to your cloud provider.

You can write your own actions, or you can find pre-built actions to use in your workflows in the {% data variables.product.prodname_marketplace %}.

{% data reusables.actions.internal-actions-summary %}

For more information, see [AUTOTITLE](/actions/how-tos/reuse-automations).

### Runners

A **runner** is a server that runs your workflows when they're triggered. Each runner can run a single **job** at a time.

{% ifversion ghes %}

You must host your own runners for {% data variables.product.prodname_ghe_server %}.

{% elsif fpt or ghec %}

{% data variables.product.company_short %} provides Ubuntu Linux, Microsoft Windows, and macOS runners to run your workflows. Each workflow run executes in a fresh, newly provisioned virtual machine. If you need a different operating system or require a specific hardware configuration, you can host your own runners.

{% ifversion actions-hosted-runners %}

{% data variables.product.prodname_dotcom %} also offers {% data variables.actions.hosted_runner %}s, which are available in larger configurations. For more information, see [AUTOTITLE](/actions/using-github-hosted-runners/about-larger-runners).

{% endif %}

{% endif %}

For more information about self-hosted runners, see [AUTOTITLE](/actions/how-tos/manage-runners/self-hosted-runners).

## A complete example workflow

Here's a simple workflow that demonstrates how all the components work together:

```yaml
name: Learn GitHub Actions
run-name: {% raw %}${{ github.actor }}{% endraw %} is learning GitHub Actions
on: [push]
jobs:
  check-bats-version:
    runs-on: ubuntu-latest
    steps:
      - uses: {% data reusables.actions.action-checkout %}
      - uses: {% data reusables.actions.action-setup-node %}
        with:
          node-version: '14'
      - run: npm install -g bats
      - run: bats -v
```

**Breaking it down:**

1. **Event** (`on: [push]`): The workflow runs whenever code is pushed
2. **Job** (`check-bats-version`): A single job that will run on an Ubuntu runner
3. **Steps**:
   - **Action** (`actions/checkout`): Pulls your repository code
   - **Action** (`actions/setup-node`): Sets up Node.js
   - **Commands** (`run`): Installs and runs the `bats` testing tool

## Next steps

Now that you understand the core concepts, you're ready to:

1. **Create your first workflow**: Start with our [Quickstart guide](/actions/get-started/quickstart)
2. **Learn best practices**: Explore workflow patterns and optimization techniques
3. **Use marketplace actions**: Discover thousands of pre-built actions in the {% data variables.product.prodname_marketplace %}

{% data reusables.actions.onboarding-next-steps %}

{% ifversion copilot %}

> [!NOTE]
> For automations that require contextual judgment about your repository's content, you can also author {% data variables.copilot.agentic_workflows_short %} in natural language instead of a traditional YAML workflow. For more information, see [AUTOTITLE](/actions/writing-workflows/using-github-actions-ai-powered-workflows).

{% endif %}

{% ifversion ghec or ghes %}

## Further reading

* [AUTOTITLE](/admin/managing-github-actions-for-your-enterprise/getting-started-with-github-actions-for-your-enterprise/about-github-actions-for-enterprises)

{% endif %}
