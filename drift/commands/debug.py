#!/usr/bin/env python
import click
import ipdb

from drift.utils import load_sbom


@click.command()
@click.argument('base_file', type=click.Path(exists=True))
@click.argument('compare_file', type=click.Path(exists=True))
def debug(base_file, compare_file):
    base_sbom = load_sbom(base_file)
    other_sbom = load_sbom(compare_file)
    ipdb.set_trace()


if __name__ == '__main__':
    debug()


# scenarios to compare

# source to source
# - artifacts
#   - count
#   - version
#   - added
#   - removed


# source to image
# - artifacts
#   - version
#   - removed

# source will have fewer artifacts than image
# count/added won't be valuable in this case.