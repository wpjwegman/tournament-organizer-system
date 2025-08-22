# **Target Audience** (Data Model - Template Entity)

## **Introduction**

A **Target Audience** Entity Template defines a reusable blueprint for identifying and categorizing groups of
participants, spectators, or other stakeholders in a tournament context. It serves as a standardized format for defining
audience characteristics, requirements, and roles.

As an Entity Template, it ensures consistent audience targeting across the system while maintaining flexibility for
different types of tournaments and their specific requirements. It is commonly referenced by [Rule](../discipline/activity/variation/rule.md) and Safety Guideline templates to specify which groups they apply to.

It inherits standard attributes from the .

It inherits properties from the [Base Entity](../foundation/base_entity.md).

---

## **Attributes**

**Note:** This Entity Template includes the standard attributes (`ID`, `Status` [e.g., Active, Inactive], `CreatedAt`,
`LastUpdatedAt`, `Version`) defined in the [Base Entity](../foundation/base_entity.md).

| Attribute           | Description                                                  | Type         | Required | Notes / Example                                                                     |
| ------------------- | ------------------------------------------------------------ | ------------ | -------- | ----------------------------------------------------------------------------------- |
| **Name**            | Clear and concise title for the Target Audience.             | String       | Yes      | `"Youth Division"`, `"Professional League"`, `"Spectators"`, `"Officials"`          |
| **Description**     | Detailed explanation of the target audience characteristics. | String       | Yes      | `"Players aged 12-18 with intermediate skill level"`, `"All tournament spectators"` |
| **Type**            | The primary category of the target audience.                 | String       | Yes      | E.g., `Participant`, `Spectator`, `Official`, `Staff`, `Other`                      |
| **Age Range**       | Minimum and maximum age requirements (if applicable).        | Range        | Optional | `{min: 12, max: 18}`, `{min: 18, max: null}`                                        |
| **Skill Level**     | Required skill level (if applicable).                        | String       | Optional | E.g., `Beginner`, `Intermediate`, `Advanced`, `Professional`                        |
| **Gender Category** | Gender category requirements (if applicable).                | String       | Optional | E.g., `Male`, `Female`, `Mixed`, `Open`                                             |
| **Region**          | Geographic region or location requirements (if applicable).  | String       | Optional | `"North America"`, `"Europe"`, `"Global"`                                           |
| **Requirements**    | List of specific requirements for this audience group.       | List[String] | Optional | `["Valid ID", "Skill Certification", "Age Verification"]`                           |
| **Roles**           | List of roles this audience group can fulfill.               | List[String] | Optional | `["Player", "Coach"]`, `["Referee", "Scorekeeper"]`                                 |

---

## **Relationships**

- A `Target Audience` template can be referenced by:
  - to define its participant requirements
  - [Rule](../discipline/activity/variation/rule.md) templates to

    specify which groups the rules apply to

  - Safety Guideline templates to specify which groups the guidelines apply to (*future enhancement*)
- The specific implementation of a target audience within a tournament will be linked to records.
- A target audience may be referenced by multiple entities across the system.

---

## **Considerations**

- **Template Nature:** This template defines a standard target audience type. Instance-specific variations or customizations

  belong on the copied instance within its specific context (e.g., a specific tournament's implementation).

- **Copy Mechanism:** The process of copying this template definition into a target context (like a specific tournament)

  needs to be handled by application logic.

- **Template Management:**
  - Templates should be curated and maintained by organizational administrators
  - New templates can be added based on demographic standards and tournament requirements
  - Templates should be reviewed periodically for inclusivity and relevance
- **Template Usage:** The template should be referenced rather than copied, as target audiences are standardized across

  the system.

- **Flexibility:** Not all attributes are required for all audience types (e.g., Spectators don't need Skill Level).
- **Validation:** Required attributes must be validated against participant data when applicable.
- **Inclusivity:** Gender Category and other demographic attributes should comply with tournament regulations and

  inclusivity policies.

- **Role Alignment:** The Roles attribute should align with the tournament's [Role](../foundation/base_entity.md) definitions.
- **Requirement Verification:** All Requirements must be verifiable and documented when applicable.
- **Customization Balance:**
  - Templates provide structure while allowing personalization
  - Customizations should not break the fundamental audience structure
  - System should support both template-based and fully custom target audiences

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO 9001:2015 - Quality management systems — Requirements](https://www.iso.org/standard/62085.html)
- [ISO 26000:2020 - Guidance on social responsibility](https://www.iso.org/standard/42546.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Entity Template patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event audience management

  standards

## See Also

- [Organization README](../organization/README.md)
- [Organization](../organization/organization.md)
- [Rule](../discipline/activity/variation/rule.md)
- [Safety Guideline](../safety/safety.md)
- [Business README](../README.md)
