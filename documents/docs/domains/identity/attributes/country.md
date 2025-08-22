# **Country** (Data Model - Value Object)

## **Introduction**

A **Country** Value Object represents a country or nation in a standardized format. It provides a consistent way to
handle country information across the tournament system, including country codes, names, and related metadata.

It describes characteristics of a country and is typically embedded within other entities (like [Address](address.md) or
[Contact Information](../contact_information.md)) to specify location details.

It inherits properties from the [Base Entity](../../foundation/base_entity.md).

---

## **Attributes**

| Attribute    | Description                                   | Type    | Required | Notes / Example                                   |
| ------------ | --------------------------------------------- | ------- | -------- | ------------------------------------------------- |
| **Name**     | The full name of the country.                 | String  | Yes      | `"United States"`, `"Canada"`, `"United Kingdom"` |
| **Code**     | The ISO 3166-1 alpha-2 country code.          | String  | Yes      | `"US"`, `"CA"`, `"GB"`                            |
| **Code3**    | The ISO 3166-1 alpha-3 country code.          | String  | Optional | `"USA"`, `"CAN"`, `"GBR"`                         |
| **Numeric**  | The ISO 3166-1 numeric country code.          | Integer | Optional | `840`, `124`, `826`                               |
| **Region**   | The geographic region the country belongs to. | String  | Optional | `"North America"`, `"Europe"`, `"Asia"`           |
| **Currency** | The primary currency code for the country.    | String  | Optional | `"USD"`, `"CAD"`, `"GBP"`                         |

---

## **Domain Rules**

### **Standardization Rules**

- **ISO Standards**: Use ISO 3166-1 alpha-2 country codes for consistency
- **Official Names**: Use official country names as recognized by international standards
- **Territory Handling**: Include territories and dependencies as separate entries where appropriate
- **Historical Accuracy**: Maintain historical accuracy for address records

### **Address Formatting Rules**

- **Regional Formats**: Country selection may affect address format requirements
- **Postal Code Validation**: Postal code formats vary by country and should be validated accordingly
- **Address Components**: Required address fields may vary by country
- **International Standards**: Follow international addressing standards for each country

### **Regulatory Compliance Rules**

- **Data Residency**: Some countries have specific data residency requirements
- **Privacy Laws**: Different countries have varying privacy and data protection laws
- **Tournament Regulations**: Some countries have specific regulations for tournament organization
- **Tax Implications**: Country selection may affect tax and financial reporting requirements

---

## **Relationships**

- A `Country` Value Object is embedded within [Address](address.md) entities.
- A `Country` Value Object may be embedded within [Contact Information](../contact_information.md) entities.
- A `Country` Value Object may be referenced by [Organization](../../organization/README.md) entities.

---

## **Considerations**

- **Standardization:** Use ISO 3166-1 standards for country codes.
- **Validation:** Country codes should be validated against the official ISO list.
- **Localization:** Country names should be displayed in the appropriate language.
- **Currency:** Currency information should be kept up-to-date.

---

## References

- [ISO 3166-1 — Country codes (Wikipedia overview)](https://en.wikipedia.org/wiki/ISO_3166-1)
- [ISO 4217 — Currency codes (Wikipedia overview)](https://en.wikipedia.org/wiki/ISO_4217)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Value Object patterns

- [UN M49 - Standard Country or Area Codes for Statistical Use](https://unstats.un.org/unsd/methodology/m49/)

## See Also

- [Address](../../identity/attributes/address.md)
- [Contact Information](../../identity/contact_information.md)
- [Organization](../../organization/organization.md)
- [Identity README](../../identity/README.md)
- [Business README](../../README.md)
