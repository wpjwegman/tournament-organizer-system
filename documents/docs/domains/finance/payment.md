---
tags:
  - finance
  - payment
  - transaction
  - outflow
  - disbursement
---

# Payment (Entity Template)

## Introduction

A **Payment** represents a financial outflow from the organization. Payments are created when the organization pays
money to a profile (such as a participant for a refund or prize), a vendor, or another external party. Payments are
linked to the relevant expense or payout source, such as a refund, prize, or vendor invoice.

## Attributes

| Attribute    | Description                                                                     | Type   | Example                       |
| ------------ | ------------------------------------------------------------------------------- | ------ | ----------------------------- |
| ID           | Unique identifier for the payment                                               | String | PAY-2024-001                  |
| Payee        | The ID of the party receiving the payment (profile, vendor, organization, etc.) | ID     | "PROFILE-123", "VENDOR-456"   |
| Related Item | Reference to the related item (e.g., expense, registration, invoice)            | Link   | "EXP-2024-001"                |
| Amount       | Amount paid                                                                     | Amount | $100                          |
| Method       | Payment method (cash, bank transfer, etc.)                                      | Enum   | "Bank Transfer"               |
| Date         | Date the payment was made                                                       | Date   | "2024-06-05"                  |
| Notes        | Additional information                                                          | Text   | "Prize for tournament winner" |

## Relationships

- Linked to the payee (profile, vendor, organization, etc.)
- Linked to the relevant expense or payout source (refund, prize, vendor, etc.) via Related Item

**Note:** The tournament is always the source for payments. Only the payee (profile, vendor, organization, etc.) is
stored explicitly. This ensures clear traceability and aligns with best practices.

## Considerations

- Payments are for data storage only; reporting and analysis are handled elsewhere.
- Each payment should be traceable to its origin (recipient and expense/payout source).

## References

- [ISO 4217 — Currency codes (Wikipedia overview)](https://en.wikipedia.org/wiki/ISO_4217) - Standard for currency representation
- [ISO 8601:2019 - Date and time format](https://www.iso.org/standard/70907.html) - Standard for date and timestamp

  representations

- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Entity Template pattern reference

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event payment processing

  and financial standards

## See Also

- [Amount](../finance/amount.md)
- [Expense](../finance/expense.md)
- [Income](../finance/income.md)
- [Cart](../finance/cart.md)
- [Account](../identity/account/account.md)
- [Finance README](../finance/README.md)
