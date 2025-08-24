# **Map** (Data Model - Template Entity)

## **Introduction**

A **Map** Entity Template represents a visual representation or layout of physical spaces like , . It provides spatial
context and navigation information for users.

This Entity Template inherits properties from the .

It inherits properties from the [Base Entity](../foundation/base_entity.md).

---

## **Attributes**

**Note:** This Entity Template includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined
in the .

| Attribute       | Description                                                       | Type         | Required | Notes / Example                                 |
| --------------- | ----------------------------------------------------------------- | ------------ | -------- | ----------------------------------------------- |
| **Name**        | A descriptive name for the map.                                   | String       | Yes      | `"Main Building - Floor 1"`, `"Field Layout A"` |
| **Description** | Optional longer description providing more context about the map. | String       | No       | `"Map showing vendor booths and restrooms"`     |
| **Floor Level** | Indicates the floor or level this map represents.                 | String / Int | No       | `"Ground"`, `"Level 2"`, `0`, `1`               |
| **Image**       | Reference to the map image stored in the database.                | UUID         | Yes      | `550e8400-e29b-41d4-a716-446655440000`          |
| **Version**     | A version identifier if the map layout changes over time.         | String       | No       | `"1.1"`, `"2024-Final"`                         |

---

## **Relationships**

- A `Map` Entity can be associated with:

  - One \*\*\*\* entity for overall layouts
  - One **[Zone](../venue/zone.md)** entity for zone-specific layouts
  - One \*\*\*\* entity for area-specific layouts

- It may reference \*\*\*\* entities for the actual map images or files.
- When instantiated, a Map may be associated with:

  - Multiple \*\*\*\* entities for points of interest
  - Multiple \*\*\*\* entities for placed items

---

## **Considerations**

- **Template Usage:** Defines the standard structure for venue maps
- **Copy Mechanism:** When instantiated, creates a new map with its own identity
- **Instance Management:** Each map instance maintains its own lifecycle
- **Validation Rules:**

  - Name must be unique within its venue context
  - Image must be in a supported format
  - Version must follow a consistent format
  - Floor level must be valid for the venue

- **Usage Cases:**

  - Event layout planning
  - Participant navigation
  - Safety planning
  - Space optimization
  - Resource placement
  - Emergency response planning

---
