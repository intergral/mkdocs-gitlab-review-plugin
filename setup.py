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

from setuptools import setup, find_packages

VERSION_NUMBER = os.environ.get('CI_COMMIT_TAG', '0.0.1')


def read_file(fname):
    "Read a local file"
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def read_file_lines(fname):
    "Read a local file"
    return open(os.path.join(os.path.dirname(__file__), fname)).readlines()


setup(
    name='mkdocs-gitlab-review-plugin',
    version=VERSION_NUMBER,
    description="Use gitlab visual review with mkdocs.",
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    keywords='mkdocs python markdown gitlab',
    url='https://github.com/intergral/mkdocs-gitlab-review-plugin/',
    author='Ben Donnelly',
    author_email='support@nerd.vision',
    license='Apache 2.0',
    python_requires='>=3.5',
    install_requires=read_file_lines('requirements.txt'),
    extras_require={
        'test': read_file_lines('requirements-dev.txt'),
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
    ],
    include_package_data=True,
    packages=find_packages(exclude=['*.tests']),
    entry_points={
        'mkdocs.plugins': [
            'gitlab_review = mkdocs_gitlab_review.plugin:GitLabPlugin'
        ]
    }
)
