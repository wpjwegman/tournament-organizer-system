# **Emergency Contact** (Data Model - Value Object)

## **Introduction**

An **Emergency Contact** is a **Value Object** representing the details of a person designated to be contacted in case
of an emergency involving the owner of the parent record.

As a Value Object, it is defined entirely by its attributes and does not have its own identity or lifecycle. It is
always **embedded** within an owning `Contact Information` Entity.

It inherits properties from the [Base Entity](../../foundation/base_entity.md).

---

## **Attributes**

| Attribute                   | Description                                                                                                                | Type   | Required | Notes / Example                                                                  |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------ | -------- | -------------------------------------------------------------------------------- |
| **Name**                    | The full name of the emergency contact person.                                                                             | String | Yes      | Example: "Jane Doe"                                                              |
| **Relationship To Subject** | The relationship of the emergency contact to the subject person (e.g., Parent, Spouse, Friend, Guardian).                  | String | Yes      | Example: `"Parent"`, `"Spouse"`, `"Friend"`, `"Guardian"`                        |
| **Contact Information**     | Reference to the Contact Information entity containing phone and email details.                                            | UUID   | Yes      |                                                                                  |
| **Notes**                   | Optional: Any specific instructions or notes regarding contacting this person (e.g., best time to call, alternate number). | Text   | Optional | Example: `"Primary contact, call anytime."`, `"If no answer, try mobile first."` |

---

## **Relationships**

- An `Emergency Contact` **Value Object** has no independent identity and holds no references to other entities.
- It is always **embedded within** an owning \*\*\*\* Entity.

---

## **Considerations**

- **Embedding:** This Value Object is intended to be part of a list within the `Contact Information` entity.
- **Contact Method:** At least one contact method (`Phone` or `Email`) should be required by application logic to ensure

  the contact is reachable.

- **Privacy:** The data stored (Name, Phone, Email, Relationship) is sensitive and requires appropriate access controls

  managed by the parent `Contact Information` context.

- **Immutability:** If contact details change, the owning `Contact Information` entity should replace the entire

  embedded `Emergency Contact` object.

---

## References

- [ISO 22320 — Emergency management (Wikipedia overview)](https://en.wikipedia.org/wiki/ISO_22320)
- [ISO/IEC 27001:2022 - Information security, cybersecurity and privacy protection](https://www.iso.org/standard/27001)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Value Object patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event emergency procedures

## See Also

- [Contact Information](../../identity/contact_information.md)
- [Identity README](../../identity/README.md)
- [First_Aid README](../../first_aid/README.md)
- [Safety](../../safety/safety.md)
- [Business README](../../README.md)

---
