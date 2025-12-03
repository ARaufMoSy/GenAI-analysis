import google.generativeai as genai
import time

API_KEY = "AIzaSyDqGueA1pjjVDXPcoISIzLGNA2CXaPhsKw"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('models/gemini-2.5-flash')

INPUT_COST = 0.075
OUTPUT_COST = 0.30


def customer_support_cost():
    email = "I ordered product #12345 but haven't received it. Where is my order?"
    response = model.generate_content(f"Reply professionally to: {email}")

    input_tokens = response.usage_metadata.prompt_token_count
    output_tokens = response.usage_metadata.candidates_token_count
    cost = (input_tokens / 1_000_000 * INPUT_COST) + (output_tokens / 1_000_000 * OUTPUT_COST)

    monthly_cost = cost * 500 * 22

    print("=" * 70)
    print("USE CASE 1: Customer Support Automation")
    print("=" * 70)
    print(f"Scenario: AI replies to customer inquiries")
    print(f"Volume:   500 emails/day × 22 working days")
    print(f"\nTokens:   {input_tokens} input + {output_tokens} output = {input_tokens + output_tokens} total")
    print(f"Cost:     ${cost:.6f} per email")
    print(f"Monthly:  ${monthly_cost:.2f} (€{monthly_cost * 0.92:.2f})")
    print(f"\nBenefit:  Saves ~4 hours/day of support agent time")

    return monthly_cost, input_tokens + output_tokens


def data_analysis_cost():
    report = """
    Sales Report Q4 2024:
    Revenue: €450,000 (up 18%)
    Top client: BMW (€80,000)
    New customers: 12
    Lost deals: 3 (price too high)
    """

    response = model.generate_content(f"Summarize in 3 bullet points:\n{report}")

    input_tokens = response.usage_metadata.prompt_token_count
    output_tokens = response.usage_metadata.candidates_token_count
    cost = (input_tokens / 1_000_000 * INPUT_COST) + (output_tokens / 1_000_000 * OUTPUT_COST)

    monthly_cost = cost * 30 * 22

    print("\n" + "=" * 70)
    print("USE CASE 2: Sales Report Summarization")
    print("=" * 70)
    print(f"Scenario: AI summarizes daily sales reports for management")
    print(f"Volume:   30 reports/day × 22 working days")
    print(f"\nTokens:   {input_tokens} input + {output_tokens} output = {input_tokens + output_tokens} total")
    print(f"Cost:     ${cost:.6f} per report")
    print(f"Monthly:  ${monthly_cost:.2f} (€{monthly_cost * 0.92:.2f})")
    print(f"\nBenefit:  Saves ~2 hours/day of analyst time")

    return monthly_cost, input_tokens + output_tokens


def translation_cost():
    german_text = "Premium Laptop mit 16GB RAM, ideal für Business-Anwendungen"
    response = model.generate_content(f"Translate to English: {german_text}")

    input_tokens = response.usage_metadata.prompt_token_count
    output_tokens = response.usage_metadata.candidates_token_count
    cost = (input_tokens / 1_000_000 * INPUT_COST) + (output_tokens / 1_000_000 * OUTPUT_COST)

    total_cost = cost * 200

    print("\n" + "=" * 70)
    print("USE CASE 3: Product Catalog Translation (DE→EN)")
    print("=" * 70)
    print(f"Scenario: Translate product descriptions for international market")
    print(f"Volume:   200 products (one-time project)")
    print(f"\nTokens:   {input_tokens} input + {output_tokens} output = {input_tokens + output_tokens} total")
    print(f"Cost:     ${cost:.6f} per translation")
    print(f"Total:    ${total_cost:.2f} (€{total_cost * 0.92:.2f})")
    print(f"\nSavings:  €{2000 - total_cost * 0.92:.2f} vs human translator (€2,000)")

    return total_cost, input_tokens + output_tokens


def show_business_summary():
    print("\n" + "█" * 70)
    print("  🤖 GEMINI AI - BUSINESS COST ANALYSIS")
    print("█" * 70 + "\n")

    support_cost, support_tokens = customer_support_cost()
    time.sleep(5)

    analysis_cost, analysis_tokens = data_analysis_cost()
    time.sleep(5)

    translation_cost_val, translation_tokens = translation_cost()

    total_monthly = support_cost + analysis_cost
    total_yearly = total_monthly * 12
    total_tokens = (support_tokens * 500 * 22) + (analysis_tokens * 30 * 22)

    print("\n" + "=" * 70)
    print("💰 COST SUMMARY")
    print("=" * 70)

    print(f"\nMonthly Recurring Costs:")
    print(f"  Customer Support:    ${support_cost:>8.2f}  (€{support_cost * 0.92:>7.2f})")
    print(f"  Report Analysis:     ${analysis_cost:>8.2f}  (€{analysis_cost * 0.92:>7.2f})")
    print(f"  {'-' * 50}")
    print(f"  Total/month:         ${total_monthly:>8.2f}  (€{total_monthly * 0.92:>7.2f})")
    print(f"  Total/year:          ${total_yearly:>8.2f}  (€{total_yearly * 0.92:>7.2f})")

    print(f"\nOne-time Project:")
    print(f"  Translation:         ${translation_cost_val:>8.2f}  (€{translation_cost_val * 0.92:>7.2f})")

    print(f"\nToken Usage (Monthly):")
    print(f"  Total tokens/month:  {total_tokens:,}")
    print(f"  Well within free tier limit (1M tokens/day)")

    # ROI
    support_hours = 4 * 22  # 4 hours/day
    analyst_hours = 2 * 22  # 2 hours/day
    hourly_rate = 30
    time_value = (support_hours + analyst_hours) * hourly_rate

    print(f"\n" + "=" * 70)
    print("📊 ROI ANALYSIS")
    print("=" * 70)
    print(f"\nTime Saved:")
    print(f"  Support team:  {support_hours} hours/month × €{hourly_rate}/hour = €{support_hours * hourly_rate}")
    print(f"  Analysts:      {analyst_hours} hours/month × €{hourly_rate}/hour = €{analyst_hours * hourly_rate}")
    print(f"  Total value:   €{time_value}/month")

    print(f"\nCost vs Value:")
    print(f"  AI cost:       €{total_monthly * 0.92:.2f}/month")
    print(f"  Value created: €{time_value}/month")
    print(f"  Net benefit:   €{time_value - total_monthly * 0.92:.2f}/month")
    print(f"  ROI:           {((time_value - total_monthly * 0.92) / (total_monthly * 0.92) * 100):.0f}%")

    print(f"\n" + "=" * 70)
    print("✅ RECOMMENDATION")
    print("=" * 70)
    print(f"\nFor an investment of €{total_monthly * 0.92:.2f}/month, the company saves")
    print(
        f"€{time_value}/month in labor costs - a {((time_value - total_monthly * 0.92) / (total_monthly * 0.92) * 100):.0f}% return.")
    print(f"\nImplementation cost is negligible. Recommend immediate deployment.")
    print("\n" + "=" * 70 + "\n")


if __name__ == "__main__":
    show_business_summary()