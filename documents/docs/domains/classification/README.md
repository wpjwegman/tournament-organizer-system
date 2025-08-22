# Classification Domain

tag: classification, domain, template, hierarchy, criterium

## Overview

The Classification domain provides a standardized, hierarchical, and flexible way to organize, categorize, and validate entities within the Tournament Organizer system. It supports consistent data management, rule-based eligibility, and extensible classification structures for tournaments, teams, venues, and more.

## Purpose

- Enable clear, consistent classification and eligibility across all business domains.
- Support hierarchical and template-based modeling for reuse and customization.
- Facilitate rule-based validation and dynamic updates for tournament management.

## Structure

The domain consists of template entities and value objects for classification and measurement:

| Entity/Value Object | Description |
|--------------------|-------------|
| [Category](category.md) | Organizes entities into hierarchical groups; supports subcategories and links to criteria. |
| [Criterium](criterium.md) | Defines requirements or standards for eligibility and classification; enables rule-based validation. |
| [Type](type.md) | Represents classification or categorization types; provides possible values and validation rules. |
| [Dimension](dimension.md) | Represents physical measurements (length, weight, capacity, etc.) for venues, equipment, and logistics. |
| [Measurement](measurement/measurement.md) | Value object for quantitative values. |
| [Unit](measurement/unit.md) | Defines measurement units and scales. |
| [System](measurement/system.md) | Describes systems of measurement. |

## See Also

- [Category](category.md)
- [Type](type.md)
- [Criterium](criterium.md)
- [Dimension](dimension.md)
- [Measurement](measurement/measurement.md)
- [Unit](measurement/unit.md)
- [System](measurement/system.md)
- [Team Domain](../team/README.md)
- [Tournament Domain](../tournament/README.md)
- [Foundation Domain](../foundation/README.md)
