---
tags:
  - timeslot
  - value-object
  - time-management
  - scheduling
---

# Timeslot (Value Object)

## Overview

A Timeslot Value Object represents a specific interval of time, defined by a start and end time.

It describes characteristics of a time period and is typically embedded within other entities (like Fixture or Event)  
to specify when activities occur.

## Structure

| Attribute | Description | Type | Required | Notes / Example |
|-----------|-------------|------|----------|-----------------|
| **Start Time** | The beginning of the time interval | DateTime | Yes | `2024-11-02T14:00:00Z` |
| **End Time** | The end of the time interval | DateTime | Yes | `2024-11-02T15:30:00Z` |
| **Duration** | The length of the time interval in minutes | Integer | Yes | `90` (minutes) |
| **Time Zone** | The time zone for the start and end times | String | Yes | `"UTC"`, `"America/New_York"`, `"Europe/London"` |

## Relationships

- A Timeslot Value Object is embedded within Fixture entities to specify match timing
- A Timeslot Value Object is embedded within Event entities to specify event timing  
- A Timeslot Value Object may be referenced by Schedule entities for overall planning

## Considerations

- **Time Zone Handling:** All times should be stored in a consistent time zone (typically UTC) and converted for display
- **Duration Calculation:** Duration is calculated as the difference between start and end times
- **Validation:** End time must be after start time
- **Overlap Detection:** Timeslots should not overlap within the same context (e.g., same venue, same team)

## See Also

- [Fixture](./fixture.md) - Scheduled competition instances using timeslots
- [Schedule](./schedule.md) - Tournament scheduling framework containing timeslots
- [Event](./event.md) - Specific occurrences within timeslot boundaries
- [Venue](../venue/venue.md) - Physical locations with timing constraints
