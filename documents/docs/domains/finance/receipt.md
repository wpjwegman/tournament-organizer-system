---
tags:
  - finance
  - receipt
  - transaction
  - inflow
  - income
---

# Receipt (Entity Template)

## Introduction

A **Receipt** represents a financial inflow to the organization. Receipts are created when the organization receives
money from a profile (such as a participant), sponsor, ticket buyer, or other source. Receipts are linked to the
relevant income source, such as a fee, ticket sale, or sponsorship.

## Attributes

| Attribute    | Description                                                                   | Type   | Example                     |
| ------------ | ----------------------------------------------------------------------------- | ------ | --------------------------- |
| ID           | Unique identifier for the receipt                                             | String | REC-2024-001                |
| Payer        | The ID of the party making the payment (profile, sponsor, organization, etc.) | ID     | "PROFILE-123", "ORG-456"    |
| Related Item | Reference to the related item (e.g., fee, registration, ticket)               | Link   | "FEE-2024-001"              |
| Amount       | Amount received                                                               | Amount | $75                         |
| Method       | Payment method (cash, card, online, etc.)                                     | Enum   | "Online"                    |
| Date         | Date the receipt was created                                                  | Date   | "2024-06-01"                |
| Notes        | Additional information                                                        | Text   | "Paid at registration desk" |

## Relationships

- Linked to the payer (profile, sponsor, organization, etc.)
- Linked to the relevant income source (fee, ticket, sponsorship, etc.) via Related Item

**Note:** The tournament is always the recipient for receipts. Only the payer (profile, sponsor, organization, etc.) is
stored explicitly. This ensures clear traceability and aligns with best practices.

## Considerations

- Receipts are for data storage only; reporting and analysis are handled elsewhere.
- Each receipt should be traceable to its origin (profile and income source).

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
- [Income](../finance/income.md)
- [Payment](../finance/payment.md)
- [Fee](../finance/fee.md)
- [Account](../identity/account/account.md)
- [Finance README](../finance/README.md)
