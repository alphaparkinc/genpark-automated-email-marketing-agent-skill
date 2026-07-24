class AutomatedEmailMarketingAgentClient:
    def generate_sequence(self, campaign_goal: str, audience_segment: str) -> dict:
        seq = [
            {"day": 0, "subject": f"Welcome! Here is your guide for {campaign_goal[:20]}", "variant": "A"},
            {"day": 3, "subject": "Quick question about your current workflow", "variant": "B"},
            {"day": 7, "subject": "Exclusive invitation: Try our premium agent features", "variant": "A"}
        ]
        return {
            "email_sequence": seq,
            "predicted_open_rate": 42.8
        }
