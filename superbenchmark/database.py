import json
from datetime import datetime
from typing import List, Optional

from .models import AveragePerformance, BenchmarkResult


class DatabaseHandler:
    def __init__(self, db_path: str = "test_database.json"):
        self.db_path = db_path

    def load_results(self) -> List[BenchmarkResult]:
        try:
            with open(self.db_path, "r") as f:
                data = json.load(f)
                return [
                    BenchmarkResult(**{**result, "timestamp": datetime.fromisoformat(result["timestamp"])})
                    for result in data.get("benchmarking_results", [])
                ]
        except FileNotFoundError:
            return []

    def calculate_average(
        self, start_time: Optional[datetime] = None, end_time: Optional[datetime] = None
    ) -> AveragePerformance:
        results = self.load_results()

        if start_time and end_time:
            results = [r for r in results if start_time <= r.timestamp <= end_time]

        if not results:
            return AveragePerformance()

        return AveragePerformance(
            avg_token_count=sum(r.token_count for r in results) / len(results),
            avg_time_to_first_token=sum(r.time_to_first_token for r in results) / len(results),
            avg_time_per_output_token=sum(r.time_per_output_token for r in results) / len(results),
            avg_total_generation_time=sum(r.total_generation_time for r in results) / len(results),
            total_results=len(results),
        )
