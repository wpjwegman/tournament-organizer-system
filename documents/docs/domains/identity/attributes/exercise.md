# **Exercise** (Data Model - Template Entity)

## **Introduction**

An **Exercise** Template Entity represents a standardized exercise type that can be selected and customized
by users. It provides a consistent way to handle exercise information for training programs, fitness tracking, and
performance management within the tournament system.

As a Template Entity, it possesses a unique identity and lifecycle, managed according to the
[Base Entity](../../foundation/base_entity.md). When used, its definition is typically **copied** into the target
context (like a specific training program), allowing for potential minor modifications or annotations without altering the
original template.

It inherits properties from the [Base Entity](../../foundation/base_entity.md).

As a Template Entity, it possesses a unique identity and lifecycle, managed according to the [Base Entity](../../foundation/base_entity.md), with additional template-specific attributes for versioning and reuse.

---

## **Attributes**

**Note:** This Template Entity includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined in the [Base Entity Model](../../foundation/base_entity.md).

| Attribute       | Description                                           | Type     | Required | Notes / Example                                                                   |
| --------------- | ----------------------------------------------------- | -------- | -------- | --------------------------------------------------------------------------------- |
| **ID**          | Unique identifier for the exercise template entity.   | UUID     | Yes      | `"e123e456-7890-1234-5678-901234567890"`                                          |
| **Name**        | The name of the exercise.                             | String   | Yes      | `"Sprint Training"`, `"Agility Course"`, `"Endurance Run"`                        |
| **Category**    | The category of exercise.                             | String   | Optional | `"Cardio"`, `"Strength"`, `"Agility"`, `"Endurance"`                              |
| **Duration**    | The typical duration of the exercise.                 | String   | Optional | `"30 minutes"`, `"1 hour"`, `"45 minutes"`                                        |
| **Intensity**   | The intensity level of the exercise.                  | String   | Optional | `"Low"`, `"Medium"`, `"High"`                                                     |
| **Equipment**   | Equipment required for the exercise.                  | String   | Optional | `"None"`, `"Cones"`, `"Weights"`, `"Treadmill"`                                   |
| **Description** | Additional description or context about the exercise. | String   | Optional | `"High-intensity interval training for speed"`, `"Low-impact endurance building"` |
| **Status**      | The status of the exercise template.                  | String   | Optional | `"Active"`, `"Inactive"`, `"Deprecated"`                                          |
| **Created At**  | Timestamp when the exercise template was created.     | DateTime | Yes      | `"2024-01-15T10:30:00Z"`                                                          |
| **Updated At**  | Timestamp when the exercise template was last updated.| DateTime | Yes      | `"2024-01-20T14:45:00Z"`                                                          |

---

## **Relationships**

- **Template Relationships:**

- Exercise Templates can be grouped by Category for easier discovery
- Exercise Templates can be referenced by training program algorithms for planning
- Exercise Templates can be linked to [Category](../../classification/category.md) entities for organization

- **Instantiation Relationships:**

- When instantiated, Exercise Templates create Exercise instances embedded within

    [Training](training.md) entities

- When instantiated, Exercise Templates create Exercise instances embedded within

    [Exercise Regimen](exercise_regimen.md) entities

- Multiple training programs may instantiate the same Exercise Template with different customizations
- Exercise Templates can be referenced by [Schedule](../../schedule/README.md) entities for planning

---

## **Considerations**

- **Template Nature:** This template defines a standard exercise type. Instance-specific variations or customizations

  belong on the copied instance within its specific context (e.g., a Training program's implementation).

- **Copy Mechanism:** The process of copying this template definition into a target context (like a Training program)

  needs to be handled by application logic.

- **Template Management:**

- Templates should be curated and maintained by system administrators
- New templates can be added based on fitness standards and user needs
- Templates should be reviewed periodically for safety and effectiveness

- **Safety:** Exercise templates should include safety considerations and requirements.
- **Progression:** Exercise templates should support progressive difficulty levels.
- **Equipment:** Equipment requirements should be clearly specified in templates.
- **Monitoring:** Exercise performance should be tracked and monitored appropriately.
- **Customization Balance:**

- Templates provide structure while allowing personalization
- Customizations should not break the fundamental exercise classification
- System should support both template-based and fully custom exercises

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ACSM Books: Exercise Testing and Prescription](https://acsm.org/education-resources/books/)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Value Object patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event training and fitness

  standards

## See Also

- [Exercise Regimen](../../identity/attributes/exercise_regimen.md)
- [Schedule](../../schedule/schedule.md)
- [Identity README](../../identity/README.md)
- [Team](../../team/team.md)
- [Business README](../../README.md)
