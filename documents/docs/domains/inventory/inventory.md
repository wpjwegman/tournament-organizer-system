# **Inventory** (Data Model - Template Entity)

## **Introduction**

An **Inventory** Entity represents a collection of [Items](../inventory/item.md) and their
[Stock Records](stock_record.md) managed by a specific organization, tournament, venue, or fixture. It provides a way to
track, group, and manage items that are inherently coupled to their location or organizational context.

It inherits properties from the [Base Entity](../foundation/base_entity.md).

---

## **Attributes**

**Note:** This Entity includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined in the [Base Entity](../foundation/base_entity.md).

| Attribute       | Description                                                                | Type   | Required | Notes / Example                                  |
| --------------- | -------------------------------------------------------------------------- | ------ | -------- | ------------------------------------------------ |
| **Name**        | Unique identifier for the inventory.                                       | String | Yes      | `"Tournament X Supplies"`, `"Venue Y Equipment"` |
| **Description** | Detailed explanation of the inventory.                                     | Text   | Yes      | `"All equipment and supplies for Tournament X"`  |
| **Type**        | Classification of the inventory.                                           | String | Yes      | `Tournament`, `Venue`, `Fixture`, `Organization` |
| **Owner**       | Reference to the owning entity.                                            | UUID   | Yes      | `tournament-uuid-x`, `venue-uuid-y`              |
| **Items**       | List of references to [Item](../inventory/item.md) entities. | Array  | No       | `[item-uuid-1, item-uuid-2]`                     |

---

## **Relationships**

- May be owned by:

  - [Tournament](../tournament/tournament.md)
  - [Fixture](../schedule/fixture.md)

- Contains multiple [Item](../inventory/item.md) entities

---

## **Considerations**

- **Ownership:** Each inventory must have a clear owner (Tournament, Venue, etc.)
- **Item Management:** Items can be added to multiple inventories
- **Validation:** Implement checks for sufficient items across all matches

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO 28000:2007 - Specification for security management systems for the supply chain](https://www.iso.org/standard/44651.html)
- [ISO 9001:2015 - Quality management systems — Requirements](https://www.iso.org/standard/62085.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Entity patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event inventory management

  standards

## See Also

- [Item](../inventory/item.md)
- [Stock Record](../inventory/stock_record.md)
- [Tournament](../tournament/tournament.md)
- [Fixture](../schedule/fixture.md)
- [Business README](../README.md)

---
