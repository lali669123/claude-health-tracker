---
name: sync-wearable
description: 从手环/健康 App 截图或用户口述中提取睡眠、心率、HRV、步数、活动数据，写入 wearable.csv 和 daily_metrics.csv。用户发手环截图时使用。
---

# 同步手环数据

1. 日期以截图上显示的日期为准。过了零点，提醒用户先把 App 里的日期切回前一天再截图。
2. 查 `wearable.csv` 当天是否已有数据，已有就更新那一行。
3. 提取（以华为运动健康为例，其他 App 字段类似）：
   - 睡眠页：夜间睡眠、零星小睡、总睡眠、睡眠评分、深睡/浅睡/快速眼动、清醒次数、入睡和醒来时间、睡眠平均心率、HRV、血氧、呼吸率。
   - 活动记录：步数、距离、活动热量、锻炼时长、活动小时数。
   - 心脏健康：心率范围、静息心率、日间 HRV 范围。
   - 情绪/压力（可选）：压力均值、情绪占比。
   时长换算成小时（7小时35分 = 7.58）。看不清的字段留空，不要猜。
4. 写入：
   - `wearable.csv`：date,device,resting_hr,hr_min,hr_max,hrv_night_avg,sleep_score,steps,activity_calories,exercise_min
   - `daily_metrics.csv` 当天一行：sleep_night_h、sleep_nap_h、sleep_total_h、sleep_score、resting_hr_bpm、hrv_night_avg_ms、steps、activity_calories、exercise_min。
   - 截图里放不进表的数据（睡眠分期、血氧、压力等）写进当天日志。
5. 回复提取到的关键数字，问用户是否现在生成日报。
