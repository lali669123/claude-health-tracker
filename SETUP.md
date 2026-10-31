# 安装说明（写给 AI 助手）

用户把 README 里的提示词发给了你（Claude Code 或 Codex），请按下面的步骤帮他装好这套健康记录方案。每一步做完简短告诉用户结果，遇到问题先说明原因再继续。

## 原则

- 只在安装目录里创建和修改文件，不改系统设置，不需要管理员权限。
- 已有的 `data/` 是用户的个人数据，任何情况下都不要覆盖或删除。
- 不要把用户数据上传到任何地方。

## 1. 确定安装位置

问用户装在哪里，默认是用户主目录下的 `claude-health-tracker` 文件夹（Windows 例如 `C:\Users\<用户名>\claude-health-tracker`）。

如果这个文件夹已经存在：
- 是这个项目的旧版本（有 `AGENTS.md` 和 `.git`）：在里面运行 `git pull` 更新即可，`data/` 不受影响。然后跳到第 5 步。
- 是别的内容：请用户换一个位置。

## 2. 下载项目

有 git 时：

```bash
git clone https://github.com/lali669123/claude-health-tracker.git <安装位置>
```

没有 git 时，下载压缩包解压，并把解压出的 `claude-health-tracker-main` 文件夹改名为安装位置：

- Windows PowerShell：
  ```powershell
  Invoke-WebRequest https://github.com/lali669123/claude-health-tracker/archive/refs/heads/main.zip -OutFile cht.zip
  Expand-Archive cht.zip -DestinationPath .
  Remove-Item cht.zip
  ```
- macOS / Linux：
  ```bash
  curl -fsSL -o cht.zip https://github.com/lali669123/claude-health-tracker/archive/refs/heads/main.zip
  unzip cht.zip && rm cht.zip
  ```

## 3. 初始化数据

在安装目录里，`data/` 不存在时才执行：把 `template/` 整个复制为 `data/`。

## 4. 建立个人档案

一次问完下面几个问题（用户可以跳过任何一项，跳过的留空）：

1. 身高（cm）、出生日期、性别
2. 现在的体重（kg），知道的话
3. 主要目标：减脂、增肌、减脂增肌、维持，或其他
4. 用什么手环或健康 App（例如华为运动健康、Apple 健康、小米运动）
5. 平时怎么吃饭：食堂、外卖、自己做
6. 有没有过敏或忌口
7. 每周训练几次，练什么

按回答填写：
- `data/config/profile.json`：personal_info、health_baseline、goals、training、wearable、dietary。
- `data/config/goals.json`：先保留模板里的默认值。用户给了体重时，在 notes 里写明蛋白质参考范围（体重 × 1.6–2.2 g）。
- 用户给了当前体重：同时在 `data/structured/daily_metrics.csv` 加一行今天的记录（只填 date 和 weight_kg，其余留空，保持 21 列），并写入 profile.json 的 initial_weight 和 current_weight。

## 5. 检查

- 确认 `AGENTS.md`、`.agents/skills/`、`.claude/skills/`、`data/structured/` 下四个 CSV 都在。
- 有 Python 时运行 `python scripts/sync_skills.py --check`，应输出「一致」。

## 6. 告诉用户怎么开始

规则和技能在会话开始时加载，所以要请用户**在安装目录里开一个新会话**：

- Claude Code 命令行：`cd <安装位置>` 然后 `claude`
- Claude 桌面应用：新建会话时选择这个文件夹
- Codex：`cd <安装位置>` 然后 `codex`

然后给用户几句示例：
- “晨重 70.5”
- “早餐一杯牛奶、两个鸡蛋”，或直接发一张照片
- 发手环截图，说“同步手环”
- “生成今天的日报”

最后提一句：想要每晚自动出日报、每周六出周报，可以看 `routines/` 里的说明。
