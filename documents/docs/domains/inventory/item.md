# **Item** (Data Model - Template Entity)

## **Introduction**

An **Item** Entity represents a specific type of equipment, supply, or resource that can be tracked in inventories. It
defines the base characteristics and categorization of an item, which can then be referenced by stock records to track
actual quantities and by groups for logical organization.

It inherits properties from the [Base Entity](../foundation/base_entity.md).

---

## **Attributes**

**Note:** This Entity includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined in the [Base Entity](../foundation/base_entity.md).

| Attribute          | Description                               | Type    | Required | Notes / Example                              |
| ------------------ | ----------------------------------------- | ------- | -------- | -------------------------------------------- |
| **Name**           | Unique identifier for the item type.      | String  | Yes      | `"Official Match Ball"`, `"Field Cone"`      |
| **Description**    | Detailed explanation of the item.         | Text    | Yes      | `"Official tournament match ball"`           |
| **Type**           | Classification of the item.               | String  | Yes      | `Prop`, `Marker`, `Equipment`, `Supply`      |
| **Category**       | Primary category for grouping.            | String  | Yes      | `Sports`, `Technical`, `Furniture`, `Safety` |
| **Unit**           | Unit of measurement.                      | String  | Yes      | `pieces`, `sets`, `pairs`                    |
| **Specifications** | Technical specifications or requirements. | Object  | No       | `{ size: "5", material: "leather" }`         |
| **Quantity**       | Total quantity available.                 | Integer | Yes      | `50`                                         |
| **Reserved**       | Quantity currently reserved.              | Integer | Yes      | `10`                                         |
| **Available**      | Quantity currently available.             | Integer | Yes      | `40`                                         |
| **Media**          | List of references to assets.             | Array   | No       | `[media-uuid-1, media-uuid-2]`               |

---

## **Relationships**

- May be referenced by multiple inventories

---

## **Considerations**

- **Quantity Management:** Changes in stock level (additions, removals, reservations) update the Quantity and Available

  fields

- **Zero Quantity:** A quantity of zero indicates the item is out of stock
- **Validation:** Available quantity must be less than or equal to Quantity minus Reserved
- **Reusability:** Items are reusable across different inventories and groups
- **Categorization:** Clear categorization helps with organization and filtering
- **Specifications:** Detailed specifications help ensure correct item usage
- **Media:** Visual references help with item identification

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO 28000:2007 - Specification for security management systems for the supply chain](https://www.iso.org/standard/44651.html)
- [ISO 9001:2015 - Quality management systems — Requirements](https://www.iso.org/standard/62085.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Entity patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event equipment management

  standards

## See Also

- [Inventory](../inventory/inventory.md)
- [Stock Record](../inventory/stock_record.md)
- [Media README](../media/README.md)
- [Business README](../README.md)

---
