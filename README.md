# claude-health-tracker

用 [Claude Code](https://claude.com/claude-code) 对话记录饮食、体重、训练和手环数据，自动生成日报和周报。数据全部存在本地的 CSV 和 Markdown 里。

适合想减脂增肌、又不想手动填表的人：拍照或说一句“午餐吃了什么”，Claude 估算热量和蛋白质并写进表里。

## 它能做什么

- **记录餐食**：文字或照片，估算热量和蛋白质，给范围和可信度。支持餐前餐后对比、多人分食、补充份量后修正。
- **同步手环**：发健康 App 截图（以华为运动健康为例），提取睡眠、心率、HRV、步数、活动热量。
- **记录训练**：动作、重量、组数次数，和上次对比，提示下次怎么加重。
- **日报 / 周报**：营养、睡眠恢复、活动、热量缺口估算、趋势、评分和下一步计划。缺数据就写缺失，不编造。

## 开始使用

```bash
git clone https://github.com/<你的用户名>/claude-health-tracker.git
cd claude-health-tracker
cp -r template data
```

然后：

1. 填写 `data/config/profile.json`（身高、出生日期、性别）和 `data/config/goals.json`。
2. 在这个文件夹里打开 Claude Code，直接说话即可：
   - “晨重 70.5”
   - “早餐一杯牛奶、两个鸡蛋” 或发一张照片
   - 发手环截图，说“同步手环”
   - “生成今天的日报”
3. 也可以用技能命令：`/record-meal`、`/sync-wearable`、`/record-training`、`/daily-report`、`/weekly-report`。

`data/` 已写进 `.gitignore`，你的个人数据不会被提交。

## 定时日报 / 周报（可选）

Claude 桌面应用支持定时任务。把 `routines/` 里的提示词贴进去，并把 `<DATA_DIR>` 换成你的 `data` 文件夹绝对路径。

- 日报：每晚 23:30 检查今天和前两天，有手环数据且还没出日报的日期就生成，已有的不覆盖。
- 周报：每周六统计上周日到本周六。

建议日常记录固定在一个对话里，不要在定时任务开出的对话里再记一遍，免得同一餐记两次。

## 文件结构

```
.claude/skills/        五个技能：记录餐食、同步手环、记录训练、日报、周报
CLAUDE.md              给 Claude 的项目规则（日期、去重、估算、分析原则）
routines/              定时任务提示词
scripts/stats.py       不经过 Claude，快速看最近 N 天平均值
template/              data/ 的初始结构：配置示例和只有表头的 CSV
data/                  你的数据（不上传）
```

## 数据表

| 文件 | 内容 |
|------|------|
| `structured/daily_metrics.csv` | 每天一行汇总：体重、摄入范围、蛋白质、睡眠、心率、HRV、步数、活动热量 |
| `structured/meals.csv` | 每餐一行：食物、热量、蛋白质、可信度、备注 |
| `structured/training.csv` | 每次训练一行，动作写在 notes 里 |
| `structured/wearable.csv` | 手环原始指标 |

## 快速统计

```bash
python scripts/stats.py --days 7
```

只用 Python 标准库，不需要安装依赖。

## 局限

- 热量和蛋白质是估算。照片估算误差可能有 20–40%，称重或看包装标签能明显提高准确度。
- 热量消耗 = Mifflin-St Jeor 基础代谢 + 手环活动热量，也是估算。判断减脂是否有效，以 7 天平均体重的变化为准。
- 不是医疗工具，不做诊断。

## 许可

MIT
