# mkdocs-gitlab-review-plugin

Plugin for [`mkdocs`](https://www.mkdocs.org/) to
use [GitLab Visual Review Apps](https://docs.gitlab.com/ee/ci/review_apps/#visual-reviews)

This plugin will automatically add the `<script>` tag for the Gitlab visual reviews. To use this you need to set up [Review Apps](https://docs.gitlab.com/ee/ci/review_apps/)
and [Merge Request pipelines](https://docs.gitlab.com/ee/ci/merge_request_pipelines/#pipelines-for-merge-requests).

## Installing

Install with pip:

```bash
pip install mkdocs-gitlab-review-plugin
```

## Using

To use this plugin, simply add the plugin to the `mkdocs.yml`

```yaml
plugins:
  - gitlab_review
```

## Configuration

There are a few configuration options available:

|option|Default|Description|
|---|---|---|
|auth|false|A boolean to enable the Gitlab auth see [Authentication for Visual Reviews](https://docs.gitlab.com/ee/ci/review_apps/#authentication-for-visual-reviews)|
|gitlab_url|https://gitlab.com| The url for the GitLab instance.|
|script_url|https://gitlab.com/assets/webpack/visual_review_toolbar.js|The url for the script to use|
|script_id|review-app-toolbar-script|The id in the HTML for the `<script>` tag.|

## Contributing

- Pull Requests are welcome.
- File bugs and suggestions in the [GitHub Issues tracker](https://github.com/intergral/mkdocs-gitlab-review-plugin/issues).
