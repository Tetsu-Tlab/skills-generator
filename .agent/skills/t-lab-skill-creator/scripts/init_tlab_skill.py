#!/usr/bin/env python3
"""
T-Lab スキル初期化スクリプト - T-Lab流テンプレートから新しいスキルを作成
"""

import sys
from pathlib import Path

SKILL_TEMPLATE = """---
name: {skill_name}
description: |
  [TODO: スキルの概要を一言で]
  "TEACHERS TECHNOLOGY TRANSFORMING" の精神で、先生の余白を創出します。
  Use when: [TODO: キーワード1, キーワード2]
  Do not use when: [TODO: 除外条件1]
---

# 🪄 {skill_title}

[TODO: このスキルがどのような「魔法」をかけるか、1-2文で説明。遊び心を忘れずに！]

## 💡 T-Lab 理念の反映

このスキルは以下の要素を重視しています：
- 🌱 **Growth**: [TODO: どう成長を促すか]
- ⚙️ **Efficiency**: [TODO: どう効率化するか]

## 🪄 このスキルを使用する時

- [TODO: シーン1]
- [TODO: シーン2]

## 🚫 このスキルを使用しない時

- [TODO: 除外シーン1]

---

## 🏗️ ワークフロー

### Step 1: 🌱 ヒアリングと「余白」の確認
[TODO: 先生が何を解決したいか、どんな余白を作りたいか確認する手順]

### Step 2: ✨ 魔法の発動（生成/処理）
[TODO: 具体的な生成手順や処理内容を記載]

---

## 📝 アウトプット形式

[TODO: 出力されるもののイメージ。プレミアムでワクワクする形式を！]

---

## 📚 参照 (References)
- [ガイドライン](references/guidelines.md)
"""

def title_case_skill_name(skill_name):
    return ' '.join(word.capitalize() for word in skill_name.split('-'))

def init_skill(skill_name, path):
    skill_dir = Path(path).resolve() / skill_name

    if skill_dir.exists():
        print(f"❌ エラー: ディレクトリが既に存在します: {skill_dir}")
        return None

    try:
        skill_dir.mkdir(parents=True, exist_ok=False)
        (skill_dir / "scripts").mkdir(exist_ok=True)
        (skill_dir / "references").mkdir(exist_ok=True)
        (skill_dir / "assets").mkdir(exist_ok=True)
        print(f"✅ T-Lab流スキルディレクトリを作成: {skill_dir}")
    except Exception as e:
        print(f"❌ 作成エラー: {e}")
        return None

    skill_title = title_case_skill_name(skill_name)
    skill_content = SKILL_TEMPLATE.format(
        skill_name=skill_name,
        skill_title=skill_title
    )

    skill_md_path = skill_dir / 'SKILL.md'
    try:
        skill_md_path.write_text(skill_content, encoding='utf-8')
        print("✅ T-Lab流 SKILL.md を作成しました！魔法を吹き込もう！✨")
    except Exception as e:
        print(f"❌ SKILL.md作成エラー: {e}")
        return None

    return skill_dir

def main():
    if len(sys.argv) < 4 or sys.argv[2] != '--path':
        print("使用方法: python init_tlab_skill.py <skill-name> --path <path>")
        sys.exit(1)

    skill_name = sys.argv[1]
    path = sys.argv[3]

    print(f"🚀 T-Lab スキルを初期化中... {skill_name}")
    result = init_skill(skill_name, path)
    sys.exit(0 if result else 1)

if __name__ == "__main__":
    main()
