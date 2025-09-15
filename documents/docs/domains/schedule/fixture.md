---
tags:
  - fixture
  - template-entity
  - tournament-scheduling
  - competition-coordination
---

# Fixture (Template Entity)

## Overview

A Fixture Entity represents a specific scheduled competition instance (a game, match, heat, etc.) within a  
tournament. It acts as the central point connecting the scheduled competition time and location with operational  
details and links to the specific competition data (like a Match).

As an Entity, it possesses a unique identity and lifecycle, managed according to the [Base Entity](../foundation/base_entity.md).

## Structure

This template entity includes standard attributes from the [Base Entity](../foundation/base_entity.md)  
and adds the following fixture-specific attributes:

| Attribute | Description | Type | Required | Notes / Example |
|-----------|-------------|------|----------|-----------------|
| **Match** | Reference to the specific Match entity that this fixture schedules | UUID | Yes | `match-uuid-123` |
| **Timeslot** | The scheduled time for this fixture, embedded as a Value Object | Timeslot | Yes | Start: 14:00, End: 15:30, Duration: 90 minutes |
| **Venue** | Reference to the Venue where this fixture takes place | UUID | Yes | `venue-uuid-main-stadium` |
| **Area** | Reference to the specific Area within the venue where this fixture occurs | UUID | Yes | `area-uuid-court-1` |
| **Status** | Current status of the fixture | String | Yes | `"Scheduled"`, `"In Progress"`, `"Completed"`, `"Cancelled"` |
| **Notes** | Additional operational notes about this specific fixture | Text | Optional | `"Delayed due to weather"`, `"Special equipment required"` |

## Relationships

- A Fixture Entity is contained within a Schedule entity
- A Fixture Entity references one Match entity
- A Fixture Entity is scheduled at one Venue and Area
- A Fixture Entity may have multiple Official entities assigned

### Parent Relationships

- **Schedule** - The schedule containing this fixture

### Child Relationships

- **Match** - The match being scheduled
- **Officials** - Officials assigned to this fixture

### Related Entities

- **Venue** - Where the fixture takes place
- **Area** - Specific area within the venue
- **Timeslot** - When the fixture occurs

## Considerations

- **Scheduling:** Fixtures are the primary unit for tournament scheduling and time management
- **Status Tracking:** Fixture status should be updated as the tournament progresses
- **Venue Allocation:** Each fixture must be assigned to a specific venue and area
- **Official Assignment:** Officials should be assigned to fixtures based on availability and qualifications

## See Also

- [Schedule](./schedule.md) - Tournament scheduling container and coordination
- [Match](./match.md) - Competitive encounters between teams or participants
- [Timeslot](./timeslot.md) - Specific time intervals for scheduling
- [Official](./official/official.md) - Tournament officials and their assignments
- [Base Entity](../foundation/base_entity.md) - Common entity structure and lifecycle
