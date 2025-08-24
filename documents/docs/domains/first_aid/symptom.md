# **Symptom** (Data Model - Template Entity)

## **Introduction**

A **Symptom** Entity Template defines a standardized way to describe observable indicators that help identify specific
medical situations or injuries. These symptoms serve as key recognition points for first aid providers and help in
determining the appropriate response protocol.

It inherits properties from the [Base Entity](../foundation/base_entity.md).

_(For a guide on using symptoms in first aid protocols, see the )._

---

## **Attributes**

**Note:** This Entity Template includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined
in the .

| Attribute       | Description                                            | Type   | Required | Notes / Example                                                           |
| --------------- | ------------------------------------------------------ | ------ | -------- | ------------------------------------------------------------------------- |
| **Title**       | Clear, concise description of the symptom.             | String | Yes      | `"Difficulty Breathing"`, `"Severe Bleeding"`, `"Loss of Consciousness"`  |
| **Category**    | Classification of the symptom type.                    | String | Yes      | `"Respiratory"`, `"Circulatory"`, `"Neurological"`, `"Trauma"`            |
| **Severity**    | Level of urgency associated with this symptom.         | String | Yes      | `"Critical"`, `"Serious"`, `"Moderate"`, `"Minor"`                        |
| **Description** | Detailed explanation of how to recognize this symptom. | Text   | Yes      | `"Person is gasping for air, unable to speak in complete sentences"`      |
| **Notes**       | Additional context or important considerations.        | Text   | No       | `"May be accompanied by chest pain"`, `"Common in high-intensity sports"` |

---

## **Relationships**

- A `Symptom` Template can be referenced by:

  - 🚨 **BROKEN:** 🚨 **BROKEN:** [Protocol](../safety/protocol/protocol.md) 🚨 🚨 entities
  - Training materials
  - Emergency response protocols

- A `Symptom` may be related to:

  - Other symptoms that commonly occur together
  - Specific instructions that address this symptom
  - Relevant escalation criteria

---

## **Considerations**

- **Template Usage:** Serves as a reusable component for symptom identification
- **Copy Mechanism:** When instantiated, creates a new symptom record with its own identity
- **Instance Management:** Each instance maintains its own lifecycle
- **Severity Levels:** Must be consistent across the system
- **Usage Cases:**

  - Medical situation identification
  - Training and education
  - Emergency response protocols
  - Safety planning

---
