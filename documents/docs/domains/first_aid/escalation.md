# **Escalation** (Data Model - Template Entity)

## **Introduction**

An **Escalation** Entity Template defines conditions or situations that require professional medical intervention beyond
basic first aid. These criteria help first aid providers determine when to seek additional medical assistance and what
type of help is needed.

It inherits properties from the [Base Entity](../foundation/base_entity.md).

_(For a guide on using escalation criteria in first aid protocols, see the )._

---

## **Attributes**

**Note:** This Entity Template includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined
in the .

| Attribute        | Description                                             | Type   | Required | Notes / Example                                                      |
| ---------------- | ------------------------------------------------------- | ------ | -------- | -------------------------------------------------------------------- |
| **Title**        | Clear, concise description of the escalation condition. | String | Yes      | `"Unconsciousness"`, `"Severe Bleeding"`, `"Difficulty Breathing"`   |
| **Priority**     | Level of urgency for medical response.                  | String | Yes      | `"Immediate"`, `"Urgent"`, `"Non-urgent"`                            |
| **Condition**    | Detailed description of when this escalation applies.   | Text   | Yes      | `"Person becomes unresponsive or shows signs of severe head injury"` |
| **Contact Type** | Type of medical assistance required.                    | String | Yes      | `"Emergency Services"`, `"Medical Staff"`, `"Hospital"`              |
| **Instructions** | Specific actions to take when escalating.               | Text   | Yes      | `"Call 911, stay with the person, prepare to provide CPR if needed"` |
| **Notes**        | Additional context or important considerations.         | Text   | No       | `"Have emergency contact information readily available"`             |

---

## **Relationships**

- An `Escalation` Template can be referenced by:

  - 🚨 **BROKEN:** 🚨 **BROKEN:** [Protocol](../safety/protocol/protocol.md) 🚨 🚨 entities
  - Emergency response protocols
  - Venue safety plans

- An `Escalation` may be related to:

  - Specific symptoms that trigger escalation
  - Required emergency contacts
  - Venue-specific protocols

---

## **Considerations**

- **Template Usage:** Serves as a reusable component for emergency protocols
- **Copy Mechanism:** When instantiated, creates a new escalation record with its own identity
- **Instance Management:** Each instance maintains its own lifecycle
- **Priority Levels:** Must be consistent across the system
- **Usage Cases:**

  - Emergency response protocols
  - Safety planning
  - Staff training
  - Venue requirements

---
