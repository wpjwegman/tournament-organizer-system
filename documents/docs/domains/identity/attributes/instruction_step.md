---
tags:
- identity
- attributes
- instruction-step
- value-object
- procedure
---

# Instruction Step (Value Object)

## Introduction

An **Instruction Step** Value Object represents a single, distinct action or step within an ordered set of
[Instructions](../../first_aid/instruction.md). It follows the Value Object pattern, meaning it has no
independent identity and is always embedded within an Instruction entity.

This value object is used to define individual steps in a sequence of actions that make up a complete instruction set.

It inherits properties from the [Base Entity](../../foundation/base_entity.md).

---

## **Attributes**

| Attribute  | Description                                                                      | Type    | Required | Notes / Example                                           |
| ---------- | -------------------------------------------------------------------------------- | ------- | -------- | --------------------------------------------------------- |
| **Order**  | The sequential position of this step within the instruction set (e.g., 1, 2, 3). | Integer | Yes      | `1`, `2`                                                  |
| **Action** | The specific action to be performed for this step.                               | String  | Yes      | `"Check all fire extinguishers."`, `"Verify exit signs."` |

---

## **Relationships**

- This Value Object has no independent identity
- It is always embedded within an [Instruction](../../first_aid/instruction.md) entity
- The Order attribute determines its position within the parent Instruction's sequence

---

## **Considerations**

- **Embedding Context:** Always embedded within a parent Instruction entity, never stored independently
- **Immutability:** Once created, the values should not be modified; create a new instance instead
- **Validation Rules:**

- Order must be a positive integer
- Action text must not be empty
- Order must be unique within its parent Instruction

- **Usage Cases:**

- Step-by-step procedures
- Safety instructions
- Setup procedures
- Maintenance tasks
- Emergency protocols

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO 29993:2017 - Learning services outside formal education](https://www.iso.org/standard/64047.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Value Object patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event procedural standards

## See Also

- [Instruction](../../identity/attributes/instruction.md)
- [Instruction](../../first_aid/instruction.md)
- [Identity README](../../identity/README.md)
- [Safety](../../safety/safety.md)
- [Business README](../../README.md)

---
