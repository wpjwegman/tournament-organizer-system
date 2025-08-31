# **Incident** (Data Model - Template Entity)

## **Introduction**

An **Incident** Entity represents a record of any safety-related incident, accident, or near-miss that occurs during
tournament activities. It serves as a crucial tool for incident tracking, analysis, and prevention.

As an Entity, it possesses a unique identity and lifecycle, managed according to the [Base Entity](../foundation/base_entity.md).

It inherits properties from the [Base Entity](../foundation/base_entity.md).

---

## **Attributes**

**Note:** This Entity includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined in the [Base Entity](../foundation/base_entity.md).

| Attribute       | Description                                          | Type             | Required | Notes / Example                                              |
| --------------- | ---------------------------------------------------- | ---------------- | -------- | ------------------------------------------------------------ |
| **Type**        | The type of incident that occurred.                  | String           | Yes      | `"Injury"`, `"Equipment Failure"`, `"Weather"`, `"Security"` |
| **Severity**    | The severity level of the incident.                  | String           | Yes      | `"Minor"`, `"Moderate"`, `"Major"`, `"Critical"`             |
| **Description** | Detailed description of what happened.               | Text             | Yes      | `"Player fell during warm-up, minor ankle sprain"`           |
| **Location**    | Where the incident occurred.                         | String           | Yes      | `"Court 1"`, `"Main Arena"`, `"Parking Lot"`                 |
| **Timestamp**   | When the incident occurred.                          | DateTime         | Yes      | `2024-11-02T14:30:15Z`                                       |
| **Involved**    | List of people or entities involved in the incident. | List or entities | | |
| **Actions**     | Actions taken in response to the incident.           | Text             | Optional | `"First aid administered, player removed from play"`         |
| **Follow-up**   | Follow-up actions required.                          | Text             | Optional | `"Review safety protocols for warm-up area"`                 |

---

## **Relationships**

- An `Incident` Entity may be associated with a entity.
- An `Incident` Entity may be associated with a entity.
- An `Incident` Entity may involve multiple or entities.

### Parent Relationships

- - The tournament where this incident occurred
- - The venue where this incident occurred

### Child Relationships

- None

### Related Entities

- - Players involved in the incident
- - Staff involved in the incident

---

## **Considerations**

- **Incident Reporting:** All incidents should be reported promptly and accurately.
- **Severity Assessment:** Incident severity should be assessed consistently using standardized criteria.
- **Follow-up Actions:** All incidents should have appropriate follow-up actions identified and tracked.
- **Prevention:** Incident data should be analyzed to identify patterns and prevent future occurrences.

---
