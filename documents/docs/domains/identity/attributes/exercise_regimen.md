---
tags:
- identity
- attributes
- exercise
- regimen
- template-entity
- fitness
---

# Exercise Regimen (Template Entity)

## Introduction

An **Exercise Regimen** Template Entity represents a standardized training program that can be selected and customized
by users. It provides a consistent way to handle training programs for fitness development, performance improvement,
and competition preparation within the tournament system.

As a Template Entity, it possesses a unique identity and lifecycle, managed according to the
[Base Entity](../../foundation/base_entity.md). When used, its definition is typically **copied** into the target
context (like a specific training program), allowing for potential minor modifications or annotations without altering the
original template.

It inherits properties from the [Base Entity](../../foundation/base_entity.md).

As a Template Entity, it possesses a unique identity and lifecycle, managed according to the
[Base Entity](../../foundation/base_entity.md), with additional template-specific attributes for versioning and reuse.

---

## **Attributes**

**Note:** This Template Entity includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`)
defined in the [Base Entity Model](../../foundation/base_entity.md).

| Attribute       | Description                                          | Type     | Required | Notes / Example                                                                          |
| --------------- | ---------------------------------------------------- | -------- | -------- | ---------------------------------------------------------------------------------------- |
| **ID**          | Unique identifier for the exercise regimen template entity. | UUID     | Yes      | `"er123e456-7890-1234-5678-901234567890"`                                               |
| **Name**        | The name of the exercise regimen.                    | String   | Yes      | `"Pre-Season Training"`, `"Competition Prep"`, `"Recovery Program"`                      |
| **Type**        | The type of regimen.                                 | String   | Optional | `"Strength"`, `"Cardio"`, `"Mixed"`, `"Recovery"`                                        |
| **Duration**    | The total duration of the regimen.                   | String   | Optional | `"8 weeks"`, `"12 weeks"`, `"6 months"`                                                  |
| **Frequency**   | How often the regimen should be performed.           | String   | Optional | `"Daily"`, `"3x per week"`, `"Alternating days"`                                         |
| **Exercises**   | List of exercises included in the regimen.           | List     | Optional | `["Sprint Training", "Agility Course", "Endurance Run"]`                                 |
| **Description** | Additional description or context about the regimen. | String   | Optional | `"Comprehensive training program for competitive athletes"`, `"Gentle recovery program"` |
| **Status**      | The status of the exercise regimen template.         | String   | Optional | `"Active"`, `"Inactive"`, `"Deprecated"`                                                 |
| **Created At**  | Timestamp when the exercise regimen template was created. | DateTime | Yes      | `"2024-01-15T10:30:00Z"`                                                                |
| **Updated At**  | Timestamp when the exercise regimen template was last updated. | DateTime | Yes      | `"2024-01-20T14:45:00Z"`                                                              |

---

## **Relationships**

- **Template Relationships:**

- Exercise Regimen Templates can be grouped by Type for easier discovery
- Exercise Regimen Templates can be referenced by training program algorithms for planning
- Exercise Regimen Templates can be linked to [Exercise](exercise.md) entities for exercise selection

- **Instantiation Relationships:**

- When instantiated, Exercise Regimen Templates create Exercise Regimen instances embedded within

    [Training](training.md) entities

- When instantiated, Exercise Regimen Templates create Exercise Regimen instances embedded within

    [Animal Profile](../profile/animal.md) entities

- Multiple training programs may instantiate the same Exercise Regimen Template with different customizations
- Exercise Regimen Templates can be referenced by [Schedule](../../schedule/README.md) entities for planning

---

## **Considerations**

- **Template Nature:** This template defines a standard exercise regimen. Instance-specific variations or customizations

  belong on the copied instance within its specific context (e.g., a Training program's implementation).

- **Copy Mechanism:** The process of copying this template definition into a target context (like a Training program)

  needs to be handled by application logic.

- **Template Management:**

- Templates should be curated and maintained by system administrators
- New templates can be added based on fitness standards and training methodologies
- Templates should be reviewed periodically for effectiveness and safety

- **Progression:** Regimen templates should support progressive difficulty and adaptation.
- **Individualization:** Regimen templates should be adaptable to individual needs and capabilities.
- **Monitoring:** Regimen adherence and progress should be tracked.
- **Recovery:** Regimen templates should include appropriate recovery periods and considerations.
- **Customization Balance:**

- Templates provide structure while allowing personalization
- Customizations should not break the fundamental regimen structure
- System should support both template-based and fully custom regimens

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ACSM Books: Exercise Testing and Prescription](https://acsm.org/education-resources/books/)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Value Object patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event training and fitness

  standards

## See Also

- [Exercise](../../identity/attributes/exercise.md)
- [Animal Profile](../../identity/profile/base_profile.md)
- [Schedule](../../schedule/schedule.md)
- [Identity README](../../identity/README.md)
- [Team](../../team/team.md)
- [Business README](../../README.md)
