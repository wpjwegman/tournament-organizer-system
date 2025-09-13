---
tags:
- identity
- account
- setting
- template-entity
- configuration
---

# Setting (Template Entity)

## Introduction

A **Setting** is a **Template Entity** that defines a configurable parameter or preference that can be applied to
various entities in the system. It provides a standardized way to manage and apply configuration values across
different contexts.

When this template is used (e.g., within a specific context), its definition is applied according to the Base Entity
framework.

It inherits properties from the [Base Entity](../../../foundation/base_entity.md).

As a Template Entity, it possesses a unique identity and lifecycle, managed according to the
[Base Entity](../../../foundation/base_entity.md), with additional template-specific attributes for versioning and
reuse.

---

## Attributes

**Note:** This Template Entity includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`)
defined in the [Base Entity](../../../foundation/base_entity.md).

| Attribute       | Description                                                                                                                                                                             | Type         | Required | Notes / Example                                                                                         |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------- | ------------------------------------------------------------------------------------------------------- |
| **Group**       | Logical grouping of the setting template (e.g., `Notifications`, `Privacy`, `UI`).                                                                                                      | String       | Yes      | Example: `Notifications`                                                                                |
| **Name**        | Machine-readable key for the setting template (e.g., `email_notifications`).                                                                                                          | String       | Yes      | Example: `email_notifications`                                                                         |
| **Description** | Optional: Human-readable description of the setting template's purpose.                                                                                                                 | String       | Optional | Example: `Enable email reminders before matches start.`                                                 |
| **Scope**       | Reference (by ID) to the [Scope](scope.md) entity that defines where this setting applies. | UUID         | No       | Example: `a1b2c3d4-e5f6-7890-1234-567890abc999`                                                         |
| **Values**      | Represents default value(s) in the template context, or the user's chosen value(s) when embedded in the Account document.                                                               | List[String] | Yes      | Example (Template Default): `["true"]`. Example (Instance): `["dark", "compact"]`. Stored as String(s). |

---

## Relationships

- A `Setting` (Template) can be associated with multiple entities through the `Apply To` attribute.
- It references a **[Setting Type](../../../foundation/base_entity.md)** that defines its behavior and validation rules.
- It references a **[Scope](scope.md)** entity that defines where this setting applies.

- This template is designed to be **copied** when used within a specific context.

---

## Considerations

- **Dual Purpose (Template & Instance):** This model structure defines both the setting _template_ (managed by admins)

  and serves as the structure for the _instance_ data embedded within an `Account` document.

- **Interpreting `Values`:** When viewing this structure as a template, `Values` holds the default value(s). When

  viewing it as an embedded instance within an `Account`, `Values` holds the user's specifically chosen setting
  value(s).

- **Value Storage & Embedding:** As noted above, user-specific settings using this structure are typically embedded

  within the `Account` document (e.g., MongoDB). The template's `ID` might still be referenced from the embedded
  instance for context or resetting.

- **Type Handling:** The `Values` are stored as strings. Application logic must handle interpretation, validation

  (potentially against a centrally defined option set), and potential type conversion (e.g., parsing "true"/"false" as
  boolean) based on the setting's `Name` or `Group`.

- **Lifecycle:** The template itself (the standalone entity) can be `Active` or `Deprecated` via the inherited `Status`.

  The lifecycle of the _applied_ setting instance is tied to the parent `Account`.

---
