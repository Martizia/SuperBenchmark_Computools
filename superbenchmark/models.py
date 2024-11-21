from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BenchmarkResult(BaseModel):
    request_id: str
    prompt_text: str
    generated_text: str
    token_count: int
    time_to_first_token: int
    time_per_output_token: int
    total_generation_time: int
    timestamp: datetime


class AveragePerformance(BaseModel):
    avg_token_count: Optional[float] = None
    avg_time_to_first_token: Optional[float] = None
    avg_time_per_output_token: Optional[float] = None
    avg_total_generation_time: Optional[float] = None
    total_results: int = 0
