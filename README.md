# Langflow Components

Custom components for Langflow - AI workflow automation platform.

## SOW Builder Component

The **SOW Builder** is a Langflow component designed to create comprehensive Statement of Work (SOW) documents for projects. It streamlines the process of generating professional SOW documents by collecting key project information and formatting it into a structured, ready-to-use document.

### Features

- **Comprehensive Input Collection**: Gather all essential SOW elements including:
  - Project name and client information
  - Project objectives and goals
  - Detailed scope of work (inclusions/exclusions)
  - List of deliverables
  - Timeline and milestones
  - Resources required
  - Work location
  - Payment terms
  - Acceptance criteria

- **Multiple Output Formats**: Generate SOW documents in three formats:
  - **Markdown**: Professional formatting with headers and sections
  - **Plain Text**: Simple, readable format suitable for any text editor
  - **Structured**: JSON format for programmatic processing

- **Smart Formatting**: Automatically formats lists, sections, and metadata
- **Date Stamping**: Includes generation date for record-keeping
- **Flexible Requirements**: Required and optional fields to accommodate different project needs

### Installation

1. Clone this repository:
```bash
git clone https://github.com/nish1121/Lnagflow-components.git
cd Lnagflow-components
```

2. Ensure you have Langflow installed:
```bash
pip install langflow
```

3. Copy the component to your Langflow components directory or set the `LANGFLOW_COMPONENTS_PATH` environment variable:
```bash
export LANGFLOW_COMPONENTS_PATH=/path/to/Lnagflow-components/components
```

### Usage

#### In Langflow UI

1. Start Langflow:
```bash
langflow run
```

2. Open the Langflow UI in your browser (typically http://localhost:7860)

3. Find the "SOW Builder" component in the components panel

4. Drag it onto your canvas

5. Configure the inputs:
   - **Project Name** (required): Name of your project
   - **Client Name** (required): Client or organization name
   - **Project Objectives** (required): High-level goals
   - **Scope of Work** (required): Detailed work description
   - **Deliverables** (required): List of project deliverables
   - **Timeline/Milestones** (required): Project schedule
   - **Resources Required** (optional): Personnel, tools, equipment
   - **Work Location** (optional): Where work will be performed
   - **Payment Terms** (optional): Cost and payment schedule
   - **Acceptance Criteria** (optional): Deliverable acceptance criteria
   - **Output Format**: Choose Markdown, Plain Text, or Structured

6. Connect the component to your flow and run it

#### Example Output

Here's an example of what the SOW Builder generates (Markdown format):

```markdown
# Statement of Work

**Project:** AI-Powered Customer Service Platform
**Client:** TechCorp Inc.
**Date:** November 23, 2025

---

## 1. Project Objectives

- Implement an AI-powered customer service platform
- Reduce customer support costs by 30%
- Enhance customer satisfaction scores

## 2. Scope of Work

**Inclusions:**
- Design and development of conversational AI chatbot
- Integration with existing CRM system
- Training data preparation and model fine-tuning

**Exclusions:**
- Hardware procurement
- Third-party API costs

## 3. Deliverables

- Functional AI chatbot deployed on company website
- Mobile app integration (iOS and Android)
- Admin dashboard for monitoring conversations

## 4. Timeline and Milestones

- Week 1-2: Requirements gathering and design
- Week 3-6: Development and initial testing
- Week 7-8: Integration with CRM

---

*This Statement of Work is a binding agreement between the parties mentioned above.*
```

### Use Cases

- **Project Managers**: Quickly create SOW documents for new projects
- **Consultants**: Generate professional SOWs for client engagements
- **Sales Teams**: Standardize SOW creation for proposals
- **Legal/Procurement**: Ensure consistent SOW formatting and completeness
- **Workflow Automation**: Integrate SOW generation into larger AI workflows

### Component Structure

The SOW Builder component follows Langflow's custom component architecture:

- **Base Class**: Inherits from `langflow.custom.Component`
- **Inputs**: Uses `MessageTextInput` and `DropdownInput` for data collection
- **Outputs**: Returns `Data` object with formatted SOW document
- **Methods**: 
  - `build_sow()`: Main method that orchestrates SOW generation
  - `_build_markdown_sow()`: Generates Markdown format
  - `_build_plain_text_sow()`: Generates plain text format
  - `_build_structured_sow()`: Generates JSON structure
  - `_format_list_items()`: Helper for formatting lists

### Development

#### Running the Example

```bash
python example_usage.py
```

This will display sample inputs and usage instructions.

#### Testing the Component

The component can be tested within Langflow or by creating a custom test script that imports and instantiates the component.

### Requirements

- Python 3.8+
- Langflow (any recent version supporting the Component API)
- Standard library only (no additional dependencies)

### Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

### License

This project is open source. Please check the repository for license details.

### Support

For issues or questions:
- Open an issue on GitHub
- Check Langflow documentation: https://docs.langflow.org

### About Statement of Work (SOW)

A Statement of Work is a formal document that defines project-specific activities, deliverables, and timelines. It serves as a binding agreement between a service provider and client, ensuring:
- Clear project scope and objectives
- Defined deliverables and acceptance criteria
- Agreed-upon timelines and resources
- Payment terms and conditions
- Risk mitigation through detailed documentation

This component helps automate SOW creation while maintaining professional standards and completeness.
