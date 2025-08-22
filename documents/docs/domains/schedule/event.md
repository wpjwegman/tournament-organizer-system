# **Match Event** (Data Model - Template Entity)

## **Introduction**

A **Match Event** Entity records a specific occurrence during a , such as penalties, warnings, timeouts, or other
significant moments that need to be tracked for the match record.

As an Entity, it inherits from the \*\*\*\* and maintains its own identity and lifecycle.

It inherits properties from the [Base Entity](../foundation/base_entity.md).

As a Template Entity, it possesses a unique identity and lifecycle, managed according to the [Base Entity](../foundation/base_entity.md), with additional template-specific attributes for versioning and reuse.

---

## **Attributes**

**Note:** This Template Entity includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined in the [Base Entity](../foundation/base_entity.md).

| Attribute       | Description                                             | Type     | Required | Notes / Example                                           |
| --------------- | ------------------------------------------------------- | -------- | -------- | --------------------------------------------------------- |
| **Match**       | Reference to the where this event occurred.             | UUID     | Yes      | `match-uuid-123`                                          |
| **Type**        | The type of event that occurred.                        | String   | Yes      | `"Penalty"`, `"Warning"`, `"Timeout"`, `"Goal"`, `"Foul"` |
| **Timestamp**   | When the event occurred during the match.               | DateTime | Yes      | `2024-11-02T14:30:15Z`                                    |
| **Player**      | Reference to the involved in the event (if applicable). | UUID     | Optional | `player-uuid-456`                                         |
| **Team**        | Reference to the involved in the event (if applicable). | UUID     | Optional | `team-uuid-789`                                           |
| **Description** | Additional details about the event.                     | Text     | Optional | `"Yellow card for unsportsmanlike conduct"`               |
| **Severity**    | The severity level of the event (if applicable).        | String   | Optional | `"Minor"`, `"Major"`, `"Critical"`                        |

---

## **Relationships**

- A `Match Event` Entity belongs to one entity.
- A `Match Event` Entity may involve one entity.
- A `Match Event` Entity may involve one entity.

### Parent Relationships

- - The match where this event occurred

### Child Relationships

- None

### Related Entities

- - Player involved in the event
- - Team involved in the event

---

## **Considerations**

- **Event Tracking:** Match events provide a detailed record of significant occurrences during a match.
- **Timing:** Events should be recorded with precise timestamps for accurate match history.
- **Classification:** Event types should be standardized for consistent reporting and analysis.
- **Severity:** Severity levels help prioritize events for review and action.

---
