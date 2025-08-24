---
tags:
  - points-system
  - template-entity
  - scoring
  - standings
  - match-outcomes
---

# Points System (Template Entity)

## Overview

A Points System is a reusable ruleset for awarding points based on match outcomes (win, draw, loss, forfeit). It’s used to compute standings within a stage or tournament context. The template defines the rules; actual awarded points are calculated from event results at runtime.

## Purpose

- Standardize how points are awarded across disciplines and tournaments.
- Ensure consistent, transparent standings calculation within a Stage.
- Support clear handling of forfeits by defining defaults for forfeit outcomes.
- Allow different stages to use different points systems where needed.

---

## Structure

This template entity includes standard attributes from the [Base Entity](../../foundation/base_entity.md).

### Attributes

| Attribute        | Description                                                            | Type   | Required | Notes / Example                                                             |
| ---------------- | ---------------------------------------------------------------------- | ------ | -------- | --------------------------------------------------------------------------- |
| **Name**         | A unique, human-readable name for the points system template.          | String | Yes      | `"Standard Soccer (3-1-0)"`, `"Chess Classic (1-0.5-0)"`                    |
| **Description**  | A detailed explanation of the system or its common use case.           | Text   | No       | `"Standard 3 points for a win, 1 for a draw, 0 for a loss."`                |
| **Win**          | Points awarded for winning a match.                                    | Number | Yes      | `3`                                                                         |
| **Draw**         | Points awarded for a drawn or tied match.                              | Number | Yes      | `1`                                                                         |
| **Loss**         | Points awarded for losing a match.                                     | Number | Yes      | `0`                                                                         |
| **Forfeit Win**  | Points awarded for winning a match by forfeit (opponent did not play). | Number | No       | Defaults to `Win` points if not specified. Example: `3`                     |
| **Forfeit Loss** | Points awarded for losing a match by forfeit (did not play).           | Number | No       | Defaults to `Loss` points if not specified. Example: `0` or negative values |

<!-- Relationships and detailed considerations omitted per documentation style. -->

## Example

### Example: Standard Soccer (3-1-0)

```mermaid
graph TD
  P[Points System]
  P --> N[Name: Standard Soccer (3-1-0)]
  P --> D[Description: 3 for Win, 1 for Draw, 0 for Loss]
  P --> W[Win: 3]
  P --> DR[Draw: 1]
  P --> L[Loss: 0]
  P --> FW[Forfeit Win: 3]
  P --> FL[Forfeit Loss: 0]
```

This diagram covers all attributes of the Points System: Name, Description, Win, Draw, Loss, Forfeit Win, and Forfeit Loss. It matches the common soccer scoring convention used to compute standings.

### Example: Chess Classic (1-0.5-0)

```mermaid
graph TD
  P[Points System]
  P --> N[Name: Chess Classic (1-0.5-0)]
  P --> D[Description: 1 for Win, 0.5 for Draw, 0 for Loss]
  P --> W[Win: 1]
  P --> DR[Draw: 0.5]
  P --> L[Loss: 0]
  P --> FW[Forfeit Win: 1]
  P --> FL[Forfeit Loss: 0]
```

This example also represents all attributes, reflecting the standard way chess tournaments award points. Forfeits align with the base outcomes unless tournament rules specify otherwise.

### Notes

- Win/Draw/Loss values should be non-negative; if negative values are allowed for special cases (e.g., penalties), document explicitly.
- Forfeit Win defaults to Win; Forfeit Loss defaults to Loss unless specified.
- Changing point values mid-stage should be avoided to keep standings stable and fair.

## See Also

- [Stage](../../discipline/stage/stage.md)
- [Stage Tiebreaker](../../discipline/stage/stage_tiebreaker.md)
- [Seeding System](../../discipline/stage/seeding_system.md)
- [Promotion Rule](../../discipline/stage/promotion_rule.md)
- [Variation](../activity/variation/variation.md)
- [Score](../../schedule/score.md)
- [Standing](../../standing/standing.md)
- [Tournament](../../tournament/tournament.md)
- [Team](../../team/team.md)

---
