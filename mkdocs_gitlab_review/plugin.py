# Copyright [2020] [Intergral GmbH]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
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
            return "data-require-auth='true' "
        return ''

    def gitlab_url(self):
        return self.config.get('gitlab_url')

    def script_url(self):
        return self.config.get('script_url')

    def script_id(self):
        return self.config.get('script_id')
