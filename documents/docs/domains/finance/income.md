---
tags:
  - finance
  - income
  - revenue
  - tracking
  - earnings
  - budget
---

# **Income** (Data Model - Template Entity)

## **Introduction**

An **Income** Entity represents a source of revenue or income for the tournament organization. It provides a consistent
way to handle income information for revenue tracking, financial reporting, and budget planning within the tournament
system.

It describes financial characteristics and is typically managed by [Finance](../finance/finance.md)
entities to provide complete revenue oversight.

It inherits properties from the [Base Entity](../foundation/base_entity.md).

As a Template Entity, it possesses a unique identity and lifecycle, managed according to the [Base Entity](../foundation/base_entity.md), with additional template-specific attributes for versioning and reuse.

---

## **Attributes**

| Attribute       | Description                                        | Type     | Required | Notes / Example                                          |
| --------------- | -------------------------------------------------- | -------- | -------- | -------------------------------------------------------- |
| **ID**          | Unique identifier for the income entity.           | UUID     | Yes      | `"i123e456-7890-1234-5678-901234567890"`                 |
| **Source**      | The source of the income.                          | String   | Yes      | `"Registration Fees"`, `"Sponsorship"`, `"Ticket Sales"` |
| **Amount**      | The amount of income received.                     | Decimal  | Yes      | `1500.00`, `2500.50`, `750.25`                           |
| **Currency**    | The currency of the income.                        | String   | Optional | `"USD"`, `"EUR"`, `"CAD"`                                |
| **Date**        | The date when the income was received.             | Date     | Yes      | `"2024-01-15"`, `"2024-02-20"`                           |
| **Category**    | The category of income.                            | String   | Optional | `"Registration"`, `"Sponsorship"`, `"Merchandise"`       |
| **Description** | Additional description of the income source.       | String   | Optional | `"Team registration fees for Spring Tournament"`         |
| **Status**      | The status of the income transaction.              | String   | Optional | `"Received"`, `"Pending"`, `"Refunded"`                  |
| **Created At**  | Timestamp when the income entity was created.      | DateTime | Yes      | `"2024-01-15T10:30:00Z"`                                 |
| **Updated At**  | Timestamp when the income entity was last updated. | DateTime | Yes      | `"2024-01-20T14:45:00Z"`                                 |

---

## **Relationships**

- An `Income` Entity is managed by a [Finance](../finance/finance.md) entity.
- An `Income` Template Entity may be associated with [Registration](../registration/registration.md) entities for

  registration fees.

- An `Income` Template Entity may be associated with entities for tournament revenue.

---

## **Considerations**

- **Accuracy:** Income amounts must be accurate and verifiable.
- **Categorization:** Income should be properly categorized for reporting purposes.
- **Timing:** Income should be recorded when actually received.
- **Documentation:** Income transactions should be properly documented.
- **Reconciliation:** Income should be reconciled with bank statements regularly.

---
