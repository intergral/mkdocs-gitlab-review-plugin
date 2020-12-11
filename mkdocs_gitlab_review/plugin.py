import os

from mkdocs.plugins import BasePlugin


class GitLabPlugin(BasePlugin):

    def __init__(self):
        self.enabled = False
        self.gitlab_project_id = os.environ.get('CI_PROJECT_ID', None)
        self.gitlab_project_path = os.environ.get('CI_PROJECT_PATH', None)
        self.gitlab_mr = os.environ.get('CI_MERGE_REQUEST_IID', None)
        if self.gitlab_mr is not None and self.gitlab_project_id is not None and self.gitlab_project_path is not None:
            self.enabled = True
            self.script = "<script " \
                          "defer data-project-id='%s' " \
                          "data-project-path='%s' " \
                          "data-merge-request-id='%s' " \
                          "data-mr-url='https://gitlab.com' " \
                          "id='review-app-toolbar-script' " \
                          "src='https://gitlab.com/assets/webpack/visual_review_toolbar.js'></script>" % (
                              self.gitlab_project_id, self.gitlab_project_path, self.gitlab_mr)

    def on_post_page(self, output, page, config):
        if not self.enabled:
            return output
        if '</head>' not in output:
            return output
        return output.replace('</head>', "%s\n</head>" % self.script)
