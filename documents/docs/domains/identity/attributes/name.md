# **Name** (Data Model - Value Object)

## **Introduction**

A **Name** Value Object represents a person's or entity's name in a structured format. It provides a standardized way to
handle different types of names (personal names, business names, etc.) with appropriate components and formatting.

It describes characteristics of a name and is typically embedded within other entities (like or ) to specify
identification details.

It inherits properties from the [Base Entity](../../foundation/base_entity.md).

---

## **Attributes**

| Attribute         | Description                                    | Type   | Required | Notes / Example                              |
| ----------------- | ---------------------------------------------- | ------ | -------- | -------------------------------------------- |
| **Type**          | The type of name (personal, business, etc.).   | String | Yes      | `"Personal"`, `"Business"`, `"Display"`      |
| **First Name**    | The first or given name (for personal names).  | String | Optional | `"John"`, `"Maria"`                          |
| **Last Name**     | The last name or surname (for personal names). | String | Optional | `"Smith"`, `"Garcia"`                        |
| **Middle Name**   | The middle name (for personal names).          | String | Optional | `"Robert"`, `"Elizabeth"`                    |
| **Business Name** | The business or organization name.             | String | Optional | `"Acme Corporation"`, `"Smith & Associates"` |
| **Display Name**  | A formatted display version of the name.       | String | Optional | `"John R. Smith"`, `"Dr. Maria Garcia"`      |
| **Nickname**      | A nickname or preferred name.                  | String | Optional | `"Johnny"`, `"Mari"`                         |

---

## **Relationships**

- A `Name` Value Object is embedded within entities.
- A `Name` Value Object is embedded within entities.
- A `Name` Value Object may be embedded within entities.

---

## **Considerations**

- **Name Types:** Different name types require different attributes to be populated.
- **Formatting:** Display names should be properly formatted for presentation.
- **Privacy:** Names should be handled according to privacy regulations.
- **Validation:** Names should be validated for appropriate format and length.

---
