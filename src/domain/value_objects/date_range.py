from datetime import datetime, timedelta
from dataclasses import dataclass

@dataclass(frozen=True)
class DateRange:
    check_in: datetime
    check_out: datetime

    def is_valid(self) -> bool:
        return (
            self.check_in < self.check_out
            and (self.check_out - self.check_in).days <= 30
            and (self.check_in - datetime.now()).total_seconds() / 3600 >= 24
        )

    def within_30_days(self) -> bool:
        return (self.check_out - self.check_in).days <= 30

    def has_24_hour_notice(self) -> bool:
        return (self.check_in - datetime.now()).total_seconds() / 3600 >= 24