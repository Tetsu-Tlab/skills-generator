#!/usr/bin/env python3
"""
T-Lab スキル検証スクリプト
"""

import sys
import re
import yaml
from pathlib import Path

def validate_skill(skill_path):
    skill_path = Path(skill_path)
    skill_md = skill_path / 'SKILL.md'
    
    if not skill_md.exists():
        return False, "❌ SKILL.md が見つかりません！"

    content = skill_md.read_text(encoding='utf-8')
    
    # Check YAML Frontmatter
    if not content.startswith('---'):
        return False, "❌ YAMLフロントマターがありません！"

    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return False, "❌ フロントマターの形式がおかしいよ！"

    try:
        frontmatter = yaml.safe_load(match.group(1))
        if not isinstance(frontmatter, dict):
            return False, "❌ フロントマターは辞書形式にしてね！"
    except yaml.YAMLError as e:
        return False, f"❌ YAMLが読み込めないよ: {e}"

    # Required fields
    for field in ['name', 'description']:
        if field not in frontmatter:
            return False, f"❌ フロントマターに '{field}' が足りないよ！"

    # TODO Check
    if '[TODO:' in content:
        return False, "❌ まだ [TODO:] が残ってるよ！魔法を完成させよう！✨"

    return True, "✅ 完璧だよ！素晴らしいスキルができあがったね！✨"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用方法: python quick_validate.py <skill_directory>")
        sys.exit(1)

    valid, message = validate_skill(sys.argv[1])
    print(message)
    sys.exit(0 if valid else 1)
