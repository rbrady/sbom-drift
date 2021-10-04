# drift-wip
drift work in progress

### output examples ###

For a source to source comparison, the sample output shows relevant subsets of data for
the new content and removed content, and the subset of data that has changed for the modified
content.

```json
{
    'artifacts': {
        'added': {
            [{
                'version': 1.0,
                'type': 'python',
                'language': 'python',
                'name': 'SqlAlchemy',
                'licenses': [],
                
            }, 
            ],
        },
        'removed': [
            {
                'version': 1.0,
                'type': 'python',
                'language': 'python',
                'name': 'foo',
                'licenses': [],
                
            },
        ],
        'modified': [
            'fastapi': {
                'cpes': ['cpe:2.3:a:fastapi:fastapi:0.68.1:*:*:*:*:*:*:*',
                'cpe:2.3:a:fastapi:fastapi:0.68.1:*:*:*:*:python:*:*',
                'cpe:2.3:a:fastapi:python-fastapi:0.68.1:*:*:*:*:*:*:*',
                'cpe:2.3:a:fastapi:python-fastapi:0.68.1:*:*:*:*:python:*:*',
                'cpe:2.3:a:fastapi:python_fastapi:0.68.1:*:*:*:*:*:*:*',
                'cpe:2.3:a:fastapi:python_fastapi:0.68.1:*:*:*:*:python:*:*',
                'cpe:2.3:a:python-fastapi:fastapi:0.68.1:*:*:*:*:*:*:*',
                'cpe:2.3:a:python-fastapi:fastapi:0.68.1:*:*:*:*:python:*:*',
                'cpe:2.3:a:python-fastapi:python-fastapi:0.68.1:*:*:*:*:*:*:*',
                'cpe:2.3:a:python-fastapi:python-fastapi:0.68.1:*:*:*:*:python:*:*',
                'cpe:2.3:a:python-fastapi:python_fastapi:0.68.1:*:*:*:*:*:*:*',
                'cpe:2.3:a:python-fastapi:python_fastapi:0.68.1:*:*:*:*:python:*:*',
                'cpe:2.3:a:python:fastapi:0.68.1:*:*:*:*:*:*:*',
                'cpe:2.3:a:python:fastapi:0.68.1:*:*:*:*:python:*:*',
                'cpe:2.3:a:python:python-fastapi:0.68.1:*:*:*:*:*:*:*',
                'cpe:2.3:a:python:python-fastapi:0.68.1:*:*:*:*:python:*:*',
                'cpe:2.3:a:python:python_fastapi:0.68.1:*:*:*:*:*:*:*',
                'cpe:2.3:a:python:python_fastapi:0.68.1:*:*:*:*:python:*:*',
                'cpe:2.3:a:python_fastapi:fastapi:0.68.1:*:*:*:*:*:*:*',
                'cpe:2.3:a:python_fastapi:fastapi:0.68.1:*:*:*:*:python:*:*',
                'cpe:2.3:a:python_fastapi:python-fastapi:0.68.1:*:*:*:*:*:*:*',
                'cpe:2.3:a:python_fastapi:python-fastapi:0.68.1:*:*:*:*:python:*:*',
                'cpe:2.3:a:python_fastapi:python_fastapi:0.68.1:*:*:*:*:*:*:*',
                'cpe:2.3:a:python_fastapi:python_fastapi:0.68.1:*:*:*:*:python:*:*'],
            'purl': 'pkg:pypi/fastapi@0.68.2',
            'version': '0.68.2'
            },
        ],
    }
}

```
