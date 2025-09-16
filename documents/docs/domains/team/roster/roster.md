---
tags:
- roster
- template-entity
- team
- player
- competition
---

# Roster (Template Entity)

## Overview

A Roster Template Entity defines a reusable blueprint for roster structures and configurations that can be used to
create specific roster instances. It provides a standardized framework for roster types, player roles, and team
composition patterns that can be applied across different contexts and tournaments.

## Purpose

The Roster Template Entity enables tournament organizers to:

- Standardize team composition rules across competitions
- Define player role categories and limitations
- Establish consistent roster requirements for different sports
- Create reusable roster configurations for tournaments
- Ensure compliance with discipline-specific rules
- Streamline team registration and validation processes

## Structure

This Template Entity includes the standard attributes defined in the [Base Entity](../../foundation/base_entity.md).

| Attribute       | Description                                                                 | Type          | Required | Notes / Example                                |
| --------------- | --------------------------------------------------------------------------- | ------------- | -------- | ---------------------------------------------- |
| **Players**     | List of main players in the roster                                        | List[Player]  | Yes      | Starting lineup and active players             |
| **Substitutes** | List of substitute players available for rotation                          | List[Player]  | Yes      | Bench players ready to enter the game         |
| **Reserves**    | List of reserve players for additional squad depth                        | List[Player]  | Optional | Extra players for emergency situations         |

## Example

```mermaid
graph TD
    R[Roster: Basketball Team<br/>Instance of Roster Template] --> P[Players<br/>List[Player]]
    R --> S[Substitutes<br/>List[Player]]
    R --> Res[Reserves<br/>List[Player]]
    
    P --> P1[Player 1: Point Guard]
    P --> P2[Player 2: Shooting Guard]
    P --> P3[Player 3: Small Forward]
    P --> P4[Player 4: Power Forward]
    P --> P5[Player 5: Center]
    
    S --> S1[Sub 1: Guard]
    S --> S2[Sub 2: Forward]
    S --> S3[Sub 3: Center]
    
    Res --> R1[Reserve 1: Utility]
    Res --> R2[Reserve 2: Specialty]
```

This example shows a Basketball roster with three distinct player categories. The Players list contains the
starting five (Point Guard, Shooting Guard, Small Forward, Power Forward, Center). The Substitutes list
includes bench players ready for rotation during the game. The Reserves list contains additional squad
members for emergency situations or special circumstances. Each list contains Player entities that can be
referenced and managed independently, providing clear organization of team composition and player availability
for different game situations and tournament requirements.

## See Also

- [Team](../team.md) - Core team entity that uses roster templates
- [Player](player/player.md) - Individual player entities within rosters
- [Position](player/position.md) - Player position templates for field assignments
- [Base Entity](../../foundation/base_entity.md) - Standard template entity attributes
