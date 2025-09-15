---
tags:
  - team-ranking
  - entity
  - ranking-position
  - competition
  - seeding
  - tournament-management
---

# Team Ranking (Entity)

## Overview

A Team Ranking represents a concrete ranking instance for a specific team within a Ranking System
and Ranking Period. As an entity with independent identity and lifecycle, it tracks the team's
current position, points, and performance metrics used for tournament seeding, qualification
decisions, and competitive analysis.

## Purpose

This entity provides concrete ranking instances that enable:

- Accurate tournament seeding based on established ranking positions
- Historical performance tracking and trend analysis across ranking periods
- Qualification determination for tournaments and competitive events
- Fair competitive balance through merit-based team placement
- Integration with tournament creation and seeding system workflows

## Structure

This entity includes standard attributes from the [Base Entity](../foundation/base_entity.md)
and adds the following team ranking-specific attributes:

| Attribute | Description | Type | Required | Notes / Example |
|-----------|-------------|------|----------|-----------------|
| **Team** | Reference to the ranked team entity | UUID | Yes | Links to [Team](../team/team.md) entity |
| **Ranking System** | Reference to the ranking calculation methodology | UUID | Yes | Links to [Ranking System](system.md) template |
| **Ranking Period** | Reference to the time-based ranking cycle | UUID | Yes | Links to [Ranking Period](period.md) template |
| **Current Position** | Team's current numerical ranking position | Integer | Yes | `1`, `5`, `127` (1 = highest rank) |
| **Previous Position** | Team's ranking position in previous calculation | Integer | Optional | `3`, `8`, `142` (for movement tracking) |
| **Ranking Points** | Embedded point breakdown and calculation details | Ranking Points | Yes | Point totals, components, earning details |
| **Qualification Status** | Team's eligibility status for ranking-based events | Enum | Yes | `QUALIFIED`, `CONDITIONAL`, `NOT_QUALIFIED`, `UNDER_REVIEW` |
| **Last Updated** | Timestamp of most recent ranking calculation | DateTime | Yes | `"2024-09-15T14:30:00Z"` |
| **Calculation Date** | Date when current ranking was officially calculated | Date | Yes | `"2024-09-15"` |
| **Movement** | Position change since previous ranking | Integer | Optional | `+3` (improved), `-2` (declined), `0` (unchanged) |
| **Ranking Criteria Met** | Embedded criteria compliance and performance data | Ranking Criteria | Yes | Minimum tournaments, qualification thresholds |
| **Performance Window** | Time period contributing to current ranking | String | Optional | `"Last 12 months"`, `"2024 season"`, `"Rolling 18 months"` |
| **Discipline Context** | Discipline-specific ranking context if applicable | UUID | Optional | Links to [Discipline](../discipline/README.md) if discipline-specific |

## Example

### Example: Professional Tennis Ranking

```mermaid
graph TD
  TR[Team Ranking: Novak's Current Position]
  TR --> T[Team: Novak Djokovic Team]
  TR --> RS[Ranking System: ATP Professional Rankings]
  TR --> RP[Ranking Period: 2024 Annual Cycle]
  TR --> CP[Current Position: 3]
  TR --> PP[Previous Position: 2]
  TR --> RPT[Ranking Points: 7160 ATP Points]
  TR --> QS[Qualification Status: QUALIFIED]
  TR --> LU[Last Updated: 2024-09-15T14:30:00Z]
  TR --> CD[Calculation Date: 2024-09-15]
  TR --> M[Movement: -1 (declined one position)]
  TR --> RC[Ranking Criteria Met: All requirements]
  TR --> PW[Performance Window: Rolling 52 weeks]
  TR --> DC[Discipline Context: Professional Tennis]
```

This example demonstrates a professional tennis player's ranking within the ATP system. The ranking
shows the current position of 3rd, previous position of 2nd (indicating a decline of one position),
and total ATP points of 7160. The player maintains qualified status with all ranking criteria met
over the rolling 52-week performance window. This covers all Team Ranking attributes including
movement tracking, qualification status, and time-based calculation details.

### Example: Youth Regional Ranking

```mermaid
graph TD
  TR[Team Ranking: Regional Youth Team]
  TR --> T[Team: City Tennis Academy U16]
  TR --> RS[Ranking System: Regional Youth Points]
  TR --> RP[Ranking Period: Youth Rolling Rankings]
  TR --> CP[Current Position: 12]
  TR --> PP[Previous Position: 15]
  TR --> RPT[Ranking Points: 485 Regional Points]
  TR --> QS[Qualification Status: CONDITIONAL]
  TR --> LU[Last Updated: 2024-09-01T10:00:00Z]
  TR --> CD[Calculation Date: 2024-09-01]
  TR --> M[Movement: +3 (improved three positions)]
  TR --> RC[Ranking Criteria Met: 8 of 10 tournaments]
  TR --> PW[Performance Window: Last 12 months]
  TR --> DC[Discipline Context: Youth Tennis]
```

This second example shows a youth team's regional ranking with conditional qualification status.
The team improved from 15th to 12th position with 485 points but needs two more tournaments to
meet full qualification criteria. The monthly update cycle and 12-month performance window
demonstrate different configuration options for youth development programs.

## See Also

- [Ranking System](system.md) - Ranking calculation methodology templates
- [Ranking Period](period.md) - Time-based ranking cycle configuration
- [Ranking History](history.md) - Historical ranking change tracking
- [Ranking Points](points.md) - Embedded point calculation components
- [Ranking Criteria](criteria.md) - Embedded qualification parameters
- [Team](../team/team.md) - Ranked team entities
- [Seeding System](../discipline/stage/seeding_system.md) - Tournament seeding integration
- [Standing](../standing/standing.md) - In-tournament performance tracking
- [Tournament](../tournament/tournament.md) - Tournament seeding and qualification
