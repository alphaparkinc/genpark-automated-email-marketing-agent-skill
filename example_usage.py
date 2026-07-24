from client import AutomatedEmailMarketingAgentClient

def main():
    client = AutomatedEmailMarketingAgentClient()
    res = client.generate_sequence("Onboard new SaaS leads", "Tech Founders")
    print(f"Predicted Open Rate: {res['predicted_open_rate']}%")
    print("Email Sequence:")
    for email in res["email_sequence"]:
        print(f"  [Day {email['day']}] Subject: {email['subject']} (Variant: {email['variant']})")

if __name__ == "__main__":
    main()
