---
tags:
- identity
- attributes
- instruction
- template-entity
- training
- competition
---

# Instruction (Template Entity)

## Introduction

An **Instruction** Template Entity represents a standardized instruction or command that can be selected and customized
by users. It provides a consistent way to handle instruction information for training, competition rules, and operational
procedures within the tournament system.

As a Template Entity, it possesses a unique identity and lifecycle, managed according to the
[Base Entity](../../foundation/base_entity.md). When used, its definition is typically **copied** into the target
context (like a specific training program), allowing for potential minor modifications or annotations without altering
the original template.

It inherits properties from the [Base Entity](../../foundation/base_entity.md).

As a Template Entity, it possesses a unique identity and lifecycle, managed according to the
[Base Entity](../../foundation/base_entity.md), with additional template-specific attributes for versioning and reuse.

---

## **Attributes**

**Note:** This Template Entity includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined
in the [Base Entity Model](../../foundation/base_entity.md).

| Attribute       | Description                                              | Type     | Required | Notes / Example                                             |
| --------------- | -------------------------------------------------------- | -------- | -------- | ----------------------------------------------------------- |
| **ID**          | Unique identifier for the instruction template entity.   | UUID     | Yes      | `"in123e456-7890-1234-5678-901234567890"`                   |
| **Command**     | The specific instruction or command.                     | String   | Yes      | `"Sit"`, `"Stay"`, `"Come"`, `"Heel"`                       |
| **Category**    | The category of instruction.                             | String   | Optional | `"Basic"`, `"Advanced"`, `"Competition"`, `"Safety"`        |
| **Method**      | The method or technique for the instruction.             | String   | Optional | `"Voice"`, `"Hand Signal"`, `"Whistle"`, `"Gesture"`        |
| **Difficulty**  | The difficulty level of the instruction.                 | String   | Optional | `"Beginner"`, `"Intermediate"`, `"Advanced"`                |
| **Description** | Additional description or context about the instruction. | String   | Optional | `"Basic obedience command"`, `"Advanced competition skill"` |
| **Status**      | The status of the instruction template.                  | String   | Optional | `"Active"`, `"Inactive"`, `"Deprecated"`                    |
| **Created At**  | Timestamp when the instruction template was created.     | DateTime | Yes      | `"2024-01-15T10:30:00Z"`                                    |
| **Updated At**  | Timestamp when the instruction template was last updated.| DateTime | Yes      | `"2024-01-20T14:45:00Z"`                                    |

---

## **Relationships**

- **Template Relationships:**

- Instruction Templates can be grouped by Category for easier discovery
- Instruction Templates can be referenced by training program algorithms for planning
- Instruction Templates can be linked to [Rule](../../discipline/activity/variation/rule.md) entities for rule definition

- **Instantiation Relationships:**

- When instantiated, Instruction Templates create Instruction instances embedded within

    [Training](../../process/README.md) entities

- When instantiated, Instruction Templates create Instruction instances embedded within

  [Rule](../../discipline/activity/variation/rule.md) entities

- Multiple training programs may instantiate the same Instruction Template with different customizations
- Instruction Templates can be referenced by [Competition](../../tournament/README.md) entities for rules

---

## **Considerations**

- **Template Nature:** This template defines a standard instruction. Instance-specific variations or customizations

  belong on the copied instance within its specific context (e.g., a Training program's implementation).

- **Copy Mechanism:** The process of copying this template definition into a target context (like a Training program)

  needs to be handled by application logic.

- **Template Management:**

- Templates should be curated and maintained by system administrators
- New templates can be added based on training standards and competition requirements
- Templates should be reviewed periodically for clarity and effectiveness

- **Clarity:** Instruction templates should be clear and unambiguous.
- **Consistency:** Instruction templates should be consistent across training and competition contexts.
- **Progression:** Instruction templates should support progressive difficulty levels.
- **Safety:** Instruction templates should include safety considerations where applicable.
- **Customization Balance:**

- Templates provide structure while allowing personalization
- Customizations should not break the fundamental instruction meaning
- System should support both template-based and fully custom instructions

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO 29993:2017 - Learning services outside formal education](https://www.iso.org/standard/64047.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Value Object patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event training and

  instruction standards

## See Also

- [Instruction Step](../../identity/attributes/instruction_step.md)
- [Rule](../../discipline/activity/variation/rule.md)
- [Identity README](../../identity/README.md)
- [Team](../../team/team.md)
- [Business README](../../README.md)
