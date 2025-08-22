# **Fixture** (Data Model - Template Entity)

## **Introduction**

A **Fixture** Entity represents a specific scheduled competition instance (a game, match, heat, etc.) within a
tournament . It acts as the central point connecting the scheduled competition time and location with operational
details and links to the specific competition data (like a ).

As an Entity, it possesses a unique identity and lifecycle, managed according to the [Base Entity](../foundation/base_entity.md).

It inherits properties from the [Base Entity](../foundation/base_entity.md).

---

## **Attributes**

**Note:** This Entity includes the standard attributes (`ID`, `Status` [e.g., Scheduled, In Progress, Completed],
`CreatedAt`, `LastUpdatedAt`) defined in the [Base Entity](../foundation/base_entity.md).

| Attribute    | Description                                                                         | Type     | Required | Notes / Example                                              |
| ------------ | ----------------------------------------------------------------------------------- | -------- | -------- | ------------------------------------------------------------ |
| **Match**    | Reference to the specific entity that this fixture schedules.                       | UUID     | Yes      | `match-uuid-123`                                             |
| **Timeslot** | The scheduled time for this fixture, embedded as a Value Object.                    | Timeslot | Yes      | Start: 14:00, End: 15:30, Duration: 90 minutes               |
| **Venue**    | Reference to the where this fixture takes place.                                    | UUID     | Yes      | `venue-uuid-main-stadium`                                    |
| **Area**     | Reference to the specific within the venue where this fixture occurs.               | UUID     | Yes      | `area-uuid-court-1`                                          |
| **Status**   | Current status of the fixture (e.g., Scheduled, In Progress, Completed, Cancelled). | String   | Yes      | `"Scheduled"`, `"In Progress"`, `"Completed"`, `"Cancelled"` |
| **Notes**    | Additional operational notes about this specific fixture.                           | Text     | Optional | `"Delayed due to weather"`, `"Special equipment required"`   |

---

## **Relationships**

- A `Fixture` Entity is contained within a entity.
- A `Fixture` Entity references one entity.
- A `Fixture` Entity is scheduled at one and .
- A `Fixture` Entity may have multiple entities assigned.

### Parent Relationships

- - The schedule containing this fixture

### Child Relationships

- - The match being scheduled
- - Officials assigned to this fixture

### Related Entities

- - Where the fixture takes place
- - Specific area within the venue
- - When the fixture occurs

---

## **Considerations**

- **Scheduling:** Fixtures are the primary unit for tournament scheduling and time management.
- **Status Tracking:** Fixture status should be updated as the tournament progresses.
- **Venue Allocation:** Each fixture must be assigned to a specific venue and area.
- **Official Assignment:** Officials should be assigned to fixtures based on availability and qualifications.

---
