# Discipline Domain

tag: discipline, sport, activity, template, rule, stage

## Overview

The Discipline domain defines and organizes competitive activities, their variations, and competition structures. It provides a flexible foundation for modeling sports, games, and other competitive pursuits within the tournament system, supporting standardized rules, stages, and awards.

## Purpose

- Enable clear, consistent definition and organization of disciplines and activities.
- Support discipline-specific rules, variations, and competition formats.
- Facilitate multi-discipline tournament organization and award management.

## Structure

The domain consists of template entities and supporting models for discipline management:

| Entity/Model | Description |
|--------------|-------------|
| [Discipline](discipline.md) | Defines a specific form of competition within an activity (e.g., "Tennis Singles", "Freestyle Swimming"). |
| [Activity](activity/activity.md) | Represents a specific event or activity within a discipline (e.g., "5v5 Basketball Tournament"). |
| [Domain](activity/domain.md) | Groups related activities (e.g., "Sports", "Esports", "Board Games"). |
| [Stage](stage/stage.md) | Defines competition progression and structure (e.g., "Playoffs", "Group Stage"). |
| [Variation](activity/variation/variation.md) | Defines alternative ways to play within a discipline (e.g., "Blitz Rules", "No-Ad Scoring"). |
| [Rule](activity/variation/rule.md) | Specifies individual rules and their enforcement. |
| [Award](award.md) | Defines recognition and prizes for achievements. |

## See Also

- [Discipline](discipline.md)
- [Activity](activity/activity.md)
- [Domain](activity/domain.md)
- [Stage](stage/stage.md)
- [Variation](activity/variation/variation.md)
- [Rule](activity/variation/rule.md)
- [Award](award.md)
- [Team Domain](../team/README.md)
- [Tournament Domain](../tournament/README.md)
- [Foundation Domain](../foundation/README.md)
