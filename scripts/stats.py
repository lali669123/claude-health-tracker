#!/usr/bin/env python3
"""快速查看最近 N 天的关键指标。只用标准库。

用法：python scripts/stats.py [--days 7] [--data-dir data/structured]
"""
import argparse
import csv
import statistics
from datetime import date, timedelta
from pathlib import Path

FIELDS = [
    ("weight_kg", "体重 kg"),
    ("calories_intake", "摄入 kcal"),
    ("protein_g", "蛋白质 g"),
    ("sleep_night_h", "夜间睡眠 h"),
    ("sleep_score", "睡眠评分"),
    ("resting_hr_bpm", "静息心率"),
    ("hrv_night_avg_ms", "夜间 HRV ms"),
    ("steps", "步数"),
    ("activity_calories", "活动热量 kcal"),
]


def load(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def main():
    parser = argparse.ArgumentParser(description="最近 N 天关键指标")
    parser.add_argument("--days", type=int, default=7)
    parser.add_argument("--data-dir", default="data/structured")
    parser.add_argument("--end", help="截止日期 YYYY-MM-DD，默认今天")
    args = parser.parse_args()

    end = date.fromisoformat(args.end) if args.end else date.today()
    start = end - timedelta(days=args.days - 1)
    rows = [
        r for r in load(Path(args.data_dir) / "daily_metrics.csv")
        if r["date"] and start <= date.fromisoformat(r["date"]) <= end
    ]

    print(f"{start} 至 {end}（{args.days} 天，表中有 {len(rows)} 天）")
    for key, label in FIELDS:
        values = [float(r[key]) for r in rows if r.get(key)]
        if not values:
            print(f"  {label:<14} 无数据")
            continue
        print(f"  {label:<14} 平均 {statistics.mean(values):>8.1f}"
              f"  范围 {min(values):g}-{max(values):g}  ({len(values)} 天)")


if __name__ == "__main__":
    main()
