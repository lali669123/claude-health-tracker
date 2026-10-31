---
name: record-meal
description: 记录一餐或加餐（文字或照片），估算热量和蛋白质，写入 meals.csv、daily_metrics.csv 和当天日志。用户说吃了什么、发餐食照片时使用。
---

# 记录餐食

1. 确认日期和餐次（早餐/午餐/晚餐/加餐）。过了零点补记的，按所属日期记。
2. 查 `data/structured/meals.csv` 当天是否已有这一餐。已有就更新那一行，不要新加。
3. 估算：
   - 逐项列出食物、可食重量、热量、蛋白质。
   - 有餐前餐后照片时，按剩余量扣减；剩的骨头、壳不算剩饭。
   - 多人分食按用户说的比例算。
   - 给中值和范围，标可信度（high/medium/low），写明最大的误差来源。
   - 份量不清时先按常见份量估，再问一个最影响结果的问题（例如“煎饼用了几个蛋、多少面？”）。
4. 写入：
   - `meals.csv` 追加一行：date,meal_type,food_items,calories_est,protein_g,confidence,notes。字段内不要用英文逗号。
   - `daily_metrics.csv` 当天一行：更新 calories_intake、calories_intake_min/max、protein_g、protein_min/max（当天各餐之和），data_quality 至少为 partial。没有这一行就新建，保持 21 列。
   - `data/logs/daily/YYYY-MM-DD.md` 追加这一餐的内容和估算说明。
5. 回复：这一餐和当天累计的热量、蛋白质，离 goals.json 目标还差多少，一条具体建议。简短即可。
