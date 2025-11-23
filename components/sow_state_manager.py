from langflow.custom import Component
from langflow.inputs import MessageTextInput
from langflow.io import Output
from langflow.schema.message import Message
import json


class SOWStateManager(Component):
    display_name = "SOW State Manager"
    description = "Tracks conversation state for SOW inputs and returns the next question."
    icon = "edit"
    name = "SOWStateManager"

    # ---------- INPUTS ----------
    inputs = [
        MessageTextInput(
            name="last_message",
            display_name="Last User Message",
            info="The latest user message (Message or plain text).",
        ),
        MessageTextInput(
            name="current_state_json",
            display_name="Current State (JSON)",
            info="JSON string holding SOW state; leave empty on first run.",
            value="",
        ),
    ]

    # ---------- OUTPUTS ----------
    outputs = [
        Output(
            name="state_json",
            display_name="Updated State (JSON)",
            method="run",
        ),
        Output(
            name="assistant_message",
            display_name="Assistant Message",
            method="run",
        ),
        Output(
            name="status",
            display_name="Status (collecting/ready)",
            method="run",
        ),
        Output(
            name="pending_key",
            display_name="Pending Key",
            method="run",
        ),
        Output(
            name="utility_type",
            display_name="Utility Type",
            method="run",
        ),
        Output(
            name="deployment_model",
            display_name="Deployment Model",
            method="run",
        ),
        Output(
            name="modules_selected",
            display_name="Modules Selected",
            method="run",
        ),
        Output(
            name="implementation_timeline",
            display_name="Implementation Timeline",
            method="run",
        ),
        Output(
            name="scope_preferences",
            display_name="Scope Preferences",
            method="run",
        ),
        Output(
            name="done",
            display_name="All Slots Filled?",
            method="run",
        ),
    ]

    # helper: Message / str / None -> clean text
    def _to_text(self, value) -> str:
        if isinstance(value, Message):
            return (value.text or "").strip()
        if value is None:
            return ""
        return str(value).strip()

    def _default_state(self):
        return {
            "slots": {
                "utility_type": "",
                "deployment_model": "",
                "modules_selected": "",
                "implementation_timeline": "",
                "scope_preferences": "",
            },
            "pending_key": None,        # which field we are waiting for
            "status": "collecting",     # or "ready"
        }

    # ---------- LOGIC ----------
    # NOTE: make args OPTIONAL and accept *args, **kwargs so LangFlow never breaks
    def run(self, last_message=None, current_state_json=None, *args, **kwargs):
        # 1) Normalize inputs
        user_text = self._to_text(last_message)

        # 2) Load or initialize state
        if current_state_json:
            try:
                state = json.loads(self._to_text(current_state_json))
            except Exception:
                state = self._default_state()
        else:
            state = self._default_state()

        slots = state.get("slots") or self._default_state()["slots"]
        pending_key = state.get("pending_key")
        status = state.get("status", "collecting")

        # Fixed order of questions
        order = [
            "utility_type",
            "deployment_model",
            "modules_selected",
            "implementation_timeline",
            "scope_preferences",
        ]

        # Question text for each slot
        questions = {
            "utility_type": (
                "What utility type are you implementing? "
                "Choose one: GAS, Electric, Water, Multi-service, or Waste Management."
            ),
            "deployment_model": "What is the deployment model? Choose: Cloud or OnPrem.",
            "modules_selected": (
                "Which Cayenta modules are in scope? (e.g., CIS, Billing, WMS, ERP, HCM)."
            ),
            "implementation_timeline": (
                "What is the planned implementation timeline? "
                "(e.g., 12 months + 3 months hypercare)."
            ),
            "scope_preferences": (
                "Briefly describe any key scope preferences: integrations, data migration depth, "
                "customizations, or constraints."
            ),
        }

        # 3) If we were waiting for a specific field, store this message as its answer
        if pending_key and user_text:
            if pending_key in slots:
                slots[pending_key] = user_text

        # 4) Decide next pending_key by finding first empty field
        next_pending = None
        for key in order:
            if not slots.get(key):
                next_pending = key
                break

        if next_pending is None:
            # All fields filled -> ready for SOW generation
            status = "ready"
            assistant_message = (
                "Great, I have all the required details. I'll now generate the Statement of Work."
            )
            done = True
        else:
            status = "collecting"
            assistant_message = questions[next_pending]
            done = False

        # 5) Update state object
        state["slots"] = slots
        state["pending_key"] = next_pending
        state["status"] = status

        # 6) Serialize state back to JSON
        state_json = json.dumps(state)

        return {
            "state_json": state_json,
            "assistant_message": assistant_message,
            "status": status,
            "pending_key": next_pending or "",
            "utility_type": slots.get("utility_type", ""),
            "deployment_model": slots.get("deployment_model", ""),
            "modules_selected": slots.get("modules_selected", ""),
            "implementation_timeline": slots.get("implementation_timeline", ""),
            "scope_preferences": slots.get("scope_preferences", ""),
            "done": done,
        }
