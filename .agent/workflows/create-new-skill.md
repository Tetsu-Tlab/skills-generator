---
description: T-Lab流の新しいスキルを作成するワークフロー
---

1. `.agent/skills/t-lab-skill-creator/scripts/init_tlab_skill.py` を実行して、スキルの雛形を作ります。
   - 例：`python .agent/skills/t-lab-skill-creator/scripts/init_tlab_skill.py my-magic-skill --path .agent/skills`
2. 作成された `.agent/skills/my-magic-skill/SKILL.md` を開き、[TODO] 項目を埋めます。
   - このとき、T-Labの「4つのシンボル」や「遊び心」を魔法のように吹き込みましょう！✨
3. 検証スクリプトを実行して、記述漏れがないか確認します。
   - 例：`python .agent/skills/t-lab-skill-creator/scripts/quick_validate.py .agent/skills/my-magic-skill`
4. Antigravityに「新しいスキルを作ったよ！」と伝えて、実際に試してみましょう！🚀
