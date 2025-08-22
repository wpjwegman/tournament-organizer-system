# **Expense** (Data Model - Template Entity)

## **Introduction**

An **Expense** Entity represents a cost or expenditure incurred by the tournament organization. It provides a consistent
way to handle expense information for cost tracking, budget management, and financial reporting within the tournament
system.

It describes financial characteristics and is typically managed by [Finance](../finance/finance.md)
entities to provide complete cost oversight.

It inherits properties from the [Base Entity](../foundation/base_entity.md).

As a Template Entity, it possesses a unique identity and lifecycle, managed according to the [Base Entity](../foundation/base_entity.md), with additional template-specific attributes for versioning and reuse.

---

## **Attributes**

| Attribute          | Description                                         | Type     | Required | Notes / Example                                 |
| ------------------ | --------------------------------------------------- | -------- | -------- | ----------------------------------------------- |
| **ID**             | Unique identifier for the expense entity.           | UUID     | Yes      | `"e123e456-7890-1234-5678-901234567890"`        |
| **Category**       | The category of the expense.                        | String   | Yes      | `"Venue Rental"`, `"Equipment"`, `"Staffing"`   |
| **Description**    | Description of the expense.                         | String   | Yes      | `"Indoor facility rental for tournament"`       |
| **Amount**         | The amount of the expense.                          | Decimal  | Yes      | `500.00`, `1250.50`, `750.25`                   |
| **Currency**       | The currency of the expense.                        | String   | Optional | `"USD"`, `"EUR"`, `"CAD"`                       |
| **Date**           | The date when the expense was incurred.             | Date     | Yes      | `"2024-01-15"`, `"2024-02-20"`                  |
| **Vendor**         | The vendor or supplier for the expense.             | String   | Optional | `"ABC Venue Services"`, `"Equipment Supply Co"` |
| **Payment Method** | The method used to pay the expense.                 | String   | Optional | `"Credit Card"`, `"Bank Transfer"`, `"Cash"`    |
| **Status**         | The status of the expense payment.                  | String   | Optional | `"Paid"`, `"Pending"`, `"Approved"`             |
| **Receipt**        | Reference to receipt or invoice document.           | String   | Optional | `"receipt_2024_001.pdf"`, `"invoice_12345.pdf"` |
| **Created At**     | Timestamp when the expense entity was created.      | DateTime | Yes      | `"2024-01-15T10:30:00Z"`                        |
| **Updated At**     | Timestamp when the expense entity was last updated. | DateTime | Yes      | `"2024-01-20T14:45:00Z"`                        |

---

## **Relationships**

- An `Expense` Entity is managed by a [Finance](../finance/finance.md) entity.
- An `Expense` Template Entity may be associated with entities for tournament costs.
- An `Expense` Template Entity may be associated with entities for venue-related expenses.

---

## **Considerations**

- **Accuracy:** Expense amounts must be accurate and verifiable.
- **Categorization:** Expenses should be properly categorized for reporting purposes.
- **Documentation:** All expenses should be supported by receipts or invoices.
- **Approval:** Expenses should follow appropriate approval processes.
- **Budget Tracking:** Expenses should be tracked against budget allocations.

---
