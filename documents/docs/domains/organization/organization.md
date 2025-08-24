# **Organization** (Data Model - Template Entity)

## **Introduction**

The **Organization** Entity represents a structured group such as a business, school, sports federation, sponsor, or
supplier involved in the Tournament Organizer ecosystem. It manages key identifying information, contact details (via
reference), and relationships for these entities.

It possesses a unique identity and lifecycle, managed according to the [Base Entity](../foundation/base_entity.md).

It inherits properties from the [Base Entity](../foundation/base_entity.md).

---

## **Attributes**

**Note:** This Entity includes the standard attributes (`ID`, `Status`, `CreatedAt`, `LastUpdatedAt`) defined in the [Base Entity](../foundation/base_entity.md).

| Attribute               | Description                                                                                     | Type       | Required | Notes / Example                                                                  |
| ----------------------- | ----------------------------------------------------------------------------------------------- | ---------- | -------- | -------------------------------------------------------------------------------- |
| **Name**                | The official or common name of the organization.                                                | String     | Yes      | Should be unique within a relevant scope. Example: "Global Badminton Federation" |
| **Description**         | A brief description of the organization and its purpose or activities.                          | String     | Optional | "The international governing body for badminton."                                |
| **Type**                | Categorizes the organization. See .                                                             | String     | Optional | Example: `"Sports Federation"`, `"Educational"`, `"Sponsor"`                     |
| **Contact Information** | Optional reference (by ID) to the primary \*\*\*\* Entity for this organization.                | UUID       | Optional | Example: `ci-a1b2c3d4-e5f6-4890-1234-567890abc020`                               |
| **Units**               | List of references (by ID) to internal \*\*\*\* Entities.                                       | List[UUID] | Optional | Example: `[ou-a1b2c3d4-e5f6-4890-1234-567890abc022]`                             |
| **Tax Identifier**      | Optional tax identification number (e.g., VAT ID, EIN) or similar official registration number. | String     | Optional | Example: "NL123456789B01"                                                        |
| **Media**               | Optional list of references (by ID) to \*\*\*\* entities associated with this organization.     | List[UUID] | Optional | Example: `[media-a1b2c3d4-e5f6-4890-1234-567890abc099]`                          |
| **Inventory**           | Reference to the organization's \*\*\*\* for managing equipment and supplies.                   | UUID       | Optional | `inventory-uuid-org-x`                                                           |

---

## **Relationships**

- An `Organization` **Entity** references other **Entities** via ID:

  - Optionally references one `Contact Information` Entity (which contains address, phone, email, media links, etc.).
  - Optionally references multiple `Organizational Unit` Entities representing its internal structure.
  - Optionally references one `Inventory` Entity for managing organization equipment and supplies.

- Other **Entities** reference `Organization`:

  - A `Tournament` may reference an `Organization` as its organizer or sponsor.
  - A `Venue` may reference an `Organization` as its owner or manager.
  - An `Organizational Unit` references its parent `Organization`.
  - A `Member` Entity indicates affiliation via context (e.g., being listed in an `Organizational Unit` belonging to

    this `Organization`).

---

## **Considerations**

- **Uniqueness:** The `Name` attribute should ideally be unique or managed within a relevant scope (e.g., unique among

  top-level organizations).

- **Categorization:** Consistent use of the `Type` attribute facilitates filtering and management. Allowed values

  defined in \*\*\*\*.

- **Contact Details:** All contact methods (address, phone, email, media links) are accessed via the referenced

  `Contact Information` entity.

- **Internal Structure:** The `Units` attribute allows modelling hierarchical structures within the organization.
- **Status Workflow:** Define clear processes for `Status` transitions (e.g., Active, Inactive, Pending Verification).
- **Inventory Management:** The organization's inventory should be managed in coordination with tournament and venue

  inventories to ensure proper resource allocation and tracking.

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO 9001:2015 - Quality management systems — Requirements](https://www.iso.org/standard/62085.html)
- [ISO 26000:2020 - Guidance on social responsibility](https://www.iso.org/standard/42546.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Entity patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event organization

  management standards

## See Also

- [Organization README](../organization/README.md)
- [Target Audience](../organization/target_audience.md)
- [Unit README](../organization/unit/README.md)
- [Contact Information](../identity/contact_information.md)
- [Inventory README](../inventory/README.md)
- [Business README](../README.md)

---
