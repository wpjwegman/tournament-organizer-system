# **Instruction** (Data Model - Template Entity)

## **Introduction**

An **Instruction** Entity Template defines a standardized, actionable instruction that forms part of a first aid
procedure. Each instruction represents a specific action to be taken in sequence to address a medical situation or
injury.

It inherits properties from the [Base Entity](../foundation/base_entity.md).

_(For a guide on using instructions in first aid protocols, see the )._

---

## **Attributes**

**Note:** This Entity Template includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined
in the .

| Attribute     | Description                                                 | Type    | Required | Notes / Example                                                                  |
| ------------- | ----------------------------------------------------------- | ------- | -------- | -------------------------------------------------------------------------------- |
| **Title**     | Clear, concise description of the action to take.           | String  | Yes      | `"Check Responsiveness"`, `"Apply Direct Pressure"`, `"Call Emergency Services"` |
| **Order**     | Sequence number in the procedure.                           | Integer | Yes      | `1`, `2`, `3`                                                                    |
| **Action**    | Detailed description of how to perform this instruction.    | Text    | Yes      | `"Place two fingers on the person's wrist to check for pulse"`                   |
| **Duration**  | Expected time to complete this instruction (if applicable). | String  | No       | `"30 seconds"`, `"Until bleeding stops"`, `"Until help arrives"`                 |
| **Equipment** | Required items to perform this instruction (if any).        | List    | No       | `["Gloves", "Bandage", "First Aid Kit"]`                                         |
| **Notes**     | Additional context, warnings, or important considerations.  | Text    | No       | `"Do not move the person if spinal injury is suspected"`                         |

---

## **Relationships**

- An `Instruction` Template can be referenced by:

  - 🚨 **BROKEN:** 🚨 **BROKEN:** [Protocol](../safety/protocol/protocol.md) 🚨 🚨 entities
  - Training materials
  - Emergency response protocols

- An `Instruction` may be related to:

  - Required equipment or supplies
  - Prerequisite instructions
  - Following instructions
  - Relevant escalation criteria

---

## **Considerations**

- **Template Usage:** Serves as a reusable component for first aid procedures
- **Copy Mechanism:** When instantiated, creates a new instruction record with its own identity
- **Instance Management:** Each instance maintains its own lifecycle
- **Instruction Ordering:** Must maintain consistent sequencing within a procedure
- **Usage Cases:**

  - Sequential first aid procedures
  - Training and education
  - Emergency response protocols
  - Safety planning

---
