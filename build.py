'''
FileName: build.py
Author: Chuncheng
Version: V0.0
Purpose: Build the README.md for the Project
'''

# %%
import os

# %%
workingFolder = os.path.dirname(__file__)
encoding = 'utf-8'

# %%
sub_folders = [e for e in os.listdir(workingFolder)
               if os.path.isdir(os.path.join(workingFolder, e))]

sub_folders

# %%


def get_files(folder, ext='.md', exclude='readme'):
    '''
    Method: get_files

    Get files from [folder] with extension is [ext],
    the files will not startswith [exclude]

    Args:
    - @folder, ext='.md', exclude='readme'

    Outputs:
    - The list of filenames.

    '''

    return [e for e in os.listdir(folder)
            if all([os.path.isfile(os.path.join(folder, e)),
                    not e.startswith(exclude),
                    e.endswith(ext)])]


def build_topic(folder):
    '''
    Method: build_topic

    Build the Readme for the [folder]

    Args:
    - @folder: The folder of the topic.

    Outputs:
    - The Content of the README.md in the topic folder.

    '''
    if not 'readme_header.md' in os.listdir(folder):
        print('E: Invalid topic folder {}'.format(folder))
        return

    print('I: Building Readme for the topic folder {}'.format(folder))

    def _path(name, folder=folder):
        return os.path.join(folder, name)

    names = sorted(get_files(folder))
    print(names)

    with open(_path('README.md'), 'wb') as f:

        def _write(msg, file=f):
            print('|->  {}'.format(msg))
            if not isinstance(msg, type(b'bytes')):
                msg = msg.encode(encoding)
            file.write(msg)

        _write(open(_path('readme_header.md'), 'r', encoding=encoding).read())

        for name in names:
            content = open(_path(name), 'r',
                           encoding=encoding).read().split('---')[0]
            _write(content)

        pass

    return open(_path('README.md'), 'r', encoding=encoding).read()


# %%
with open(os.path.join(workingFolder, 'README.md'), 'wb') as f:

    def _write(msg, file=f):
        print('|->  {}'.format(msg))
        if not isinstance(msg, type(b'bytes')):
            msg = msg.encode(encoding)
        file.write(msg)

    _write(open(os.path.join(workingFolder, 'README_header.md'),
           'r', encoding=encoding).read())

    for folder in sub_folders:
        content = build_topic(os.path.join(workingFolder, folder))
        if content is not None:
            _write(content)

# %%
