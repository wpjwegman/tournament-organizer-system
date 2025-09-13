---
tags:
- identity
- account
- scope
- template-entity
- configuration
---

# Scope (Template Entity)

## Introduction

A **Scope** Entity Template defines the context or domain where settings and configurations apply within the
Tournament Organizer system. It provides a standardized way to manage and organize settings across different contexts
such as tournaments, disciplines, teams, or global system settings.

As a Template Entity, it possesses a unique identity and lifecycle, managed according to the
[Base Entity](../../../foundation/base_entity.md). When used, its definition is typically **copied** into the target
context, allowing for potential modifications while maintaining the original template's structure.

It inherits properties from the [Base Entity](../../../foundation/base_entity.md).

---

## Attributes

**Note:** This Entity Template includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined
in the [Base Entity](../../../foundation/base_entity.md).

| Attribute       | Description                                                  | Type       | Required | Notes / Example                                                                                     |
| --------------- | ------------------------------------------------------------ | ---------- | -------- | --------------------------------------------------------------------------------------------------- |
| **Type**        | The type of scope this template represents.                  | String     | Yes      | `"Global"`, `"Tournament"`, `"Discipline"`, `"Team"`, `"Venue"`                                     |
| **Name**        | A descriptive name for the scope template.                   | String     | Yes      | `"Tournament Settings"`, `"Team Communication"`, `"Discipline Rules"`                               |
| **Description** | Detailed explanation of what this scope template represents. | Text       | Yes      | `"Settings that apply to all tournaments"`, `"Team-specific communication preferences"`             |
| **Contexts**    | List of specific contexts where this scope applies.          | List[UUID] | No       | Required for non-global scopes. Example: `["tour-1234-5678-90ab-cdef", "tour-5678-90ab-cdef-1234"]` |

---

## Relationships

- A `Scope` Template can be referenced by:

- [Setting](setting.md) entities for defining where settings apply

- Account configurations for user-specific settings
- System configurations for global settings

- A `Scope` may be related to:

- Specific tournaments (via Contexts)
- Specific disciplines (via Contexts)
- Specific teams (via Contexts)
- Specific venues (via Contexts)

---

## Considerations

- **Template Usage:** Serves as a reusable component for defining setting contexts across the system
- **Copy Mechanism:** When instantiated, creates a new scope record with its own identity and context
- **Instance Management:** Each instance maintains its own lifecycle and can be modified independently
- **Scope Types:** Must be consistent across the system to ensure proper setting inheritance
- **Context Management:**

- Global scopes (Type: "Global") do not require Contexts
- Non-global scopes must specify at least one Context
- Contexts must be valid UUIDs of the appropriate entity type

- **Usage Cases:**

- Tournament-wide settings
- Team-specific configurations
- Discipline-specific rules
- Global system settings
- Venue-specific settings

---
