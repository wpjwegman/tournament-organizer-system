---
tags:
- identity
- role
- responsibility
- expectation
- value-object
---

# Expectation (Value Object)

## Introduction

An **Expectation** is a Value Object that represents a standard of conduct, behavior, or outcome expected from a Role or
Responsibility. Expectations are referenced to clarify what is required or valued in a given context.

As a Value Object, it does not have identity or lifecycle - it is immutable and defined by its attributes.

---

## **Attributes**

| Attribute       | Description                             | Type   | Required | Example                         |
| --------------- | --------------------------------------- | ------ | -------- | ------------------------------- |
| **Name**        | Name of the expectation                 | String | Yes      | "Impartiality"                  |
| **Description** | Details about the expectation           | Text   | Yes      | "Treat all participants fairly" |
| **Category**    | Broad classification of the expectation | String | No       | "Behavioral", "Performance"     |

---

## **Relationships**

- Expectations are referenced by Responsibilities and Roles, but are not managed as standalone entities in this context.

---

## **Usage Guidelines**

- Use expectations to clarify standards for roles and responsibilities.
- Group expectations by category for training or evaluation.

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO 26000:2020 - Guidance on social responsibility](https://www.iso.org/standard/42546.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Value Object patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event conduct standards

## See Also

- [Responsibility](../../../identity/role/responsibility/responsibility.md)
- [Skill](../../../identity/role/responsibility/skill.md)
- [Role](../../../identity/role/role.md)
- [Identity README](../../../identity/README.md)
- [Business README](../../../README.md)

---
