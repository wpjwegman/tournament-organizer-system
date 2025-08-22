# **Base Entity Model** (Technical Foundation)

This document describes the technical foundation shared by all
**[Entities](../foundation/ddd_concepts.md#entity)** and
**[Template Entities](../foundation/ddd_concepts.md#template-entity)** within the
system. It defines the standard attributes and behaviors that every entity must implement, regardless of its domain
context or whether it's a template or instance.

Individual Entity and Entity Template model definitions will reference this base model for these common fields.

---

## **Standard Attributes**

| Attribute        | Description                                                                                                                                                                                                                        | Type         | Required | Notes / Example                                                                                                                                                                                  |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Unique ID**    | The unique, immutable identifier for this specific Entity instance or Template. Used for referencing this Entity from others.                                                                                                      | UUID         | Yes      | Primary Key. Standardized as UUID version 4. Example: `acc-a1b2c3d4-e5f6-7890-1234-567890abcdef` (Prefixes like `acc-` are convention, the core is UUID v4).                                     |
| **Template ID**  | Reference to the template this entity is based on. If this is a template, Template ID equals Unique ID. If this is an instance, Template ID references the template it was created from.                                           | UUID         | Yes      | For templates: Same as Unique ID. For instances: References parent template. Example: `tmpl-a1b2c3d4-e5f6-7890-1234-567890abcdef`                                                                |
| **Version**      | The version number of this entity or template. Follows semantic versioning (MAJOR.MINOR.PATCH). For instances, this indicates which version of the template they were created from. For templates, this tracks template evolution. | String       | Yes      | Example: `1.0.0` for initial version, `1.1.0` for minor updates, `2.0.0` for major changes.                                                                                                      |
| **Statuses**     | List of current statuses for this Entity instance or Template. Each status is a .                                                                                                                                                  | List[Status] | Yes      | At least one status must be present. Example: `[{"Type": "System", "Value": "Active", "Notes": "Initial activation."}, {"Type": "Entity", "Value": "Draft", "Notes": "Draft created by user."}]` |
| **Created At**   | Timestamp indicating when this specific Entity instance or Template was first persisted in the system.                                                                                                                             | DateTime     | Yes      | System-managed. ISO 8601 format (UTC). Example: `2024-03-10T15:00:00Z`                                                                                                                           |
| **Last Updated** | Timestamp indicating when this specific Entity instance or Template was last modified. Updated automatically on any change to mutable attributes (excluding potentially `Statuses`).                                               | DateTime     | Yes      | System-managed. ISO 8601 format (UTC). Example: `2024-07-15T11:30:00Z`                                                                                                                           |

---

## **Technical Considerations**

### ID and Template Management

- **Unique ID:**
  - Must be unique across all Entities and Templates
  - Immutable once assigned
  - Used for direct entity references
  - Format: UUIDv4 with optional domain prefix

- **Template ID:**
  - For templates: Matches Unique ID
  - For instances: References parent template
  - Enables template lineage tracking
  - Supports template evolution

- **Version Management:**
  - Follows semantic versioning (MAJOR.MINOR.PATCH)
  - MAJOR: Breaking changes
  - MINOR: Backward-compatible features
  - PATCH: Backward-compatible fixes
  - Instances track template version at creation
  - Templates increment version on changes

### Template-Instance Relationship

- **Template Creation:**
  - Unique ID and Template ID are identical
  - Initial version is 1.0.0
  - Can be modified to create new versions
  - Changes may affect future instances

- **Instance Creation:**
  - Gets new Unique ID
  - Template ID references parent template
  - Version matches template version at creation
  - Can evolve independently of template

- **Template Updates:**
  - Create new version of template
  - Existing instances remain at their creation version
  - New instances use latest template version
  - Option to upgrade instances to new version

### System Management

- **Timestamps:** `CreatedAt` and `LastUpdatedAt` are managed by the underlying data persistence layer and should not

  typically be set manually.

- **Status Management:**
  - Entities must have at least one status
  - Multiple statuses of different types can be active simultaneously
  - Status changes should be logged for audit purposes
  - Status transitions may trigger notifications
  - Some status changes may require specific permissions
  - Status history should be maintained for audit trails
  - See for allowed values by type

### Implementation Guidelines

1. **Data Persistence:**
   - All entities must be persisted with these base attributes
   - The persistence layer should enforce these requirements
   - Changes to base attributes should be tracked for audit purposes
   - Template changes should create new versions

2. **Validation Rules:**
   - Unique ID must be valid UUID v4
   - Template ID must be valid UUID v4
   - Version must follow semantic versioning
   - At least one status must be present
   - Timestamps must be valid ISO 8601 UTC format
   - Status values must be from allowed options
   - Template ID must match Unique ID for templates
   - Template ID must reference existing template for instances

3. **Performance Considerations:**
   - Unique ID should be indexed for efficient lookups
   - Template ID should be indexed for template queries
   - Version should be indexed for version-based queries
   - Status changes should be optimized for frequent updates
   - Timestamp updates should be handled efficiently
   - Template lookups should be optimized
   - Instance creation from templates should be efficient

---

## References

- [ISO/IEC 11179-1:2015 - Information technology — Metadata registries (MDR) — Part 1: Framework](https://www.iso.org/standard/35343.html)
- [ISO 8601:2019 - Date and time format](https://www.iso.org/standard/70907.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Entity and Value Object patterns

- [Martin Fowler: Patterns of Enterprise Application Architecture](https://martinfowler.com/books/eaa.html)

## See Also

- [Foundation README](../foundation/README.md)
- [Business README](../README.md)
- [Account](../identity/account/account.md)
- [Discipline](../discipline/discipline.md)
- [Finance](../finance/finance.md)
- [Team](../team/team.md)

---
