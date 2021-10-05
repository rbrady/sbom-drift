#!/usr/bin/env python
import click

from IPython import embed

from drift.comparisons import compare_artifact
from drift.data.model import SBOM
from drift.scenarios import image_as_base


@click.command()
@click.argument('base_file', type=click.Path(exists=True))
@click.argument('compare_file', type=click.Path(exists=True))
def compare(base_file, compare_file):
    base_sbom = SBOM.parse_file(base_file)
    other_sbom = SBOM.parse_file(compare_file)
    result = image_as_base(base_sbom, other_sbom)
    print(result)
    embed()


if __name__ == '__main__':
    compare()


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