class Ops(type):
    """Ops is the base class for all operations"""

    def __init__(self):
        pass

    def load_sbom(self):
        """Load sbom from input where input can be from the command line or
        database"""
        pass

    def get_sbom(self):
        """Get sbom will retrieve document from database"""
        pass

    def compare_sbom(self):
        """Comparison logic for sbom"""
        pass

    def compare_yaml(self):
        pass


class OpsGuard(Ops):
    """OpsGuard will contain all guard operations for documents stored"""

    def __init__(self):
        pass

    def version_check(self):
        """Version Check should query for specified changes in attributes."""
        pass

    def artifact_equality(base: list, other: list) -> bool:
        """Artifact Equality will perform a niave equality check to prevent
        expensive operations"""
        pass
