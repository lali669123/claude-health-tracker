<div align="center">

# claude-health-tracker

**简体中文** | [English](README.en.md)

用 AI 编程助手当你的私人健康记录员：说一句话、拍一张照片，饮食、体重、训练和手环数据就整理进本地表格，每天生成有依据的健康日报。

[![Claude Code](https://img.shields.io/badge/Claude_Code-支持-D97757)](https://code.claude.com/docs/en/setup)
[![Codex](https://img.shields.io/badge/Codex-支持-10A37F)](https://github.com/openai/codex)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

---

## 一键部署

把下面这段话复制给 **Claude Code** 或 **Codex**，它会自动下载整套方案、建好你的个人档案，然后告诉你怎么开始：

```text
请按照 https://github.com/lali669123/claude-health-tracker/blob/main/SETUP.md 里的步骤，帮我安装并配置这套健康记录方案。
```

还没有 AI 助手？先装一个：[Claude Code](https://code.claude.com/docs/en/setup) · [Codex](https://github.com/openai/codex)

<details>
<summary>手动安装</summary>

```bash
git clone https://github.com/lali669123/claude-health-tracker.git
cd claude-health-tracker
cp -r template data        # Windows PowerShell: Copy-Item -Recurse template data
```

填写 `data/config/profile.json` 和 `goals.json`，然后在这个文件夹里运行 `claude` 或 `codex`。

</details>

两个工具读同一套规则（`AGENTS.md`）和同一套技能，记录的数据也是同一份，可以混用。

---

## 为什么用 AI 做健康管理

多数人并不缺健康知识，缺的是**持续、准确、能对上号的数据**，和一个肯每天帮你看这些数据的人。

传统做法有三个痛点：
- **记录太麻烦**：营养 App 要逐项搜食物、填克数，坚持不了几天。
- **数据是孤岛**：手环知道你睡了多久，饮食 App 知道你吃了什么，体重秤知道你多重，但没人把它们放在一起看。
- **建议太泛**：“多睡觉、多吃蛋白质”人人都知道，难的是“今天具体差多少、明天怎么补”。

AI 助手能补上这三块：

| 能力 | 具体表现 |
|------|----------|
| **低成本记录** | 拍照或一句话描述，AI 估算份量、热量和蛋白质；家里做的饭告诉它用了几个蛋、多少面，它会按实际用量重算 |
| **跨维度关联** | 把睡眠、HRV、静息心率、训练量、饮食放在同一张表里看：昨晚睡得少是不是让今天 HRV 偏低？训练日蛋白质够不够？ |
| **主动发现问题** | 每晚自动检查数据，发现蛋白质连续几天不足、睡眠持续不到 7 小时、体重 7 天平均停滞，主动提醒 |
| **个性化建议** | 基于你自己的数据给出可执行的下一步，例如“午餐再加两个鸡蛋，约补 12g 蛋白质” |
| **诚实地说“不知道”** | 规则里写死了：没数据就写缺失，估算一定给范围和可信度，不编造“超过 90% 同龄人”这类对比 |

### 它能帮你关注哪些方面

- **体重与体成分**：用 7 天平均体重看趋势，过滤掉喝水吃盐带来的 0.5–1 kg 日常波动。
- **能量平衡**：基础代谢（Mifflin-St Jeor 公式）+ 手环活动热量 − 饮食摄入，估算每天的热量缺口。
- **营养结构**：蛋白质是否达到每公斤体重 1.6–2.2g；蔬菜、水果、油盐是否合理。
- **睡眠与恢复**：夜间睡眠时长、深睡比例、夜醒次数、HRV、静息心率，判断身体恢复得怎么样。
- **训练进步**：记录每个动作的重量和次数，对比上一次，按渐进超负荷提示下次怎么加。
- **压力与情绪**：如果手环有压力和情绪数据，也会记进日志，和睡眠、饮食一起看。

### 可以继续扩展的方向

下面这些**还没有实现**，是这套结构天然适合扩展的方向，欢迎提 PR：
- 接入智能体重秤、体脂秤的导出数据，追踪体脂率和肌肉量。
- 解析体检报告（血脂、血糖、尿酸），把饮食建议和指标联系起来。
- 女性生理周期记录，分析周期对体重、睡眠和训练表现的影响。
- 连续血糖仪（CGM）数据，看不同食物对血糖的实际影响。
- 家庭多成员档案，帮长辈记录血压、用药和饮食。
- 月度、季度报告，对比阶段目标。

> ⚠️ **这不是医疗工具**。AI 提供的是基于你数据的记录、整理和生活方式建议，不能替代医生诊断。数据持续异常时请就医。

---

## 日常使用

直接说话即可，不需要记命令：

| 你说 | AI 做什么 |
|------|-----------|
| “晨重 70.5” | 记入体重，更新档案 |
| “早餐一杯牛奶、两个鸡蛋” 或发一张照片 | 估算热量和蛋白质，写入餐食表，告诉你今天还差多少 |
| 发餐前、餐后两张照片 | 按剩余量扣减 |
| 发手环截图，说“同步手环” | 提取睡眠、心率、HRV、步数、活动热量 |
| “今天练了推，卧推 60kg 8/8/7” | 记录训练，对比上一次，提示下次怎么加 |
| “生成今天的日报” / “出周报” | 生成报告并保存 |
| “最近一周蛋白质够吗？” | 查表回答 |

也可以直接调用技能：

| 技能 | Claude Code | Codex |
|------|-------------|-------|
| 记录餐食 | `/record-meal` | `$record-meal` |
| 同步手环 | `/sync-wearable` | `$sync-wearable` |
| 记录训练 | `/record-training` | `$record-training` |
| 日报 | `/daily-report` | `$daily-report` |
| 周报 | `/weekly-report` | `$weekly-report` |

### 定时日报 / 周报（可选）

- **Claude 桌面应用**：侧边栏 Scheduled 新建定时任务，贴入 `routines/` 里的提示词，把 `<DATA_DIR>` 换成你的 `data` 文件夹绝对路径。
- **Codex**：可以用系统定时任务（Windows 任务计划程序 / cron）运行 `codex exec "<routines 里的提示词>"`。这个方式我们还没有完整测试过。

日报每晚检查今天和前两天，有手环数据但还没出日报的就补出，已有的不覆盖。建议日常记录固定在一个对话里，免得同一餐记两次。

---

## 文件结构

```
SETUP.md               写给 AI 助手的安装步骤
AGENTS.md              共享规则（Codex 直接读，Claude Code 通过 CLAUDE.md 导入）
CLAUDE.md              一行 @AGENTS.md 导入
.agents/skills/        技能（Codex 读这里，改技能只改这里）
.claude/skills/        技能副本（Claude Code 读这里，用 sync_skills.py 同步）
routines/              定时日报、周报的提示词
scripts/stats.py       不经过 AI，快速看最近 N 天平均值
scripts/sync_skills.py 把 .agents/skills 同步到 .claude/skills
template/              data/ 的初始结构：配置示例和只有表头的 CSV
data/                  你的数据（.gitignore 排除，不会上传）
```

## 数据表

| 文件 | 内容 |
|------|------|
| `structured/daily_metrics.csv` | 每天一行汇总：体重、摄入范围、蛋白质、睡眠、心率、HRV、步数、活动热量 |
| `structured/meals.csv` | 每餐一行：食物、热量、蛋白质、可信度、备注 |
| `structured/training.csv` | 每次训练一行，动作写在 notes 里 |
| `structured/wearable.csv` | 手环原始指标 |

全是普通 CSV，可以用 Excel 打开，也可以导入任何分析工具。数据只在你的电脑上。

```bash
python scripts/stats.py --days 7      # 最近 7 天平均值，只用标准库
python scripts/sync_skills.py --check # 检查两套技能是否一致
```

## 局限

- 照片估算热量的误差可能有 20–40%。称重或看包装标签能明显提高准确度。
- 热量消耗是估算值。判断减脂是否有效，以 7 天平均体重的变化为准。
- 手环截图识别以华为运动健康测试过，其他 App 字段类似，但未逐一验证。

## 许可

[MIT](LICENSE)
