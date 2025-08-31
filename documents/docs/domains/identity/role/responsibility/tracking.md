# **Tracking** (Data Model - Value Object)

## **Introduction**

A **Tracking** is a **Value Object** that represents the execution monitoring and progress tracking for a Task. This
model captures the "how it's being done" aspects of task execution, including progress, time tracking, and
execution-specific notes. Tracking information is optional and can be embedded within Task entities when execution
monitoring is required.

For example, in a tournament context, tracking might monitor "Equipment Safety Check" progress or "Court Preparation"
completion, while in a business context, it might track "Project Review" status or "Quality Assurance" milestones.

As a Value Object, it does not have identity or lifecycle - it is immutable and defined by its attributes.

---

## **Attributes**

| Attribute              | Description                           | Type          | Required | Notes / Example                                    |
| ---------------------- | ------------------------------------- | ------------- | -------- | -------------------------------------------------- |
| **Progress**           | Percentage of task completion (0-100) | Integer       | No       | 75 (0-100 scale)                                   |
| **Actual Hours**       | Time actually spent on the task       | Float         | No       | 2.25 (in hours)                                    |
| **Started At**         | When execution began                  | DateTime      | No       | 2024-06-15 08:15:00                                |
| **Completed At**       | When execution finished               | DateTime      | No       | 2024-06-15 10:30:00                                |
| **Notes**              | Execution-specific notes and updates  | Text          | No       | "Equipment #3 needs replacement"                   |
| **Issues**             | Problems encountered during execution | List[String]  | No       | ["Missing safety certificate", "Delayed delivery"] |
| **Quality Score**      | Assessment of task execution quality  | Integer       | No       | 85 (0-100 scale)                                   |
| **Checklist Progress** | Which checklist items are completed   | List[Boolean] | No       | [true, true, false, true]                          |

---

## **Business Rules**

### **Tracking Rules**

1. **Progress Validation**: Progress must be 0-100%
2. **Time Validation**: Actual hours cannot exceed estimated hours by more than 50% without approval
3. **Completion Rules**: Completion requires progress = 100% or explicit completion
4. **Assignment**: Responsibility for execution lies with the assigned role

### **Quality Assessment**

1. **Quality Score**: Required upon completion
2. **Score Range**: 0-100 scale with clear criteria
3. **Assessment Criteria**: Based on checklist completion, time efficiency, and issue resolution

### **Issue Management**

1. **Issue Reporting**: Issues must be reported within 2 hours of discovery
2. **Issue Escalation**: Critical issues escalate after 4 hours without resolution
3. **Issue Resolution**: All issues must be resolved or documented before completion

---

## **Relationships**

- Tracking is always embedded within a Task entity and does not have independent identity
- Tracking can reference checklist items through boolean progress indicators
- Tracking may reference other entities through notes and issues
- Responsibility for execution is handled by the role assignment mechanism

---

## **Usage Guidelines**

- Use tracking when task execution monitoring is required
- Update progress regularly to maintain accurate status
- Document issues promptly to enable timely resolution
- Assess quality objectively based on defined criteria
- Use notes for context-specific information and updates

---

## **Implementation Notes**

- Tracking is embedded as a Value Object within Task entities
- Tracking attributes are only populated when execution monitoring is needed
- Tracking data supports analytics and continuous improvement
- Tracking can be enabled/disabled based on context requirements

---

## References

- [ISO 8000-2:2017 - Data quality - Part 2: Vocabulary](https://www.iso.org/standard/36326.html)
- [ISO 21500:2021 - Guidance on project management](https://www.iso.org/standard/50003.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

  by Eric Evans - Value Object patterns

- [Event Management Body of Knowledge (EMBOK)](https://www.embok.org/index.php/embok-model) - Event monitoring standards

## See Also

- [Task](../../../identity/role/responsibility/task.md)
- [Responsibility](../../../identity/role/responsibility/responsibility.md)
- [Skill](../../../identity/role/responsibility/skill.md)
- [Identity README](../../../identity/README.md)
- [Business README](../../../README.md)

---
