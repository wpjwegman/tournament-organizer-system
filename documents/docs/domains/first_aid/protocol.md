# **Protocol** (Data Model - Template Entity)

## **Introduction**

A **Protocol** Entity Template defines a complete set of standardized procedures for responding to specific medical
situations or injuries that may occur during tournaments. It serves as a reusable blueprint for creating consistent
first aid protocols, combining symptoms, instructions, and escalation criteria into a comprehensive response plan.

It inherits properties from the [Base Entity](../foundation/base_entity.md).

_(For a guide on using first aid protocols, see the )._

---

## **Attributes**

**Note:** This Entity Template includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined
in the .

| Attribute        | Description                                             | Type              | Required | Notes / Example                                                              |
| ---------------- | ------------------------------------------------------- | ----------------- | -------- | ---------------------------------------------------------------------------- |
| **Title**        | Clear, concise title identifying the medical situation. | String            | Yes      | `"Choking (Adult)"`, `"Minor Cut"`, `"Heat Exhaustion"`                      |
| **Category**     | Classification of the medical situation.                | String            | Yes      | `"Trauma"`, `"Medical"`, `"Environmental"`                                   |
| **Symptoms**     | List of observable indicators for this situation.       | List[Symptom]     | Yes      | References [Symptom](../first_aid/symptom.md) entities         |
| **Instructions** | Ordered sequence of actions to take.                    | List[Instruction] | Yes      | References [Instruction](../first_aid/instruction.md) entities |
| **Escalation**   | Conditions requiring professional medical help.         | List[Escalation]  | Yes      | References [Escalation](../first_aid/escalation.md) entities   |
| **Media**        | References to relevant instructional media.             | List[Media]       | No       | References [Media](../media/media_asset.md) entities           |
| **Version**      | Version identifier for tracking updates.                | String            | Yes      | `"1.2"`                                                                      |
| **Notes**        | Additional context or important considerations.         | Text              | No       | `"Common in contact sports"`, `"Requires specific training"`                 |

---

## **Relationships**

- A `Protocol` Template can be referenced by:

  - [Tournament](../tournament/tournament.md) entities
  - [Venue](../venue/venue.md) entities
  - Training programs

- A `Protocol` Template contains:

  - Multiple [Symptom](../first_aid/symptom.md) entities
  - Multiple [Instruction](../first_aid/instruction.md) entities
  - Multiple [Escalation](../first_aid/escalation.md) entities
  - Optional references to [Media](../media/media_asset.md) entities

---

## **Considerations**

- **Template Usage:** Serves as a base for creating specific first aid protocols
- **Copy Mechanism:** When instantiated, creates a new protocol with its own identity
- **Instance Management:** Each instance maintains its own lifecycle
- **Version Control:** Tracks changes to protocols
- **Media Management:** References to media must be valid and accessible
- **Usage Cases:**

  - Emergency response protocols
  - Staff training
  - Venue safety requirements
  - Tournament safety planning
  - Medical situation management

---
