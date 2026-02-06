# T-Lab Skills Generator 🪄

T-Labの理念「TEACHERS TECHNOLOGY TRANSFORMING」に基づいた、AIスキルの生成・管理プロジェクトです。

## 🌟 プロジェクトの概要

このリポジトリは、GitHubの School-Agent が公開している [skill-creator](https://github.com/School-Agent-Inc/orchestrate-it/tree/main/.antigravity/skills/skill-creator) をベースに、T-Labの生徒が使いやすいようにリメイクしたものです。

先生が「1/1000の魔法使い」になり、自分自身の「余白（よはく）」を創り出すためのツール（スキル）を簡単に作成するためのガイドとテンプレートが含まれています。

## 🧙 含まれている主なスキル

- **t-lab-skill-creator**: T-Lab流の新しいスキルを設計・作成するためのメインスキル。

## 🚀 使い方

詳細は `.agent/workflows/create-new-skill.md` を参照してください。

### 新しいスキルの作成

```bash
python .agent/skills/t-lab-skill-creator/scripts/init_tlab_skill.py <skill-name> --path .agent/skills
```

---
Designed with ❤️ by T-Lab
