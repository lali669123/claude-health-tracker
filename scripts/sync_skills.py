#!/usr/bin/env python3
"""把 .agents/skills/ 同步到 .claude/skills/，让 Codex 和 Claude Code 用同一套技能。

改技能时只改 .agents/skills/，然后运行：python scripts/sync_skills.py
加 --check 只检查两边是否一致（不一致时返回 1）。
"""
import argparse
import filecmp
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / ".agents" / "skills"
DST = ROOT / ".claude" / "skills"


def differences():
    if not DST.exists():
        return ["(.claude/skills 不存在)"]
    cmp = filecmp.dircmp(SRC, DST)
    out = []

    def walk(c, prefix=""):
        out.extend(prefix + n for n in c.left_only + c.right_only + c.diff_files)
        for name, sub in c.subdirs.items():
            walk(sub, f"{prefix}{name}/")

    walk(cmp)
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    diff = differences()
    if args.check:
        print("一致" if not diff else "不一致：" + ", ".join(diff))
        sys.exit(1 if diff else 0)

    if DST.exists():
        shutil.rmtree(DST)
    shutil.copytree(SRC, DST)
    print(f"已同步 {sum(1 for _ in SRC.rglob('SKILL.md'))} 个技能到 .claude/skills/")


if __name__ == "__main__":
    main()
