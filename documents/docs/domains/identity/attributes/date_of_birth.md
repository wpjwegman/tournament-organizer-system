# **Date of Birth** (Data Model - Value Object)

## **Introduction**

A **Date of Birth** Value Object represents an individual's birth date in a standardized format. It provides a
consistent way to handle birth date information for age calculations, eligibility verification, and administrative
purposes within the tournament system.

It describes temporal characteristics and is typically embedded within other entities (like or ) to specify birth
details.

It inherits properties from the [Base Entity](../../foundation/base_entity.md).

---

## **Attributes**

| Attribute | Description                            | Type    | Required | Notes / Example                |
| --------- | -------------------------------------- | ------- | -------- | ------------------------------ |
| **Date**  | The birth date in ISO 8601 format.     | Date    | Yes      | `"1990-05-15"`, `"2005-12-03"` |
| **Year**  | The birth year.                        | Integer | Optional | `1990`, `2005`                 |
| **Month** | The birth month (1-12).                | Integer | Optional | `5`, `12`                      |
| **Day**   | The birth day (1-31).                  | Integer | Optional | `15`, `3`                      |
| **Age**   | Calculated age as of a reference date. | Integer | Optional | `33`, `18`                     |

---

## **Relationships**

- A `Date of Birth` Value Object is embedded within entities.
- A `Date of Birth` Value Object is embedded within entities.
- A `Date of Birth` Value Object may be referenced by [Registration](../../registration/registration.md)

  entities for age verification.

---

## **Considerations**

- **Privacy:** Birth date information should be handled according to privacy regulations.
- **Age Calculation:** Age should be calculated dynamically based on current date.
- **Validation:** Birth dates should be validated for reasonable ranges.
- **Format:** Use ISO 8601 format for consistent date handling.

---
