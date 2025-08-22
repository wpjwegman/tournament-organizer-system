# **Account** (Data Model - Entity)

## **Introduction**

An **Account** Entity represents a user account within the tournament system. It provides a comprehensive way to handle
account information for authentication, authorization, and user management within the tournament system.

It describes account characteristics and coordinates with other entities (like [User](../profile/human.md), [Setting](setting/setting.md),
and [Permission](../role/permission/permission.md)) to provide complete account oversight.

It inherits properties from the [Base Entity](../../foundation/base_entity.md).

---

## **Attributes**

| Attribute          | Description                                         | Type     | Required | Notes / Example                                      |
| ------------------ | --------------------------------------------------- | -------- | -------- | ---------------------------------------------------- |
| **ID**             | Unique identifier for the account entity.           | UUID     | Yes      | `"a123e456-7890-1234-5678-901234567890"`             |
| **Username**       | The username for the account.                       | String   | Yes      | `"john.doe"`, `"jane_smith"`, `"admin"`              |
| **Email**          | The email address associated with the account.      | String   | Yes      | `"john.doe@example.com"`, `"jane.smith@company.com"` |
| **Password Hash**  | The hashed password for the account.                | String   | Yes      | Securely hashed password                             |
| **Status**         | The status of the account.                          | String   | Optional | `"Active"`, `"Inactive"`, `"Suspended"`, `"Locked"`  |
| **Type**           | The type of account.                                | String   | Optional | `"User"`, `"Admin"`, `"Organizer"`, `"Participant"`  |
| **Last Login**     | The timestamp of the last login.                    | DateTime | Optional | `"2024-01-15T10:30:00Z"`                             |
| **Login Attempts** | Number of failed login attempts.                    | Integer  | Optional | `0`, `3`, `5`                                        |
| **Lockout Until**  | Timestamp until account is locked.                  | DateTime | Optional | `"2024-01-15T11:30:00Z"`                             |
| **Settings**       | Account settings and preferences.                   | Object   | Optional | Embedded [Setting](setting/setting.md) Value Objects         |
| **Created At**     | Timestamp when the account entity was created.      | DateTime | Yes      | `"2024-01-15T10:30:00Z"`                             |
| **Updated At**     | Timestamp when the account entity was last updated. | DateTime | Yes      | `"2024-01-20T14:45:00Z"`                             |

---

## **Relationships**

- An `Account` Entity is associated with a [User](../profile/human.md) entity.
- An `Account` Entity may be associated with [Permission](../role/permission/permission.md) entities.
- An `Account` Entity may be associated with [Role](../role/role.md) entities.

---

## **Considerations**

- **Security:** Account security should be prioritized with strong passwords and multi-factor authentication.
- **Privacy:** Account information should be handled with appropriate privacy controls.
- **Access Control:** Account access should be controlled based on permissions and roles.
- **Monitoring:** Account activity should be monitored for security purposes.
- **Recovery:** Account recovery processes should be available and secure.

---

## References

- [ISO/IEC 27001:2022 - Information security, cybersecurity and privacy protection](https://www.iso.org/standard/27001)
- [NIST Special Publication 800-63-3: Digital Identity Guidelines](https://pages.nist.gov/800-63-3/)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans

- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

## See Also

- [Identity README](../../identity/README.md)
- [Contact Information](../../identity/contact_information.md)
- [Role](../../identity/role/role.md)
- [Permission](../../identity/role/permission/README.md)
- [Business README](../../README.md)
