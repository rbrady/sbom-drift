#!/usr/bin/env python
import click

from IPython import embed

from drift.comparisions2.artifact import compare_artifact
from drift.utils import load_sbom_from_file


@click.command()
@click.argument('base_file', type=click.Path(exists=True))
@click.argument('compare_file', type=click.Path(exists=True))
def debug(base_file, compare_file):
    base_sbom = load_sbom_from_file(base_file)
    other_sbom = load_sbom_from_file(compare_file)
    embed()


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