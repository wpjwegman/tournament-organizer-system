# **Address** (Data Model - Value Object)

## **Introduction**

An **Address** is a **Value Object** representing the structured components of a physical location. It is defined
entirely by its attributes and does not have its own identity or lifecycle.

Addresses are **embedded** within owning **Entities** (like profiles or organizations) to describe a specific location associated with that
Entity (e.g., mailing address, billing address, venue location).

As a Value Object, it does not have identity or lifecycle - it is immutable and defined by its attributes.

---

## **Attributes**

| Attribute                | Description                                                                                 | Type   | Required | Notes / Example                                      |
| ------------------------ | ------------------------------------------------------------------------------------------- | ------ | -------- | ---------------------------------------------------- |
| **Street**               | The primary street address line(s), including house number and street name.                 | String | Yes      | Example: "123 Main St\nSuite 101", "45 B Oak Avenue" |
| **Locality**             | The city, town, or village name.                                                            | String | Yes      | Example: "Metropolis", "Smallville"                  |
| **Region**               | The state, province, or administrative region.                                              | String | Yes      | Example: "CA", "New York", "Ontario"                 |
| **Postal Code**          | The postal code (e.g., ZIP code) used for mail delivery.                                    | String | Yes      | Example: "90210", "SW1A 0AA"                         |
| **Country**              | Reference (by ID) to the [Country](../../identity/attributes/country.md) Entity. | UUID   | Yes      | Example: `c0a1b2c3-d4e5-4f67-8901-234567abcdef`      |
| **Building Name Number** | Identifier for a specific building within a complex, if applicable.                         | String | No       | Example: "Building A", "Tower 3"                     |
| **Latitude**             | Optional geographic coordinate (latitude).                                                  | Number | Optional | Example: `40.7128`                                   |
| **Longitude**            | Optional geographic coordinate (longitude).                                                 | Number | Optional | Example: `-74.0060`                                  |

---

## **Relationships**

- An `Address` **Value Object** has no independent identity and therefore no outgoing relationships defined by

  references (IDs), except for the reference to a `Country` Entity.

- It is always **embedded within** an owning **Entity**.

---

## **Considerations**

- **Embedding:** As a Value Object, Addresses are always part of another Entity (e.g., `Contact Information`, `Venue`).
- **Immutability:** Value Objects are conceptually immutable. If an address needs to change, the owning Entity should

  replace the entire embedded Address object with a new one.

- **Country Entity:** This model assumes the existence of a separate `Country` Entity, identified by UUID, which holds

  country details (Name, Code, etc.).

- **Address Standardization/Validation:** Consider implementing address validation logic (potentially using external

  services) within the application logic where Addresses are created or updated.

- **Internationalization:** Address formats vary. Validation rules may depend on the referenced `Country`.
- **Required Fields:** The required fields (`Street`, `Locality`, `Region`, `Postal Code`, `Country`) represent a common

  baseline.

---

## References

- [ISO 19112:2019 - Geographic information — Spatial referencing by geographic identifiers](https://www.iso.org/standard/74039.html)
- [ISO 3166-1:2020 - Codes for the representation of names of countries and their subdivisions](https://www.iso.org/standard/72482.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Value Object patterns

- [W3C Address Data Model](https://www.w3.org/TR/vcard-rdf/#d4e1199)

## See Also

- [Country](../../identity/attributes/country.md)
- [Contact Information](../../identity/contact_information.md)
- [Venue](../../venue/venue.md)
- [Identity README](../../identity/README.md)
- [Business README](../../README.md)

---
