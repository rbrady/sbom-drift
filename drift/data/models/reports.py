from __future__ import annotations
from typing import Optional

from pydantic import BaseModel, Field
from .sbom_deltas import DistroDelta, SourceDelta


class ComparisonReport(BaseModel):
    artifacts: Optional[dict] = []
    distro: Optional[DistroDelta] = None
    source: Optional[SourceDelta] = None

