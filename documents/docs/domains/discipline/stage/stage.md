---
tags:
  - stage
  - template-entity
  - tournament-structure
  - advancement
  - grouping
---

# Stage (Template Entity)

## Overview

A Stage defines how teams are grouped, matched, and advance (e.g., Group Stage, Knockout). Discipline references one Activity; each Stage selects the Activity Variation that applies.

---

## Structure

This template entity includes standard attributes from the [Base Entity](../../foundation/base_entity.md).

### Attributes

| Attribute              | Description                                                                                                                        | Type       | Required | Notes / Example                                                                |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------- | -------- | ------------------------------------------------------------------------------ |
| Name                   | Title for the Stage                                                                                                                | String     | Yes      | "Playoffs", "Group Stage A", "Championship Finals"                             |
| Description            | Purpose and structure                                                                                                              | String     | Yes      | "Top 16 teams compete in a single elimination bracket."                         |
| Activity Variation     | Embedded [Variation](../activity/variation/variation.md) that applies                                  | Variation  | Yes      | Selected way to play the Activity at this Stage                                 |
| Min Teams              | Minimum teams required                                                                                                              | Integer    | Optional | 8                                                                                |
| Max Teams              | Maximum teams allowed                                                                                                               | Integer    | Optional | 16                                                                               |
| Phase                  | Ordered list of embedded [Stage Phase](stage_phase.md)                                                                              | List[Stage Phase] | Optional | [Group Matches] or [R16, QF, SF, Final]                                         |
| Format                 | Embedded [Stage Format](stage_format.md)                                                                                            | Stage Format | Yes   | "Single Elimination" or "Round Robin"                                          |
| Match System           | Embedded [Match System](match_system/match_system.md)                                                                               | Match System | Yes  | "Best-of-3" or "Single Game"                                                   |
| Points System          | Optional embedded [Points System](points_system.md)                                                                                | Points System | Optional | "3 points for win"                                                              |
| Seeding System         | Optional embedded [Seeding System](seeding_system.md)                                                                              | Seeding System | Optional | Based on qualification rank                                                      |
| Promotion Rule         | Optional embedded [Promotion Rule](promotion_rule.md)                                                                               | Promotion Rule | Optional | "Top 2 teams advance"                                                           |
| Team Format            | Optional embedded [Team Format](team_format.md)                                                                                    | Team Format | Optional | "5v5 Roster"                                                                     |
| Team Creation          | Optional embedded [Team Creation](team_creation.md)                                                                                | Team Creation | Optional | How teams are formed/registered                                                  |
| Tiebreakers            | Ordered list of embedded [Stage Tiebreaker](stage_tiebreaker.md) used when determining advancement                                 | List[Stage Tiebreaker] | Yes | [H2H, Score Diff]                                                                |

---

## Example

### Example: Group Stage with Round Robin

```mermaid
graph TD
  S[Stage]
  S --> N[Name: Group Stage]
  S --> DS[Description: Round-robin groups determine rankings]
  S --> V[Activity Variation: 5v5 (embedded Variation)]
  S --> PH[Phase: Group Matches]
  S --> F[Format: Round Robin]
  F --> FMIN[Min Group Size: 3]
  F --> FMAX[Max Group Size: 6]
  S --> MS[Match System: Best-of-3]
  MS --> MU1[Unit: Set]
  MS --> MU2[Unit: Set]
  MS --> MU3[Unit: Set]
  MS --> MT[Match Tiebreakers: None]
  S --> P[Points System: 3 for Win]
  P --> PW[Win: 3]
  P --> PD[Draw: 1]
  P --> PL[Loss: 0]
  S --> SE[Seeding System: By Ranking]
  SE --> STYPE[Type: RANKING]
  SE --> RSRC[Ranking Source: Regional U18]
  S --> PR[Promotion Rule: Top 2 advance]
  PR --> TOPN[Top N: 2]
  S --> TMN[Min Teams: 8]
  S --> TMX[Max Teams: 16]
  S --> TF[Team Format: 5v5 Roster]
  TF --> TFSZ[Active Size: 5]
  S --> TC[Team Creation: Registered Teams]
  TC --> TCM[Method: PreRegistered]
  S --> TB[Tiebreakers: H2H, Score Diff]
  TB --> TB1[H2H]
  TB --> TB2[Score Diff]
```

This example represents all Stage attributes: Name, Description, Activity Variation (embedded), Min/Max Teams, Format, Match System, Points System, Seeding System, Promotion Rule, Team Format, Team Creation, and Tiebreakers. It shows a Round Robin Group Stage with Best-of-3 matches, 3 points for a win, ranking-based seeding, and Top 2 promotion.

### Example: Knockout Stage with Single Elimination

```mermaid
graph TD
  S[Stage]
  S --> N[Name: Knockout Stage]
  S --> DS[Description: Single-elimination bracket determines winner]
  S --> V[Activity Variation: 3v3 (embedded Variation)]
  S --> PH[Phase: R16, QF, SF, Final]
  S --> F[Format: Single Elimination]
  F --> ELIM[Loser Eliminated]
  S --> MS[Match System: Single Game]
  MS --> MU[Unit: Game]
  MS --> MT[Match Tiebreakers: None]
  S --> P[Points System: Not used]
  S --> SE[Seeding System: By Group Results]
  SE --> STYPE2[Type: PERFORMANCE]
  S --> PR[Promotion Rule: Winner advances]
  PR --> ADV[Advance: 1]
  S --> TMN[Min Teams: 8]
  S --> TMX[Max Teams: 16]
  S --> TF[Team Format: 3v3 Roster]
  S --> TC[Team Creation: Qualified from Groups]
  S --> TB[Tiebreakers: H2H, Score Diff]
```

This example represents all Stage attributes. It uses a Single Elimination format with single-game matches, no points system, seeding from group results, winner-advances promotion, 3v3 roster, and team creation via qualification from groups.

### Notes

- Min Teams must be <= Max Teams.
- Phase order must be unique and strictly increasing where numeric (e.g., R16 < QF < SF < Final).
- If Format uses groups, group sizes should be compatible with Min/Max Teams; the system may round or auto-balance.
- Stage Tiebreakers are evaluated in listed order.

## See Also

- [Stage Format](stage_format.md)
- [Stage Phase](stage_phase.md)
- [Stage Tiebreaker](stage_tiebreaker.md)
- [Promotion Rule](promotion_rule.md)
- [Points System](points_system.md)
- [Seeding System](seeding_system.md)
- [Match System](match_system/match_system.md)
- [Team Format](team_format.md)
- [Team Creation](team_creation.md)
- [Activity](../activity/activity.md)
- [Variation](../activity/variation/variation.md)
- [Discipline](../discipline.md)
- [Tournament](../../tournament/tournament.md)
- [Team](../../team/team.md)
