"""
根据 QSO 列表计算统计数据,返回一个 dict 给 narrator 用。
"""

from collections import Counter

def compute(qsos: list[dict]) -> dict:
    stats_dict = {}
    stats_dict["station_callsign"] = sorted(set(qso["station_callsign"].upper() for qso in qsos))
    stats_dict["total_qsos"] = len(qsos)
    earliest = min(qso["qso_date"] for qso in qsos)
    latest = max(qso["qso_date"] for qso in qsos)
    stats_dict["date_range"] = (earliest, latest)
    band_count = Counter(qso["band"].upper() for qso in qsos).most_common()
    stats_dict["band_distribution"] = band_count
    mode_count = Counter(qso["mode"].upper() for qso in qsos).most_common()
    stats_dict["mode_distribution"] = mode_count
    daily_max = Counter(qso["qso_date"] for qso in qsos).most_common(1)
    stats_dict["daily_max"] = {"date" : daily_max[0][0], "count" : daily_max[0][1]}
    top_callsigns = Counter(qso["call"] for qso in qsos).most_common(5)
    stats_dict["top_callsigns"] = top_callsigns
    stats_dict["unique_callsigns"] = len(set(qso["call"] for qso in qsos))
    return stats_dict