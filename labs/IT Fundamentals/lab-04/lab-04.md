---
type: lab
title: Лабораторная работа №4 — Организация Python-проекта
created: 2026-10-08
updated: 2026-10-15
status: needs-review
tags: [subject/it-fundamentals, sem-1, lab, python, architecture]
sources:
  - [[source-it-fundamentals-labs]]
---

# Лабораторная работа №4 — Организация Python-проекта

## Goal and assignment

* **Дисциплина:** Введение в информационные технологии (ВвИТ)
* **Тема:** Модульная архитектура проекта на Python, организация пакетов (`__init__.py`), вынос конфигурации в `config.json`, логирование и управление зависимостями (`requirements.txt`).
* **Методичка:** [[Методичка ВвИТ 8 лаб 2026.pdf]] в `raw/assignments/IT Fundamentals/`.

## Method and reproduction

* **Структура проекта:** `measurement_project/`
  * Модули: `utils/reader.py` (чтение данных), `utils/statistics.py` (статистический расчёт).
  * Конфигурация: `config.json`
  * Зависимости: `requirements.txt`
  * Тесты: `test.py`
* **Файлы отчёта:**
  * Исходник отчёта: `[[Бородин_Л4.docx]]`
  * Итоговый отчёт: `[[Бородин_Л4.pdf]]`

## Result and evidence

* Разработан модульный проект с разделением зон ответственности (ввод/вывод, бизнес-логика, утилиты).
* Настроено логирование событий приложения в `logs/app.log`.
* Проведено тестирование компонентов через `test.py`.

## AI disclosure

* Проект и отчёт выполнены самостоятельно.
