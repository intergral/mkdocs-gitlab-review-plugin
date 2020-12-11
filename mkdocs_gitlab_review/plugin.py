import os

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin


class GitLabPlugin(BasePlugin):
    config_scheme = (
        ('auth', config_options.Type(bool, default=False)),
        ('gitlab_url', config_options.Type(str, default='https://gitlab.com')),
        ('script_url', config_options.Type(str, default='https://gitlab.com/assets/webpack/visual_review_toolbar.js')),
        ('script_id', config_options.Type(str, default='review-app-toolbar-script')),
    )

    def __init__(self):
        self.enabled = False
        self.gitlab_project_id = os.environ.get('CI_PROJECT_ID', None)
        self.gitlab_project_path = os.environ.get('CI_PROJECT_PATH', None)
        self.gitlab_mr = os.environ.get('CI_MERGE_REQUEST_IID', None)
        if self.gitlab_mr is not None and self.gitlab_project_id is not None and self.gitlab_project_path is not None:
            self.enabled = True

    def script(self):
        return "<script " \
               "defer data-project-id='%s' " \
               "data-project-path='%s' " \
               "data-merge-request-id='%s' " \
               "%s" \
               "data-mr-url='%s' " \
               "id='%s' " \
               "src='%s'></script>" % (
                   self.gitlab_project_id, self.gitlab_project_path, self.gitlab_mr, self.require_auth(), self.gitlab_url(),
                   self.script_id(), self.script_url())

    def on_post_page(self, output, page, config):
        if not self.enabled:
            return output
        if '</head>' not in output:
            return output
        return output.replace('</head>', "%s\n</head>" % self.script())

    def require_auth(self):
        if self.config.get('auth'):
            return "data-require-auth='true'"
        return ''

    def gitlab_url(self):
        return self.config.get('gitlab_url')

    def script_url(self):
        return self.config.get('script_url')

    def script_id(self):
        return self.config.get('script_id')
