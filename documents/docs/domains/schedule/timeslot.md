# **Timeslot** (Data Model - Value Object)

## **Introduction**

A **Timeslot** Value Object represents a specific interval of time, defined by a start and end time.

It describes characteristics of a time period and is typically embedded within other entities (like or ) to specify when
activities occur.

It inherits properties from the [Base Entity](../foundation/base_entity.md).

---

## **Attributes**

| Attribute      | Description                                 | Type     | Required | Notes / Example                                  |
| -------------- | ------------------------------------------- | -------- | -------- | ------------------------------------------------ |
| **Start Time** | The beginning of the time interval.         | DateTime | Yes      | `2024-11-02T14:00:00Z`                           |
| **End Time**   | The end of the time interval.               | DateTime | Yes      | `2024-11-02T15:30:00Z`                           |
| **Duration**   | The length of the time interval in minutes. | Integer  | Yes      | `90` (minutes)                                   |
| **Time Zone**  | The time zone for the start and end times.  | String   | Yes      | `"UTC"`, `"America/New_York"`, `"Europe/London"` |

---

## **Relationships**

- A `Timeslot` Value Object is embedded within entities to specify match timing.
- A `Timeslot` Value Object is embedded within entities to specify event timing.
- A `Timeslot` Value Object may be referenced by entities for overall planning.

---

## **Considerations**

- **Time Zone Handling:** All times should be stored in a consistent time zone (typically UTC) and converted for

  display.

- **Duration Calculation:** Duration is calculated as the difference between start and end times.
- **Validation:** End time must be after start time.
- **Overlap Detection:** Timeslots should not overlap within the same context (e.g., same venue, same team).

---
