from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
ASSETS = "https://raw.githubusercontent.com/SayGGGo/pythonProjectAI_learn/master/.github/assets/buttons"
DOWNLOAD = "https://github.com/Alexander4409/pythonProjectAI_learn/archive/refs/heads/master.zip"
FORK = "https://github.com/Alexander4409/pythonProjectAI_learn/fork"
TEACHER = "https://github.com/Alexander4409/"


def button(path, alt, width):
    return f'<img src="{path}" alt="{alt}" width="{width}">' 


def lesson_files(folder):
    return sorted(folder.glob("*.py"), key=lambda item: (natural_key(item.name), item.name.lower()))


def natural_key(value):
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", value)]


def group_info(folder):
    name = folder.name
    if name == "ИИ_Вовлекай":
        return "Вовлекай", "Онлайн-занятия по искусственному интеллекту.", "online"
    match = re.match(r"(ИИ|ИЭ)_(\d)(\d)_кем$", name)
    if not match:
        return name, "Учебные материалы и код с занятий.", "group"
    direction, grade, group = match.groups()
    return f"{direction}-{grade}{group}", f"{grade} класс · {group} группа · направление {direction}", "group"


def lesson_table(folder):
    lessons = lesson_files(folder)
    rows = []
    for index, lesson in enumerate(lessons, 1):
        rows.append(f'| {index} | `{lesson.name}` | <a href="{lesson.name}">{button(f"{ASSETS}/open.svg", "Открыть", 105)}</a> |')
    return "\n".join(rows) if rows else "| — | Уроки пока не опубликованы | — |"


def group_readme(folder):
    title, description, _ = group_info(folder)
    table = lesson_table(folder)
    return f'''# {title}

{description}

## Быстрые действия

<a href="../README.md">{button(f"{ASSETS}/back.svg", "Назад", 115)}</a>
<a href="{DOWNLOAD}">{button(f"{ASSETS}/download.svg", "Скачать", 125)}</a>
<a href="{FORK}">{button(f"{ASSETS}/fork.svg", "Форк", 95)}</a>

## Уроки

| № | Файл | Действие |
|---:|---|---|
{table}
'''


def update_group_readme(folder):
    readme = folder / "README.md"
    if not readme.exists():
        readme.write_text(group_readme(folder), encoding="utf-8")
        return
    current = readme.read_text(encoding="utf-8")
    section = f"## Уроки\n\n| № | Файл | Действие |\n|---:|---|---|\n{lesson_table(folder)}\n"
    if re.search(r"(?ms)^## Уроки\s*\n.*\Z", current):
        current = re.sub(r"(?ms)^## Уроки\s*\n.*\Z", section, current)
    else:
        current = current.rstrip() + "\n\n" + section
    readme.write_text(current, encoding="utf-8")


def folder_button(folder):
    title, _, kind = group_info(folder)
    if kind == "online":
        filename = "vovlekai-online.svg"
    else:
        match = re.match(r"(ИИ|ИЭ)_(\d)(\d)_кем$", folder.name)
        prefix = "ii" if match and match.group(1) == "ИИ" else "ie"
        filename = f"{prefix}-{match.group(2)}{match.group(3)}-kem.svg" if match else ""
    if not filename or not (ROOT / ".github" / "assets" / "buttons" / filename).exists():
        return f'<a href="{folder.name}/README.md">{title}</a>'
    return f'<a href="{folder.name}/README.md">{button(f"{ASSETS}/{filename}", title, 125)}</a>'


def main_readme(folders):
    regular = [folder for folder in folders if folder.name != "ИИ_Вовлекай"]
    ii = [folder for folder in regular if folder.name.startswith("ИИ_")]
    ie = [folder for folder in regular if folder.name.startswith("ИЭ_")]
    online = [folder for folder in folders if folder.name == "ИИ_Вовлекай"]
    ii_buttons = "\n".join(folder_button(folder) for folder in ii)
    ie_buttons = "\n".join(folder_button(folder) for folder in ie)
    online_buttons = "\n".join(folder_button(folder) for folder in online)
    return f'''<div align="center">

# Обучение УникУм

Весь код с занятий.

</div>

## Выберите группу

### ИИ — искусственный интеллект

<div align="center">
{ii_buttons}
</div>

### ИЭ

<div align="center">
{ie_buttons}
</div>

### Онлайн-занятия

<div align="center">
{online_buttons}
</div>

## Быстрые действия

<div align="center">
<a href="{TEACHER}">{button(f"{ASSETS}/teacher.svg", "Преподаватель", 145)}</a>
<a href="{DOWNLOAD}">{button(f"{ASSETS}/download.svg", "Скачать", 115)}</a>
<a href="{FORK}">{button(f"{ASSETS}/fork.svg", "Форк", 95)}</a>
</div>
'''


def main():
    folders = sorted(
        [item for item in ROOT.iterdir() if item.is_dir() and item.name != "assets" and not item.name.startswith(".")],
        key=lambda item: item.name.lower(),
    )
    for folder in folders:
        update_group_readme(folder)
    print(f"Обновлено групп: {len(folders)}")


if __name__ == "__main__":
    main()
