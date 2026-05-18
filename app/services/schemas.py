from pydantic import BaseModel
from typing import List


class Finding(BaseModel):
    issue: str
    severity: str
    recommendation: str


class ReviewResponse(BaseModel):
    findings: List[Finding]