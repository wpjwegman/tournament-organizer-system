---
tags:
- identity
- role
- responsibility
- skill
- value-object
---

# Skill (Value Object)

## Introduction

A **Skill** is a Value Object that represents a specific ability, competency, or area of expertise required to fulfill a
Responsibility or Role. Skills are referenced in Responsibilities to clarify requirements and support evaluation or
training.

As a Value Object, it does not have identity or lifecycle - it is immutable and defined by its attributes.

---

## **Attributes**

| Attribute             | Description                              | Type   | Required | Example                       |
| --------------------- | ---------------------------------------- | ------ | -------- | ----------------------------- |
| **Name**              | Name of the skill                        | String | Yes      | "Time management"             |
| **Description**       | Details about the skill                  | Text   | Yes      | "Ability to manage schedules" |
| **Category**          | Broad classification of the skill        | String | No       | "Soft Skill", "Technical"     |
| **Proficiency Level** | (Optional) Level of proficiency required | String | No       | "Beginner", "Advanced"        |

---

## **Relationships**

- Skills are referenced by Responsibilities and Roles, but are not managed as standalone entities in this context.
- Skills can be grouped by Category for reporting or training purposes.

---

## **Usage Guidelines**

- Use skills to clarify requirements for responsibilities and roles.
- Optionally specify proficiency level for more precise requirements.

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO 17024:2012 - Conformity assessment - General requirements for bodies operating certification of persons](https://www.iso.org/standard/29315.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Value Object patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event competency standards

## See Also

- [Responsibility](../../../identity/role/responsibility/responsibility.md)
- [Task](../../../identity/role/responsibility/task.md)
- [Role](../../../identity/role/role.md)
- [Identity README](../../../identity/README.md)
- [Business README](../../../README.md)

---
