---
tags:
  - qualification
  - value-object
  - certification
  - professional-credentials
---

# Qualification (Value Object)

## Overview

A Qualification Value Object represents a certification or qualification held by an official. It is embedded within  
an Official entity and does not have its own identity or lifecycle.

## Structure

| Attribute | Description | Type | Required | Notes / Example |
|-----------|-------------|------|----------|-----------------|
| **Type** | The category of qualification | String | Yes | E.g., `Referee`, `Umpire`, `Judge`, `Scorekeeper` |
| **Level** | The level or grade of the qualification | String | Yes | E.g., `National`, `Regional`, `Local`, `International` |
| **Issued Date** | The date when the qualification was issued | Date | Yes | `2020-05-15` |
| **Expiry Date** | The date when the qualification expires | Date | Yes | `2025-12-31` |
| **Issuing Body** | The organization or authority that issued the qualification | UUID | Yes | Reference to an Organization entity |
| **Notes** | Additional information about the qualification | Text | No | E.g., `"Specialized in youth competitions"`, `"Advanced certification"` |

## Relationships

- A Qualification Value Object is always embedded within an Official entity
- It does not have its own identity or lifecycle

## Considerations

- **Validation:** Ensure expiry dates are in the future when creating new qualifications
- **Renewal:** Track qualification status and handle renewal processes
- **Compliance:** Ensure qualifications meet tournament or event requirements

## See Also

- [Official](./official.md) - Tournament officials holding qualifications
- [Organization](../../organization/organization.md) - Bodies that issue qualifications
- [Tournament](../../tournament/tournament.md) - Competitions requiring qualified officials
- [Base Value Object](../../foundation/base_value_object.md) - Common value object principles
