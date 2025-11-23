"""
SOW Builder Component for Langflow

This component helps create comprehensive Statement of Work (SOW) documents
by collecting project information and generating a structured SOW output.
"""

from datetime import datetime
from typing import Optional
from langflow.custom import Component
from langflow.io import MessageTextInput, DropdownInput, Output
from langflow.schema import Data


class SOWBuilder(Component):
    display_name = "SOW Builder"
    description = "Create comprehensive Statement of Work (SOW) documents for projects"
    icon = "file-text"
    name = "SOWBuilder"

    inputs = [
        MessageTextInput(
            name="project_name",
            display_name="Project Name",
            info="Name of the project or engagement",
            required=True,
        ),
        MessageTextInput(
            name="client_name",
            display_name="Client Name",
            info="Name of the client or organization",
            required=True,
        ),
        MessageTextInput(
            name="project_objectives",
            display_name="Project Objectives",
            info="High-level goals and objectives of the project",
            multiline=True,
            required=True,
        ),
        MessageTextInput(
            name="scope_of_work",
            display_name="Scope of Work",
            info="Detailed description of work to be performed (include inclusions and exclusions)",
            multiline=True,
            required=True,
        ),
        MessageTextInput(
            name="deliverables",
            display_name="Deliverables",
            info="List of project deliverables (one per line or comma-separated)",
            multiline=True,
            required=True,
        ),
        MessageTextInput(
            name="timeline",
            display_name="Timeline/Milestones",
            info="Project timeline with key milestones and dates",
            multiline=True,
            required=True,
        ),
        MessageTextInput(
            name="resources",
            display_name="Resources Required",
            info="Personnel, tools, equipment, or other resources needed",
            multiline=True,
            required=False,
        ),
        MessageTextInput(
            name="location",
            display_name="Work Location",
            info="Physical or remote location(s) where work will be performed",
            required=False,
        ),
        MessageTextInput(
            name="payment_terms",
            display_name="Payment Terms",
            info="Cost breakdown, payment schedule, and terms",
            multiline=True,
            required=False,
        ),
        MessageTextInput(
            name="acceptance_criteria",
            display_name="Acceptance Criteria",
            info="Criteria for deliverable acceptance and project completion",
            multiline=True,
            required=False,
        ),
        DropdownInput(
            name="output_format",
            display_name="Output Format",
            info="Choose the format for the SOW document",
            options=["Markdown", "Plain Text", "Structured"],
            value="Markdown",
        ),
    ]

    outputs = [
        Output(display_name="SOW Document", name="sow_output", method="build_sow")
    ]

    def build_sow(self) -> Data:
        """
        Build a comprehensive Statement of Work document from the provided inputs.
        """
        # Get current date for document generation
        current_date = datetime.now().strftime("%B %d, %Y")
        
        # Build the SOW document based on the selected format
        if self.output_format == "Markdown":
            sow_content = self._build_markdown_sow(current_date)
        elif self.output_format == "Plain Text":
            sow_content = self._build_plain_text_sow(current_date)
        else:  # Structured
            sow_content = self._build_structured_sow(current_date)
        
        # Create the Data object with the SOW content
        result = Data(
            text=sow_content,
            data={
                "project_name": self.project_name,
                "client_name": self.client_name,
                "generated_date": current_date,
                "format": self.output_format
            }
        )
        
        self.status = f"SOW generated for project: {self.project_name}"
        return result

    def _build_markdown_sow(self, date: str) -> str:
        """Build SOW in Markdown format."""
        sections = []
        
        # Header
        sections.append(f"# Statement of Work")
        sections.append(f"\n**Project:** {self.project_name}")
        sections.append(f"**Client:** {self.client_name}")
        sections.append(f"**Date:** {date}")
        sections.append("\n---\n")
        
        # Project Objectives
        sections.append("## 1. Project Objectives")
        sections.append(f"\n{self.project_objectives}\n")
        
        # Scope of Work
        sections.append("## 2. Scope of Work")
        sections.append(f"\n{self.scope_of_work}\n")
        
        # Deliverables
        sections.append("## 3. Deliverables")
        sections.append(f"\n{self._format_list_items(self.deliverables)}\n")
        
        # Timeline
        sections.append("## 4. Timeline and Milestones")
        sections.append(f"\n{self.timeline}\n")
        
        # Resources (optional)
        if self.resources:
            sections.append("## 5. Resources Required")
            sections.append(f"\n{self.resources}\n")
        
        # Location (optional)
        if self.location:
            sections.append("## 6. Work Location")
            sections.append(f"\n{self.location}\n")
        
        # Payment Terms (optional)
        if self.payment_terms:
            sections.append("## 7. Payment Terms")
            sections.append(f"\n{self.payment_terms}\n")
        
        # Acceptance Criteria (optional)
        if self.acceptance_criteria:
            sections.append("## 8. Acceptance Criteria")
            sections.append(f"\n{self.acceptance_criteria}\n")
        
        # Footer
        sections.append("---")
        sections.append("\n*This Statement of Work is a binding agreement between the parties mentioned above.*")
        
        return "\n".join(sections)

    def _build_plain_text_sow(self, date: str) -> str:
        """Build SOW in plain text format."""
        sections = []
        
        # Header
        sections.append("=" * 70)
        sections.append("STATEMENT OF WORK")
        sections.append("=" * 70)
        sections.append(f"\nProject: {self.project_name}")
        sections.append(f"Client: {self.client_name}")
        sections.append(f"Date: {date}")
        sections.append("\n" + "-" * 70 + "\n")
        
        # Project Objectives
        sections.append("1. PROJECT OBJECTIVES")
        sections.append("-" * 70)
        sections.append(f"{self.project_objectives}\n")
        
        # Scope of Work
        sections.append("2. SCOPE OF WORK")
        sections.append("-" * 70)
        sections.append(f"{self.scope_of_work}\n")
        
        # Deliverables
        sections.append("3. DELIVERABLES")
        sections.append("-" * 70)
        sections.append(f"{self._format_list_items(self.deliverables)}\n")
        
        # Timeline
        sections.append("4. TIMELINE AND MILESTONES")
        sections.append("-" * 70)
        sections.append(f"{self.timeline}\n")
        
        # Resources (optional)
        if self.resources:
            sections.append("5. RESOURCES REQUIRED")
            sections.append("-" * 70)
            sections.append(f"{self.resources}\n")
        
        # Location (optional)
        if self.location:
            sections.append("6. WORK LOCATION")
            sections.append("-" * 70)
            sections.append(f"{self.location}\n")
        
        # Payment Terms (optional)
        if self.payment_terms:
            sections.append("7. PAYMENT TERMS")
            sections.append("-" * 70)
            sections.append(f"{self.payment_terms}\n")
        
        # Acceptance Criteria (optional)
        if self.acceptance_criteria:
            sections.append("8. ACCEPTANCE CRITERIA")
            sections.append("-" * 70)
            sections.append(f"{self.acceptance_criteria}\n")
        
        # Footer
        sections.append("=" * 70)
        sections.append("This Statement of Work is a binding agreement between the parties")
        sections.append("mentioned above.")
        sections.append("=" * 70)
        
        return "\n".join(sections)

    def _build_structured_sow(self, date: str) -> str:
        """Build SOW in structured dictionary format (JSON-like)."""
        sow_dict = {
            "document_type": "Statement of Work",
            "metadata": {
                "project_name": self.project_name,
                "client_name": self.client_name,
                "generated_date": date,
            },
            "sections": {
                "project_objectives": self.project_objectives,
                "scope_of_work": self.scope_of_work,
                "deliverables": self.deliverables.split("\n") if "\n" in self.deliverables else self.deliverables.split(","),
                "timeline": self.timeline,
            }
        }
        
        # Add optional fields if provided
        if self.resources:
            sow_dict["sections"]["resources"] = self.resources
        if self.location:
            sow_dict["sections"]["location"] = self.location
        if self.payment_terms:
            sow_dict["sections"]["payment_terms"] = self.payment_terms
        if self.acceptance_criteria:
            sow_dict["sections"]["acceptance_criteria"] = self.acceptance_criteria
        
        # Convert to formatted string representation
        import json
        return json.dumps(sow_dict, indent=2)

    def _format_list_items(self, text: str) -> str:
        """Format text as a list with bullet points or numbers."""
        if not text:
            return ""
        
        # Split by newlines or commas
        items = []
        if "\n" in text:
            items = [item.strip() for item in text.split("\n") if item.strip()]
        else:
            items = [item.strip() for item in text.split(",") if item.strip()]
        
        # Format as markdown list
        formatted = []
        for i, item in enumerate(items, 1):
            # Check if item already starts with a bullet or number
            if item.startswith("-") or item.startswith("*") or item[0].isdigit():
                formatted.append(item)
            else:
                formatted.append(f"- {item}")
        
        return "\n".join(formatted)
