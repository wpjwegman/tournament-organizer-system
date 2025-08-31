---
tags:

  - profile
  - abstract-entity
  - identity
  - base

---

# Base Profile (Abstract Entity)

## Overview

The **Base Profile** Abstract Entity defines the core attributes and relationships shared by all profile types in the system (e.g., Human, Animal, Plant, Vehicle, Robot, etc.). It provides a unified foundation for representing any participant, resource, or asset within the Tournament Organizer, ensuring consistency and extensibility across all profile subtypes.

All specific profile entities (such as Human Profile, Animal Profile, etc.) inherit from this base model and add their domain-specific attributes.

It inherits properties from the [Base Entity](../../foundation/base_entity.md).

## Purpose

- Provide a unified foundation for all profile types in the system
- Ensure consistency and extensibility across profile subtypes  
- Enable polymorphic handling of different profile types
- Support shared attributes and relationships for all profiles

## Structure

This abstract entity includes standard attributes from the [Base Entity](../../foundation/base_entity.md).

| Attribute               | Description                             | Type       | Required | Notes / Example                          |
| ----------------------- | --------------------------------------- | ---------- | -------- | ---------------------------------------- |
| **ProfileType**         | Discriminator for the profile subtype   | String     | Yes      | `"Human"`, `"Animal"`, `"Vehicle"`, etc. |
| **Name**                | Display name for the profile            | String     | Yes      | `"John Smith"`, `"Rover"`, `"Team Bus"`  |
| **Contact Information** | Reference to Contact Information entity | UUID       | No       |                                          |
| **Image**               | Embedded or referenced image            | [Image]    | No       |                                          |
| **Relationships**       | List of relationship references         | List[UUID] | No       | Links to Relationship entities           |
| **Media**               | List of media asset references          | List[UUID] | No       | Links to Media Asset entities            |

## Example

```mermaid
graph TD
    BP[Base Profile]
    BP --> PT[ProfileType: Human]
    BP --> N[Name: John Smith]
    BP --> CI[Contact Information: UUID]
    BP --> IMG[Image: Optional]
    BP --> REL[Relationships: List[UUID]]
    BP --> MED[Media: List[UUID]]
    
    subgraph "Inherited Entities"
        HP[Human Profile]
        AP[Animal Profile]
        VP[Vehicle Profile]
        RP[Robot Profile]
    end
    
    BP -.-> HP
    BP -.-> AP
    BP -.-> VP
    BP -.-> RP
```

This example shows the base profile structure with all core attributes and demonstrates how specific profile types inherit from the base.

## Relationships

- All specific profile entities inherit from Base Profile.
- Relationships and media are managed consistently across all profile types.
- Contact Information is referenced for communication and notifications.

## Considerations

- **Extensibility:** New profile types can be added by inheriting from Base Profile and extending with domain-specific attributes.
- **Polymorphism:** APIs and UIs can treat all profiles generically using the `ProfileType` discriminator.
- **Consistency:** Shared attributes and relationships ensure uniform handling of all profiles.
- **Security:** Access control and audit logging should be applied at the base level for sensitive data.

## Inheritance Hierarchy

```text
Base Profile
 ├── Human Profile
 ├── Animal Profile
 ├── Plant Profile
 ├── Vehicle Profile
 ├── Robot Profile
 ├── Software Profile
 ├── Machine Profile
 ├── Digital Profile
 ├── Art Profile
 └── Computer Profile
```

## See Also

- [Human Profile](human.md)
- [Animal Profile](animal.md)
- [Contact Information](../contact_information.md)
- [Identity Domain](../README.md)
- [Registration](../../registration/registration.md)
- [Base Entity](../../foundation/base_entity.md)
