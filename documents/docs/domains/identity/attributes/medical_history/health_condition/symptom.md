# **Symptom** (Data Model - Template Entity)

## **Introduction**

A **Symptom** Entity Template defines a reusable blueprint for documenting and tracking health-related symptoms within
the tournament system. It serves as a standardized format for recording participant health conditions and their impact
on participation.

As an Entity Template, it ensures consistent symptom documentation across the system while maintaining flexibility for
different types of health conditions and their severity levels.

It inherits standard attributes from the .

It inherits properties from the [Base Entity](../../../../foundation/base_entity.md).

---

## **Attributes**

**Note:** This Entity Template includes the standard attributes (`ID`, `Status` [e.g., Active, Inactive], `CreatedAt`,
`LastUpdatedAt`, `Version`) defined in the [Base Entity](../../../../foundation/base_entity.md).

| Attribute             | Description                                                              | Type         | Required | Notes / Example                                   |
| --------------------- | ------------------------------------------------------------------------ | ------------ | -------- | ------------------------------------------------- |
| **Name**              | Clear and concise title for the Symptom.                                 | String       | Yes      | `"Fever"`, `"Muscle Strain"`, `"Headache"`        |
| **Description**       | Detailed explanation of the symptom and its characteristics.             | String       | Yes      | `"Elevated body temperature above normal range."` |
| **Severity Levels**   | List of possible severity levels for this symptom.                       | List[String] | Yes      | E.g., `[Mild, Moderate, Severe]`                  |
| **Impact Duration**   | Typical duration of impact on participation.                             | String       | Yes      | `"24-48 hours"`, `"1-2 weeks"`                    |
| **Required Actions**  | List of actions required when this symptom is reported.                  | List[String] | Yes      | `["Rest", "Medical Clearance Required"]`          |
| **Contagious**        | Whether this symptom indicates a contagious condition.                   | Boolean      | Yes      | `true`, `false`                                   |
| **Medical Clearance** | Whether medical clearance is required before returning to participation. | Boolean      | Yes      | `true`, `false`                                   |

---

## **Relationships**

- A `Symptom` template can be referenced by a <!-- TODO: Health Report not yet implemented -->

  health reporting system to document participant conditions.

- The specific implementation of a symptom within a health report will be linked to records.
- A symptom may be referenced by multiple <!-- TODO: Health Report not yet implemented -->

  health report instances.

---

## **Considerations**

- **Template Usage:** The template should be referenced rather than copied, as symptoms are standardized across the

  system.

- **Severity Assessment:** The Severity Levels help determine appropriate actions and restrictions.
- **Contagious Conditions:** Contagious symptoms may trigger additional protocols and participant isolation

  requirements.

- **Medical Clearance:** Symptoms requiring medical clearance must be properly documented and verified.
- **Impact Duration:** The Impact Duration helps in planning return-to-participation timelines.

---
