import re
from datetime import datetime, timedelta


__all__ = ["format_tag_text", "get_time"]

def format_tag_text(text, rep=("", )):
    return text.replace("\n", rep[0])


def get_time(time_str):
    now = datetime.now()

    if "ago" in time_str:
        dt = re.match(r"(\d+)\s+(\w+)\s+ago", time_str)       
        if dt:
            num = int(dt.group(1))
            unit = dt.group(2)

            if unit.startswith("day"):
                return now - timedelta(days=num)
            
            elif unit.startswith("hour"):
                return now - timedelta(hours=num)

    return datetime.strptime(time_str, "%b %d %Y")
