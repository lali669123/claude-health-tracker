# 健康记录项目规则

这个项目用对话记录饮食、体重、训练和手环数据，并生成日报、周报。Codex 和 Claude Code 都读这份文件（Claude Code 通过 CLAUDE.md 导入）。

## 数据位置

- 所有个人数据在 `data/`（已被 .gitignore 排除，不会上传）。
- 首次使用：把 `template/` 复制为 `data/`，再填写 `data/config/profile.json` 和 `goals.json`。如果 `data/` 不存在，先提醒用户做这一步。
- 结构化数据：`data/structured/` 下四个 CSV（表头见 template）。
- 每日日志：`data/logs/daily/YYYY-MM-DD.md`。
- 报告：`data/reports/daily/YYYY-MM-DD.md`、`data/reports/weekly/YYYY-Www.md`。

## 技能

具体流程在 `.agents/skills/`（Codex）和 `.claude/skills/`（Claude Code），两份内容相同。用户记录餐食、发手环截图、说训练内容、要日报周报时，按对应技能执行：record-meal、sync-wearable、record-training、daily-report、weekly-report。

## 记录规则

1. 先确认日期。用户过了零点补记前一天的内容很常见，按内容所属日期记，不按当前时间。
2. 写入前查当天是否已有同一餐或同一份手环数据，避免重复记录。
3. CSV 字段里不要出现英文逗号，备注用分号分隔。写完检查每行列数和表头一致。
4. 估算要给中值和范围，并标可信度（high：称重或包装标签；medium：照片加用户确认的份量；low：只凭照片或描述）。
5. 用户补充了实际份量，就改原记录，不要再加一条。
6. 每条体重同时更新 `daily_metrics.csv` 的 weight_kg 和 `config/profile.json` 的 current_weight_kg、current_weight_date。

## 分析规则

- 结论要有依据，数字要有来源。没有数据就写缺失，不要估算补齐，也不要编造对比（例如“超过 90% 的同龄人”）。
- 单次体重受水分和盐影响会波动 0.5–1 kg，判断趋势至少用 7 天平均。
- 热量消耗是估算：Mifflin-St Jeor 基础代谢 + 手环活动热量。报告里要写明这一点。
- 不做医学诊断。数据持续异常（例如静息心率连续多天明显升高、血氧持续偏低）时，建议用户就医，不要自行解释成某种疾病。
